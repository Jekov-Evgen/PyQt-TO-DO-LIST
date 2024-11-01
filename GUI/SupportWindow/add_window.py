from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from GUI.Style.style import CONST_ADD_WINDOW
from GUI.SupportWindow.pop_ups import err, Result
from DB.working_with_database import add_db, all_task_db

class AddWindowTask(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Add task")
        self.setStyleSheet(CONST_ADD_WINDOW)
        
        self.call_err = None
        self.res = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        priority = QLabel(text="priority")
        self.enter_priority = QLineEdit()
        text_task = QLabel(text="enter text task")
        self.enter_text = QLineEdit()
        
        add_task = QPushButton(text="Add")
        add_task.clicked.connect(self.add_processing)
        
        control_UI.addWidget(priority, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.enter_priority)
        control_UI.addWidget(text_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.enter_text)
        control_UI.addWidget(add_task)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def add_processing(self):
        try:
            pr = int(self.enter_priority.text())
            tx = str(self.enter_text.text())
        except:
            self.call_err = err()
        
        add_db(pr, tx)
        
        self.res = Result("Successful addition!", "Your task has been added!")