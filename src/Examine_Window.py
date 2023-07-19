from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from assets.ui.examine_window_ui import Ui_examine_window
import assets.resources.resources_rc

class Examine_Window(QMainWindow):
    def __init__(self) -> None:
        super(Examine_Window, self).__init__()
        self.__ui = Ui_examine_window()

        self.__ui.setupUi(self)

        self.__setting_up_button()

        self.setWindowTitle("Sát hạch lái xe A1")
        self.setWindowIcon(QIcon(":icons/app_icon"))

    def __setting_up_button(self):
        self.__load_button_icon()
        self.__connect_button_signal_and_slot()

    def __load_button_icon(self):
        self.__ui.next_question.setIcon(QIcon(":icons/next"))
        self.__ui.previous_question.setIcon(QIcon(":icons/previous"))
        self.__ui.submit.setIcon(QIcon(":icons/submit"))

    def __connect_button_signal_and_slot(self):
        self.__ui.next_question.clicked.connect(self.move_to_next_question)
        self.__ui.previous_question.clicked.connect(self.move_to_previous_question)
        self.__ui.submit.clicked.connect(self.submit)