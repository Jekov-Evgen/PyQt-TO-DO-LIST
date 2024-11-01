from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from GUI.Style.style import CONST_MAIN_WINDOW
from GUI.SupportWindow.add_window import AddWindowTask
from GUI.SupportWindow.delete_window import DeleteWindowTask
from GUI.SupportWindow.look_window import LookWindowTask

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('TO-DO-LIST')
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        self.add = None
        self.delete = None
        self.look_t = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greet = QLabel(text="hello, select action")
        
        add_to_db = QPushButton(text='add record')
        add_to_db.clicked.connect(self.add_task)
        
        delete_to_db = QPushButton(text="delete record")
        delete_to_db.clicked.connect(self.del_task)
        
        look_db = QPushButton(text="view entries")
        look_db.clicked.connect(self.look_task)
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(add_to_db)
        control_UI.addWidget(delete_to_db)
        control_UI.addWidget(look_db)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def add_task(self):
        self.add = AddWindowTask()
        
    def del_task(self):
        self.delete = DeleteWindowTask()
        
    def look_task(self):
        self.look_t = LookWindowTask()
        