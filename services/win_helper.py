import ctypes
import logging
from time import sleep
from typing import List, Tuple

import win32api as wapi
import win32con as wcon


class Win32Helper:
    # The following two constants indicate a hotkey that changes the keyboard layout
    # in the system. Replace them in accordance with the 'mapping' dictionary keys
    # below if your hotkey differs.
    CHANGE_KEYBOARD_LAYOUT_KEY1 = wcon.VK_LWIN  # leftwindow
    CHANGE_KEYBOARD_LAYOUT_KEY2 = wcon.VK_SPACE  # spacebar

    KEYEVENTF_KEYUP = wcon.KEYEVENTF_KEYUP  # 0x0002
    KEYEVENTF_KEYDOWN = 0x0000

    def __init__(self):
        self.log = logging.getLogger("Win32Helper")

    def char_to_win32_key_signal(self, c) -> Tuple[int]:
        ret: List[int] = []
        is_capse = self._capslock_is_on()
        if c == "\n":
            ret.append(wcon.VK_RETURN)
        elif c == "\t":
            ret.append(wcon.VK_SPACE)
        else:
            res = wapi.VkKeyScanEx(c, self.get_keyboard_layout())
            if res == -1:
                return tuple((-1,))

            ss = (res >> 8) & 0xFF
            if (ss & 0x01 and not is_capse) or (not ss & 0x01 and is_capse):
                ret.append(wcon.VK_SHIFT)
            if ss & 0x02:
                ret.append(wcon.VK_SPACE)
            if ss & 0x04:
                ret.append(wcon.VK_MENU)
            ret.append(res & 0xFF)
        return tuple(ret)

    def press_btn(self, list_key_codes: Tuple[int, ...]):
        interval = 0.001
        for key in list_key_codes:
            self._press_event(key)
            sleep(interval)
        for key in reversed(list_key_codes):
            self._unpress_event(key)
            sleep(interval)

    def _capslock_is_on(self) -> bool:
        return wapi.GetKeyState(wcon.VK_CAPITAL)

    @classmethod
    def _press_event(cls, key_code):
        ctypes.windll.user32.keybd_event(key_code, 0, cls.KEYEVENTF_KEYDOWN, 0)

    @classmethod
    def _unpress_event(cls, key_code):
        ctypes.windll.user32.keybd_event(key_code, 0, cls.KEYEVENTF_KEYUP, 0)

    def get_keyboard_layout(self, thread_id=0):
        current_window = ctypes.windll.user32.GetForegroundWindow()
        if thread_id == 0:
            thread_id = ctypes.windll.user32.GetWindowThreadProcessId(current_window, 0)
            # keyboard_language_id made up of 0xAAABBBB, where
        # AAA = HKL (handle object), BBBB = language ID
        keyboard_language_id = ctypes.windll.user32.GetKeyboardLayout(thread_id)
        # Language ID -> low 10 bits, Sub-language ID -> high 6 bits
        language_id = keyboard_language_id & (2 ** 16 - 1)
        # Convert language ID from decimal to hexadecimal
        language_id_hex = language_id
        return language_id_hex

    def change_keyboard_layout(self):
        change_layout_btn = (self.CHANGE_KEYBOARD_LAYOUT_KEY1, self.CHANGE_KEYBOARD_LAYOUT_KEY2,)
        self.press_btn(change_layout_btn)
        self.log.debug(f'Switched to {self.get_keyboard_layout()} keyboard layout')
        sleep(0.1)
