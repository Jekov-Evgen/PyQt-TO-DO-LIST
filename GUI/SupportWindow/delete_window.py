from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from GUI.Style.style import CONST_DELETE_WINDOW

class DeleteWindowTask(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Delete Window")
        self.setStyleSheet(CONST_DELETE_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        l_del_task = QLabel(text="enter data")
        id_task = QLabel(text="enter id")
        id_task_enter = QLineEdit()
        del_task = QPushButton(text="Delete")
        
        control_UI.addWidget(l_del_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(id_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(id_task_enter)
        control_UI.addWidget(del_task)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()