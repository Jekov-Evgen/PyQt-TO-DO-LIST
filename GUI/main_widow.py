from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('TO-DO-LIST')
        
        self.show()
        