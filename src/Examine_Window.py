from PySide6.QtWidgets import QMainWindow
from assets.ui.examine_window_ui import Ui_examine_window
import assets.resources.resources_rc

class Examine_Window(QMainWindow):
    def __init__(self) -> None:
        super(Examine_Window, self).__init__()
        self.__ui = Ui_examine_window()

        self.__ui.setupUi(self)