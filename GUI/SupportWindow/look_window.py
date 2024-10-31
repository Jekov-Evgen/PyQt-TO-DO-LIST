from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from DB.working_with_database import all_task

class LookWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Look Window')
        
        result = all_task()
        list_Ql = []
        
        for i in range(len(result)):
            list_Ql.append(QLabel())

        for i in range(len(result)):
            list_Ql[i].setText(result[i])
            