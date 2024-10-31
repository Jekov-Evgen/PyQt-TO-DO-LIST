from GUI.main_widow import MainWindow
from PyQt6.QtWidgets import QApplication
from DB.working_with_database import connect

if __name__ == "__main__":
    app = QApplication([])
    
    connect()
    
    start = MainWindow()
    
    app.exec()