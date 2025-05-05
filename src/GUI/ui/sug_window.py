from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QFormLayout, 
                            QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from GUI.core.generator import PasswordGenerator

class SuggestionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PERSONAL PASSWORD SUGGESTION")
        self.setGeometry(600, 300, 500, 400)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Title
        title = QLabel("PERSONAL INFORMATION COLLECTION")
        title.setStyleSheet("font-family: 'Courier New'; font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Form layout for input fields
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        
        self.username_input = QLineEdit()
        self.email_input = QLineEdit()
        self.birthdate_input = QLineEdit()
        self.favorites_input = QLineEdit()
        
        for widget in [self.username_input, self.email_input, 
                      self.birthdate_input, self.favorites_input]:
            widget.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)
        
        form.addRow("Your Username:", self.username_input)
        form.addRow("Your Email:", self.email_input)
        form.addRow("Your Birthdate:", self.birthdate_input)
        form.addRow("Your Favorites:", self.favorites_input)
        
        layout.addLayout(form)
        
        # Suggest button
        self.suggest_btn = QPushButton("GENERATE PERSONAL SUGGESTIONS")
        self.suggest_btn.setStyleSheet("""
            QPushButton {
                background-color: #003300;
                color: #00ff00;
                border: 1px solid #00aa00;
                padding: 10px;
                font-family: 'Courier New';
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005500;
            }
        """)
        self.suggest_btn.clicked.connect(self.generate_suggestions)
        layout.addWidget(self.suggest_btn)
        
        # Password display
        self.password_display = QTextEdit()
        self.password_display.setStyleSheet("""
            background-color: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New';
            border: 1px solid #005500;
            padding: 5px;
        """)
        self.password_display.setReadOnly(True)
        layout.addWidget(self.password_display)
    def generate_suggestions(self):
        user_info = {
            'username': self.username_input.text(),
            'email': self.email_input.text(),
            'birthdate': self.birthdate_input.text(),
            'hobbies': self.favorites_input.text()
        }
        
        passwords = PasswordGenerator.generate_targeted_password(user_info, num_passwords=5)
        
        self.password_display.clear()
        self.password_display.append("SUGGESTED PASSWORDS:\n")
        for i, pwd in enumerate(passwords, 1):
            self.password_display.append(f"{i}. {pwd}")
        
        self.password_display.append("\nSelect one and copy it to your clipboard")
