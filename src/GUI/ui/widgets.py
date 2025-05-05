from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor

class HackerTerminal(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            background-color: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New', monospace;
            font-size: 12px;
            border: 1px solid #00aa00;
            padding: 5px;
        """)
        self.setReadOnly(True)
        self.setLineWrapMode(QTextEdit.NoWrap)
        
    def append(self, text):
        self.moveCursor(QTextCursor.End)
        self.insertPlainText(text + "\n")
        self.ensureCursorVisible()