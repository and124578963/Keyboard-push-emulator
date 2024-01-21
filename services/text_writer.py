import logging
import random
from time import sleep

from services.win_helper import Win32Helper


class TextWriter:
    def __init__(self, timeout, min_interval, max_interval, text):
        self.timeout = float(timeout)
        self.min_inteval = float(min_interval) / 1000
        self.max_interval = float(max_interval) / 1000
        self.text = text
        self.log = logging.getLogger("TextWriter")
        self.win32 = Win32Helper()

        if isinstance(self.text, str) == False:
            raise AttributeError('The message is not a string')

    def run(self):
        sleep(self.timeout)
        self.write_text()

    def write_text(self):
        for ch in self.text:
            key_s = self.win32.char_to_win32_key_signal(ch)
            max_attempts = 5
            while -1 in key_s:
                self.win32.change_keyboard_layout()
                key_s = self.win32.char_to_win32_key_signal(ch)
                self.log.debug(f"'char {ch}', signal '{key_s}', attempt {max_attempts}")
                max_attempts -= 1
                if max_attempts == 0:
                    break
            if max_attempts == 0:
                self.log.warning(f"Couldn't get the keyboard shortcut to print the character '{ch}'")
                continue

            self.win32.press_btn(key_s)
            sleep(random.uniform(self.min_inteval, self.max_interval))




