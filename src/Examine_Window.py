from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from assets.ui.examine_window_ui import Ui_examine_window
import assets.resources.resources_rc

class Examine_Window(QMainWindow):
    def __init__(self) -> None:
        super(Examine_Window, self).__init__()
        self.__ui = Ui_examine_window()

        self.__ui.setupUi(self)

        self.setWindowTitle("Sát hạch lái xe A1")
        self.setWindowIcon(QIcon(":icons/app_icon"))

    def __load_button_icon(self):
        self.__ui.next_question.setIcon(QIcon(":icons/next"))
        self.__ui.previous_question.setIcon(QIcon(":icons/previous"))
        self.__ui.submit.setIcon(QIcon(":icons/submit"))