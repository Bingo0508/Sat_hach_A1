from PySide6.QtWidgets import QApplication
import sys

def main() -> None:
    app = QApplication(sys.argv)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()