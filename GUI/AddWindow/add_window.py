from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from GUI.Style.style import CONST_ADD_WINDOW

class AddWindowTask(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Add task")
        self.setStyleSheet(CONST_ADD_WINDOW)
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        l_add_task = QLabel(text="enter data")
        priority = QLabel(text="priority")
        enter_priority = QLineEdit()
        text_task = QLabel(text="enter text task")
        enter_text = QLineEdit()
        id_ = QLabel(text="id for search")
        enter_id = QLineEdit()
        add_task = QPushButton(text="add task to list")
        
        control_UI.addWidget(l_add_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(priority, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(enter_priority)
        control_UI.addWidget(text_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(enter_text)
        control_UI.addWidget(id_, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(enter_id)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()