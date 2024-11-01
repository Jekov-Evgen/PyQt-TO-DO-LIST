from PyQt6.QtWidgets import QMessageBox
from GUI.Style.style import CONST_MESSAGE_BOX

class Error:
    def __init__(self) -> None:
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setText("input error")
        self.error.setStyleSheet(CONST_MESSAGE_BOX)
        self.error.show()

class Result:
    def __init__(self, title, text) -> None:
        self.res = QMessageBox()
        self.res.setWindowTitle(title)
        self.res.setText(text)
        self.res.setStyleSheet(CONST_MESSAGE_BOX)
        self.res.show()