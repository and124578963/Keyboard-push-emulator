from typing import Tuple

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QRegularExpression
from PyQt5.QtGui import QRegularExpressionValidator, QFont


class CustomEntry(QtWidgets.QLineEdit):
    def __init__(self, parent, only_numeric=False):
        super(CustomEntry, self).__init__(parent=parent)
        self.setMinimumSize(0, 32)
        self.setStyleSheet("""

        QLineEdit {
          border-bottom: 1px solid #aaa;
           border-right: 1px solid #aaa;
          border-radius: 2px;
          padding: 2px 5px;
                   }
        QLineEdit:focus {
             border-bottom: 1px solid #209fa6;
             border-right: 1px solid #209fa6;
        }
         QLineEdit:hover{

         }

        """)

        if only_numeric:
            reg_ex = QRegularExpression(r"[0-9]*[\,,.]{1}[0-9]*")
            validator = QRegularExpressionValidator(reg_ex)
            self.setValidator(validator)


class CustomTextEdit(QtWidgets.QTextEdit):
    def __init__(self, parent):
        super(CustomTextEdit, self).__init__(parent=parent)
        self.setStyleSheet("""
                QTextEdit {
                border-bottom: 1px solid #aaa;
                border-right: 1px solid #aaa;
                border-radius: 2px;
                }
                QTextEdit:focus {
                border-bottom: 1px solid #209fa6;
                border-right: 1px solid #209fa6;
                }
                QLineEdit:hover{
                }
                """)


class ColorButton(QtWidgets.QPushButton):
    def __init__(self, parent: QtWidgets.QWidget, color: str):
        super(ColorButton, self).__init__(parent=parent)
        dict_btn_color = {
            "blue": "#3f768d",
        }
        # self.setSizeIncrement(QtCore.QSize(0, 0))
        self.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        self.setObjectName(color)
        self.setStyleSheet("""
                QPushButton{{
                  color: #555;
                  font-weight: 700;
                  text-decoration: none;
                  padding: .3em 1em;
                  outline: none;
                  border: 1px solid #ddd;
                  border-radius: 0px;
                  transition: 0.3s;
                  background: #eee;
                }}

                QPushButton:hover {{
                  color: #fff;
                  background: {0};
                  border: 1px solid #ddd;
                }}
                
                QPushButton:pressed  {{
                  border: 2px solid {0};
                }}
                
                QPushButton::menu-indicator {{ image: none; }}
                
                """.format(dict_btn_color.get(color, "blue")))


def create_horizontal_w_lo(parent_w: QtWidgets.QWidget, parent_lo: QtWidgets.QBoxLayout) -> \
        Tuple[QtWidgets.QWidget, QtWidgets.QBoxLayout]:
    w = QtWidgets.QWidget(parent=parent_w)
    lo = QtWidgets.QHBoxLayout(w)
    lo.setSpacing(5)
    lo.setContentsMargins(0, 0, 0, 0)
    parent_lo.addWidget(w)
    return w, lo


def get_h_spacer():
    return QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Expanding,
                                 QtWidgets.QSizePolicy.Policy.Minimum)


def get_v_spacer():
    return QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                 QtWidgets.QSizePolicy.Policy.Expanding)


def generate_font(size: int, bold=False) -> QFont:
    if bold:
        font = QtGui.QFont("Roboto-Medium")
    else:
        font = QtGui.QFont("Roboto-Regular")

    font.setPointSize(size)
    return font
