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
