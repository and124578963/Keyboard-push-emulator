from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QSizePolicy

from configs import get_abs_path
from services.text_writer import TextWriter
from ui.elementls import ColorButton, create_horizontal_w_lo, generate_font, CustomTextEdit, CustomEntry, get_h_spacer


class MainWindow_UI(QMainWindow):
    def __init__(self):
        super(MainWindow_UI, self).__init__()

        self.text_entry = None
        self.min_speed_entry = None
        self.timeout_entry = None
        self.max_speed_entry = None

        self.central_widget = QtWidgets.QWidget(parent=self)
        self.setCentralWidget(self.central_widget)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.top_area_widget = QtWidgets.QWidget(parent=self)
        self.vertical_layout.addWidget(self.top_area_widget)
        self.top_area_horizontal_lo = QtWidgets.QHBoxLayout(self.top_area_widget)

        self.config_area = QtWidgets.QWidget(parent=self.top_area_widget)
        self.top_area_horizontal_lo.addWidget(self.config_area)
        self.config_lo = QtWidgets.QVBoxLayout(self.config_area)

        self.configure_structure()
        self.draw_ui_elements()
        self._set_window_icon()
        self.setWindowTitle("Генератор нажатий")

    def configure_structure(self):
        self.top_area_widget.setFixedHeight(125)
        # self.setFixedWidth(500)
        self.config_lo.setContentsMargins(0, 0, 0, 0)
        self.config_area.setFixedWidth(230)
        self.top_area_horizontal_lo.setContentsMargins(0, 0, 0, 0)
        self.config_lo.setSpacing(0)

    def draw_ui_elements(self):
        self.vertical_layout.setSpacing(0)
        self.draw_timeout()
        self.draw_speed()
        self.draw_text_area()
        self.draw_start()

    def draw_start(self):
        start_btn = ColorButton(self.top_area_widget, "blue")
        start_btn.setText("Напечатать")
        start_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        start_btn.clicked.connect(self.start)
        self.top_area_horizontal_lo.addWidget(start_btn)

    def start(self):
        TextWriter(
            self.timeout_entry.text(),
            self.min_speed_entry.text(),
            self.max_speed_entry.text(),
            self.text_entry.toPlainText()
        ).run()

    def draw_text_area(self):
        w, lo = create_horizontal_w_lo(self.central_widget, self.vertical_layout)
        text_label = QtWidgets.QLabel(parent=w)
        text_label.setText("Текст для печати:")
        text_label.setFont(generate_font(9, bold=True))
        text_label.setContentsMargins(0, 18, 0, 6)
        lo.addWidget(text_label)

        w, lo = create_horizontal_w_lo(self.central_widget, self.vertical_layout)
        self.text_entry = CustomTextEdit(w)
        self.text_entry.setFont(generate_font(8))
        lo.addWidget(self.text_entry)

    def draw_timeout(self):
        w, lo = create_horizontal_w_lo(self.config_area, self.config_lo)
        timeout_label = QtWidgets.QLabel(parent=w)
        timeout_label_end = QtWidgets.QLabel(parent=w)
        self.timeout_entry = CustomEntry(w, only_numeric=True)

        timeout_label.setText("Таймаут:")
        timeout_label.setFont(generate_font(9, bold=True))
        self.timeout_entry.setText("5")
        self.timeout_entry.setToolTip("Время, через которое начнется печать текста после старта.")
        self.timeout_entry.setMaximumWidth(50)
        timeout_label_end.setText("сек")

        lo.addWidget(timeout_label)
        lo.addWidget(self.timeout_entry)
        lo.addWidget(timeout_label_end)
        lo.addItem(get_h_spacer())
        lo.setSpacing(10)

    def draw_speed(self):
        tooltip = "Случайное время между нажатиями клавиш из диапазона min-max"

        w, lo = create_horizontal_w_lo(self.config_area, self.config_lo)
        speed_label = QtWidgets.QLabel(parent=w)
        speed_label.setText("Интервал нажатий:")
        speed_label.setFont(generate_font(9, bold=True))
        speed_label.setContentsMargins(0, 18, 0, 6)
        lo.addWidget(speed_label)

        w, lo = create_horizontal_w_lo(self.config_area, self.config_lo)
        min_speed_label = QtWidgets.QLabel(parent=w)
        self.min_speed_entry = CustomEntry(w, only_numeric=True)
        min_speed_label.setText("min:")
        self.min_speed_entry.setText("5")
        self.min_speed_entry.setToolTip(tooltip)
        self.min_speed_entry.setMaximumWidth(50)
        lo.addWidget(min_speed_label)
        lo.addWidget(self.min_speed_entry)

        _label = QtWidgets.QLabel(parent=w)
        _label.setText(" - ")
        lo.addWidget(_label)

        max_speed_label = QtWidgets.QLabel(parent=w)
        max_speed_label.setText("max:")
        self.max_speed_entry = CustomEntry(w, only_numeric=True)
        self.max_speed_entry.setText("100")
        self.max_speed_entry.setToolTip(tooltip)
        self.max_speed_entry.setMaximumWidth(50)
        lo.addWidget(max_speed_label)
        lo.addWidget(self.max_speed_entry)

        _label = QtWidgets.QLabel(parent=w)
        _label.setText(" мс")
        lo.addWidget(_label)

        lo.addItem(get_h_spacer())

    def _set_window_icon(self):
        self.setWindowIcon(QtGui.QIcon(get_abs_path('style\\icon.png')))

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        exit(0)