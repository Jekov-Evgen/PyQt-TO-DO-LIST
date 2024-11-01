from PyQt6.QtWidgets import QMessageBox
    
class Error:
    def __init__(self) -> None:
        self.error = QMessageBox()
        self.error.setWindowTitle("Error")
        self.error.setText("input error")
        self.error.show()

class Result:
    def __init__(self, title, text) -> None:
        self.res = QMessageBox()
        self.res.setWindowTitle(title)
        self.res.setText(text)
        self.res.show()