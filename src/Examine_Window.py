from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from assets.ui.examine_window_ui import Ui_examine_window
import assets.resources.resources_rc

class Examine_Window(QMainWindow):
    def __init__(self) -> None:
        super(Examine_Window, self).__init__()
        self.__ui = Ui_examine_window()

        self.__ui.setupUi(self)

        ui = self.__ui
        self.__QUESTION_BUTTONS = [ ui.question_1, ui.question_2, ui.question_3, ui.question_4, ui.question_5,
                                    ui.question_6, ui.question_7, ui.question_8, ui.question_9, ui.question_10,
                                    ui.question_11, ui.question_12, ui.question_13, ui.question_14, ui.question_15,
                                    ui.question_16, ui.question_17, ui.question_18, ui.question_19, ui.question_20,
                                    ui.question_21, ui.question_22, ui.question_23, ui.question_24, ui.question_25 ]
        
        self.__setting_up_button()

        self.setWindowTitle("Sát hạch lái xe A1")
        self.setWindowIcon(QIcon(":icons/app_icon"))

    def __setting_up_button(self):
        self.__load_button_icon()

    def __load_button_icon(self):
        self.__ui.next_question.setIcon(QIcon(":icons/next"))
        self.__ui.previous_question.setIcon(QIcon(":icons/previous"))
        self.__ui.submit.setIcon(QIcon(":icons/submit"))