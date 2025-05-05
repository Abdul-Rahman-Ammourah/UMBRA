from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QGridLayout, 
                            QLineEdit, QPushButton, QMessageBox, QFormLayout, QApplication, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from GUI.core.generator import PasswordGenerator
import time
import random

class GenerationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TARGETED PASSWORD GENERATION")
        self.setGeometry(600, 300, 700, 500)
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        # Title
        title = QLabel("TARGET INFORMATION COLLECTION")
        title.setStyleSheet("font-family: 'Courier New'; font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Form layout for input fields
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        
        self.username_input = QLineEdit()
        self.birthdate_input = QLineEdit()
        self.hobbies_input = QLineEdit()
        self.fav_input = QLineEdit()
        self.city_input = QLineEdit()
        self.chucksize_input = QLineEdit()
        
        for widget in [self.username_input, self.birthdate_input, 
                      self.chucksize_input, self.hobbies_input,
                      self.fav_input, self.city_input]:
            widget.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)
        grid_layout = QGridLayout()
        
        # First column
        grid_layout.addWidget(QLabel("Name:"), 0, 0)
        grid_layout.addWidget(self.username_input, 0, 1)
        
        grid_layout.addWidget(QLabel("Birthdate:"), 1, 0)
        grid_layout.addWidget(self.birthdate_input, 1, 1)
        
        grid_layout.addWidget(QLabel("Hobbies:"), 2, 0)
        grid_layout.addWidget(self.hobbies_input, 2, 1)
        
        # Second column
        grid_layout.addWidget(QLabel("Favorite:"), 0, 2)
        grid_layout.addWidget(self.fav_input, 0, 3)
        
        grid_layout.addWidget(QLabel("City:"), 1, 2)
        grid_layout.addWidget(self.city_input, 1, 3)
        
        grid_layout.addWidget(QLabel("Chunksize:"), 2, 2)
        grid_layout.addWidget(self.chucksize_input, 2, 3)
        
        layout.addLayout(grid_layout)
        # Generate button
        self.generate_btn = QPushButton("GENERATE TARGETED PASSWORDS")
        self.generate_btn.setStyleSheet("""
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
        self.generate_btn.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_btn)


        # Status label
        self.status_label = QLabel("READY FOR INPUT")
        self.status_label.setStyleSheet("font-family: 'Courier New';")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

    def generate_passwords(self):
        user_info = {
            'Uname': self.username_input.text(),
            'Byear': self.birthdate_input.text(),
            'Fav': self.fav_input.text(),
            'City': self.city_input.text(),
            'Hobby': self.hobbies_input.text(),
            'Chunksize': self.chucksize_input.text()
        }
        self.status_label.setText(user_info.items())
        QApplication.processEvents()  # Update UI
        
                
        passwords = PasswordGenerator.generate_targeted_password(user_info)
        
        # Save to file
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"targeted_passwords_{timestamp}.txt"
        with open(filename, 'w') as f:
            f.write("\n".join(passwords))
        
        self.status_label.setText(f"SAVED TO {filename}")
        QMessageBox.information(self, "Generation Complete", 
                               f"Generated {len(passwords)} passwords and saved to {filename}")
