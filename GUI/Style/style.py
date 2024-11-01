CONST_MAIN_WINDOW = """
    QMainWindow {
        background-color: #1e1e1e; 
    }

    QLabel {
        color: #d4d4d4;
        font-size: 30px;
        font-weight: bold;
        padding: 10px;
    }

    QPushButton {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 16px;
        border-radius: 6px;
        padding: 8px;
        border: 1px solid #555555;
        margin: 5px 0;
    }

    QPushButton:hover {
        background-color: #505357; 
    }

    QPushButton:pressed {
        background-color: #3a3d41;
        border: 1px solid #6a6a6a; 
    }

    QPushButton#addButton {
        background-color: #007acc;
        color: white;
    }

    QPushButton#deleteButton {
        background-color: #d9534f;
        color: white;
    }

    QPushButton#viewButton {
        background-color: #f0ad4e;
        color: white;
    }
    
    QVBoxLayout {
        padding: 15px;
    }

    QWidget {
        background-color: #2d2d2d; 
        border-radius: 10px;
        margin: 10px;
    }
"""


CONST_ADD_WINDOW = """
    QMainWindow {
        background-color: #1e1e1e; 
    }

    QLabel {
        color: #d4d4d4;
        font-size: 20px;
        font-weight: bold;
        padding: 8px;
    }

    QLabel#l_add_task {
        font-size: 24px;
        font-weight: bold;
        color: #d4d4d4;
    }

    QLineEdit {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 16px;
        padding: 8px;
        border: 1px solid #555555;
        border-radius: 6px;
        margin: 5px 0;
    }

    QPushButton {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 16px;
        border-radius: 6px;
        padding: 10px;
        border: 1px solid #555555;
        margin: 5px 0;
    }

    QPushButton:hover {
        background-color: #505357; 
    }

    QPushButton:pressed {
        background-color: #3a3d41;
        border: 1px solid #6a6a6a; 
    }

    QPushButton#add_task {
        background-color: #007acc;
        color: white;
    }
    
    QWidget {
        background-color: #2d2d2d;
        border-radius: 10px;
        margin: 10px;
    }

    QVBoxLayout {
        padding: 15px;
    }
"""

CONST_DELETE_WINDOW = """
    QMainWindow {
        background-color: #1e1e1e; 
    }

    QLabel {
        color: #d4d4d4;
        font-size: 20px;
        font-weight: bold;
        padding: 8px;
    }

    QLabel#l_del_task {
        font-size: 24px;
        font-weight: bold;
        color: #d4d4d4;
    }

    QLineEdit {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 16px;
        padding: 8px;
        border: 1px solid #555555;
        border-radius: 6px;
        margin: 5px 0;
    }

    QPushButton {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 16px;
        border-radius: 6px;
        padding: 10px;
        border: 1px solid #555555;
        margin: 5px 0;
    }

    QPushButton:hover {
        background-color: #505357; 
    }

    QPushButton:pressed {
        background-color: #3a3d41;
        border: 1px solid #6a6a6a; 
    }

    QPushButton#del_task {
        background-color: #d9534f;
        color: white;
    }
    
    QWidget {
        background-color: #2d2d2d;
        border-radius: 10px;
        margin: 10px;
    }

    QVBoxLayout {
        padding: 15px;
    }
"""

CONST_MESSAGE_BOX = """
    QMessageBox {
        background-color: #1e1e1e;
        color: #d4d4d4;
        font-size: 16px;
        border-radius: 10px;
    }

    QMessageBox QLabel {
        color: #d4d4d4;
        font-size: 16px;
        font-weight: bold;
    }

    QMessageBox QPushButton {
        background-color: #3a3d41;
        color: #d4d4d4;
        font-size: 14px;
        border-radius: 6px;
        padding: 8px;
        border: 1px solid #555555;
    }

    QMessageBox QPushButton:hover {
        background-color: #505357; 
    }

    QMessageBox QPushButton:pressed {
        background-color: #3a3d41;
        border: 1px solid #6a6a6a;
    }
    
    QMessageBox QPushButton#okButton {
        background-color: #007acc;
        color: white;
    }

    QMessageBox QPushButton#cancelButton {
        background-color: #d9534f;
        color: white;
    }
"""

CONST_LOOK_WINDOW = """
    QMainWindow {
        background-color: #1b1b1b; 
        min-width: 1024px;
        min-height: 768px;
    }

    QLabel {
        color: #e0e0e0;
        font-size: 26px;
        font-weight: bold;
        padding: 15px;
        border: 2px solid #666666; /* Добавлена рамка для верхней строки заголовков */
        border-radius: 8px;
        background-color: #2e2e2e; /* Добавлен фон для рамок заголовков */
    }

    QLabel#taskLabel {
        color: #e0e0e0;
        font-size: 20px;
        padding: 12px;
        border: 1px solid #666666; /* Добавлена рамка для задач */
        border-radius: 8px;
        background-color: #3c3f42; /* Добавлен фон для рамок задач */
    }

    QPushButton {
        background-color: #45494d;
        color: #e0e0e0;
        font-size: 18px;
        border-radius: 8px;
        padding: 12px;
        border: 2px solid #666666;
        margin: 8px 0;
    }

    QPushButton:hover {
        background-color: #5c5f63; 
    }

    QPushButton:pressed {
        background-color: #45494d;
        border: 2px solid #828282; 
    }

    QPushButton#mainButton {
        background-color: #0091ea;
        color: white;
        font-size: 20px;
        font-weight: bold;
    }

    QLineEdit {
        background-color: #3c3f42;
        color: #e0e0e0;
        font-size: 18px;
        padding: 12px;
        border-radius: 8px;
        border: 2px solid #666666;
        margin: 8px 0;
    }
    
    QWidget {
        background-color: #292b2d;
        border-radius: 15px;
        margin: 12px;
    }

    QVBoxLayout, QHBoxLayout {
        padding: 20px;
        spacing: 15px;
    }
    
    QMessageBox {
        background-color: #1b1b1b;
        color: #e0e0e0;
        font-size: 18px;
        border-radius: 12px;
        padding: 20px;
    }

    QMessageBox QLabel {
        color: #e0e0e0;
        font-size: 18px;
    }

    QMessageBox QPushButton {
        background-color: #45494d;
        color: #e0e0e0;
        font-size: 16px;
        border-radius: 8px;
        padding: 10px;
        border: 2px solid #666666;
        margin: 5px;
    }

    QMessageBox QPushButton:hover {
        background-color: #5c5f63; 
    }

    QMessageBox QPushButton:pressed {
        background-color: #45494d;
        border: 2px solid #828282;
    }
"""