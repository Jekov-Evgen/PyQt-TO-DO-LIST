from GUI.main_widow import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    
    start = MainWindow()
    
    app.exec()