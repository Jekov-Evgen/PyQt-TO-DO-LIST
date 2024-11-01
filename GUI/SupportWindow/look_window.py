from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from DB.working_with_database import all_db
from GUI.Style.style import CONST_LOOK_WINDOW

def sort(arr_task_bd):
    result = sorted(arr_task_bd, key=lambda x: x[1])
    return result

class LookWindowTask(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1024, 768)
        self.setWindowTitle('Look Window')
        self.setStyleSheet(CONST_LOOK_WINDOW)
        self.sc = QScrollArea()
        
        
        get_bd = all_db()
        sort_data = sort(get_bd)
        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        title = QHBoxLayout()
        title_id = QLabel(text="ID")
        title_pr = QLabel(text="Priority")
        title_text = QLabel(text="Task")
        
        title.addWidget(title_id, alignment=Qt.AlignmentFlag.AlignTop)
        title.addWidget(title_pr, alignment=Qt.AlignmentFlag.AlignTop)
        title.addWidget(title_text, alignment=Qt.AlignmentFlag.AlignTop)
        
        central_widget.setLayout(control_UI)
        
        control_UI.addLayout(title)
        
        for i in range(len(sort_data)):
            control_task = QHBoxLayout()
            
            l_id = QLabel(text=str(sort_data[i][0]))
            l_pr = QLabel(text=str(sort_data[i][1]))
            l_text = QLabel(text=str(sort_data[i][2]))
            
            l_id.setObjectName("taskLabel")
            l_pr.setObjectName("taskLabel")
            l_text.setObjectName("taskLabel")
            
            control_task.addWidget(l_id)
            control_task.addWidget(l_pr)
            control_task.addWidget(l_text)
            
            control_UI.addLayout(control_task)
            
        self.setCentralWidget(central_widget)
        
        title_id.setObjectName("taskLabel")
        title_pr.setObjectName("taskLabel")
        title_text.setObjectName("taskLabel")
        
        self.sc.setWidgetResizable(True)
        
        self.show()
                
            