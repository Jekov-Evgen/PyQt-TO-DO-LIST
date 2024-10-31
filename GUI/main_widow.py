from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from GUI.Style.style import CONST_MAIN_WINDOW, CONST_ADD_WINDOW
from GUI.AddWindow.add_window import AddWindowTask

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('TO-DO-LIST')
        self.setStyleSheet(CONST_MAIN_WINDOW)
        
        self.add = None
        
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        greet = QLabel(text="hello, select action")
        
        add_to_db = QPushButton(text='add record')
        add_to_db.clicked.connect(self.add_task)
        
        delete_to_db = QPushButton(text="delete record")
        look_db = QPushButton(text="view entries")
        
        control_UI.addWidget(greet, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(add_to_db)
        control_UI.addWidget(delete_to_db)
        control_UI.addWidget(look_db)
        
        central_widget.setLayout(control_UI)
        
        self.setCentralWidget(central_widget)
        
        self.show()
        
    def add_task(self):
        self.add = AddWindowTask()
        