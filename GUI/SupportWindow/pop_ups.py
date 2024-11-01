from PyQt6.QtWidgets import QMessageBox

def err():
    error = QMessageBox()
    error.setWindowTitle("Error")
    error.setText("input error")
    error.show()
    
def result(title : str, text : str):
    pass

class Result:
    def __init__(self, title, text) -> None:
        self.res = QMessageBox()
        self.res.setWindowTitle(title)
        self.res.setText(text)
        self.res.show()