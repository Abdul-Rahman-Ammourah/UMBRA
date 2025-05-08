import time
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QPushButton, 
                            QLabel, QFrame, QHBoxLayout)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QTextCursor
from .gen_window import GenerationWindow
from .sug_window import SuggestionWindow
from .sensory_window import SensorySuggestionWindow
from .widgets import HackerTerminal

class UMRBAMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UMBRA")
        self.setGeometry(500, 250, 800, 600)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        self.setStyleSheet("background-color: #121212;")
        self.init_ui()
    
    def init_ui(self):
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Header with animated effect
        header = QLabel("""
 ██╗   ██╗███╗   ███╗██████╗ ██████╗  █████╗ 
 ██║   ██║████╗ ████║██╔══██╗██╔══██╗██╔══██╗
 ██║   ██║██╔████╔██║██████╔╝██████╔╝███████║
 ██║   ██║██║╚██╔╝██║██╔══██╗██╔══██╗██╔══██║
 ╚██████╔╝██║ ╚═╝ ██║██████╔╝██║  ██║██║  ██║
  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
        """)
        header.setStyleSheet("""
            color: #00ff00;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            font-weight: bold;
            padding: 10px;
            border-bottom: 1px solid #005500;
        """)
        header.setAlignment(Qt.AlignCenter)
        layout.addWidget(header)
        
        # Create terminal output
        self.terminal = HackerTerminal()
        layout.addWidget(self.terminal)
        
        # Create button panel
        button_panel = QFrame()
        button_panel.setStyleSheet("""
            background-color: #0a0a0a;
            border: 1px solid #005500;
            border-radius: 3px;
            padding: 10px;
        """)
        button_layout = QHBoxLayout()
        button_panel.setLayout(button_layout)
        
        # Generate button
        self.btn_generate = QPushButton("TARGETED GENERATION")
        self.btn_generate.setStyleSheet("""
            QPushButton {
                background-color: #003300;
                color: #00ff00;
                border: 1px solid #00aa00;
                padding: 8px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005500;
            }
            QPushButton:pressed {
                background-color: #001100;
            }
        """)
        self.btn_generate.clicked.connect(self.open_generation_window)
        button_layout.addWidget(self.btn_generate)
        
        # Suggest button
        self.btn_suggest = QPushButton("PERSONAL SUGGESTION")
        self.btn_suggest.setStyleSheet(self.btn_generate.styleSheet())
        self.btn_suggest.clicked.connect(self.open_suggestion_window)
        button_layout.addWidget(self.btn_suggest)
        
        # Exit button
        self.btn_exit = QPushButton("TERMINATE")
        self.btn_exit.setStyleSheet("""
            QPushButton {
                background-color: #330000;
                color: #ff0000;
                border: 1px solid #aa0000;
                padding: 8px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #550000;
            }
            QPushButton:pressed {
                background-color: #110000;
            }
        """)
        self.btn_exit.clicked.connect(self.close)
        button_layout.addWidget(self.btn_exit)
        
        layout.addWidget(button_panel)
        
        # Status bar
        self.status_bar = QLabel("SYSTEM READY")
        self.status_bar.setStyleSheet("""
            color: #00aa00;
            font-family: 'Courier New', monospace;
            font-size: 11px;
            border-top: 1px solid #005500;
            padding: 5px;
        """)
        layout.addWidget(self.status_bar)
        
        # Initial boot sequence
        self.boot_sequence()
    
 
    def boot_sequence(self):
        messages = [
            "INITIALIZING UMBRA SECURITY SYSTEM...",
            "LOADING CRYPTOGRAPHIC MODULES...",
            "ESTABLISHING SECURE CONNECTION...",
            "VERIFYING SYSTEM INTEGRITY...",
            "ALL SYSTEMS OPERATIONAL",
            "UMBRA IS NOW ONLINE"
        ]
        
        self.terminal.append("> SYSTEM BOOT SEQUENCE INITIATED")
        for i, msg in enumerate(messages):
            QTimer.singleShot(800 * i, lambda m=msg: self.typewriter_effect(m))
    

    def typewriter_effect(self, text):
        for i in range(len(text) + 1):
            QTimer.singleShot(50 * i, lambda t=text[:i]: self.update_terminal(t))
    
    def update_terminal(self, text):
        self.terminal.moveCursor(QTextCursor.End)
        self.terminal.insertPlainText("\r> " + text)
        self.terminal.moveCursor(QTextCursor.End)
        self.terminal.ensureCursorVisible()
    
    def open_generation_window(self):
        self.terminal.append("\n> OPENING TARGETED GENERATION MODULE...")
        self.generation_window = GenerationWindow(self)
        self.generation_window.exec_()
        self.terminal.append("> RETURNED TO MAIN INTERFACE")
    
    def open_suggestion_window(self):
        self.terminal.append("\n> OPENING PERSONAL SUGGESTION MODULE...")
        self.suggestion_window = SuggestionWindow(self)
        self.suggestion_window.exec_()
        self.terminal.append("> RETURNED TO MAIN INTERFACE")