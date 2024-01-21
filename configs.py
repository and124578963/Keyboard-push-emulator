import logging
import logging.handlers
import os

import win32con as wcon
from PyQt5.QtGui import QFontDatabase

# Клавиши для переключения языка раскладки клавиатуры:
# wcon.VK_MENU - alt
# wcon.VK_SHIFT - shift
# https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
CHANGE_KEYBOARD_LAYOUT_KEY1 = wcon.VK_LWIN  # leftwindow
CHANGE_KEYBOARD_LAYOUT_KEY2 = wcon.VK_SPACE  # spacebar

BASE_DIR = os.path.dirname(__file__)

def get_abs_path(local_path):
    return os.path.join(BASE_DIR.replace("\\", "/"), local_path)


def init_fonts():
    f1 = QFontDatabase.addApplicationFont(get_abs_path('style/fonts/Roboto-Regular.ttf'))
    f2 = QFontDatabase.addApplicationFont(get_abs_path('style/fonts/Roboto-Medium.ttf'))

    if f1 == -1 or f2 == -1:
        logging.error("Шрифты Roboto не установлены")


logging.basicConfig(
                level=logging.DEBUG,
                format="%(asctime)s [%(levelname)s] %(name)s - %(filename)s - %(funcName)s: %(message)s",
                handlers=[
                    logging.StreamHandler(),
                    logging.handlers.RotatingFileHandler(
                            filename="./log.txt",
                            maxBytes=100,
                            backupCount=0,
                            encoding="UTF-8",
                    ),
                ],
        )

logging.getLogger("TextWriter").setLevel(logging.DEBUG)




