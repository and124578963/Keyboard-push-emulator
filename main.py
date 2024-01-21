import sys
import logging

from PyQt5.QtWidgets import QApplication

from configs import init_fonts
from ui.windows import MainWindow_UI


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)
    logging.error(exception, exc_info=True)


if __name__ == "__main__":

    if sys.platform != 'win32':
        raise Exception('Currently supports only Windows OS!')

    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    init_fonts()
    window = MainWindow_UI()
    window.show()

    sys.exit(app.exec())
