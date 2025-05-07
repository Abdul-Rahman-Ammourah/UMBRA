import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import UMRBAMainWindow

def launch_gui():
    app = QApplication(sys.argv)
    window = UMRBAMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()