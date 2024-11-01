from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from GUI.Style.style import CONST_DELETE_WINDOW
from GUI.SupportWindow.pop_ups import Error, Result
from DB.working_with_database import del_db, add_db, all_db

class DeleteWindowTask(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle("Delete Window")
        self.setStyleSheet(CONST_DELETE_WINDOW)
        
        self.call_err = None
        self.res = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        id_task = QLabel(text="enter id")
        self.id_task_enter = QLineEdit()
        
        del_task = QPushButton(text="Delete")
        del_task.clicked.connect(self.del_processing)
        
        control_UI.addWidget(id_task, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.id_task_enter)
        control_UI.addWidget(del_task)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        self.show()
    
    def del_processing(self):
        try:
            ind = int(self.id_task_enter.text())
        except:
            self.call_err = Error()
        
        del_db(ind)
        
        self.res = Result("Successful delete!", "Your task has been deleted!")