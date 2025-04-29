import sys
import random
import string
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                            QPushButton, QLabel, QTextEdit, QHBoxLayout, QFrame,
                            QLineEdit, QDialog, QFormLayout, QMessageBox)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont, QColor, QTextCursor, QPalette
import json
import time

# >>> Add by Mohammad Salah
# >>> Added by UMBRA Team: SensorySuggestionWindow Class for Input Collection Only <<<
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QTextEdit
from PyQt5.QtCore import Qt

class SensorySuggestionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("SENSORY QUESTIONS INPUT")
        self.setGeometry(150, 150, 600, 600)
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        title = QLabel("SENSORY QUESTIONS COLLECTION")
        title.setStyleSheet("font-family: 'Courier New'; font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignRight)

        # Define questions
        self.questions = [
            "What is your favorite color?",
            "What is your favorite car?",
            "What type of music or song do you love the most?",
            "What is your favorite book or movie?",
            "What is your favorite food or dish?",
            "What sport do you enjoy playing or watching?",
            "What is your favorite travel destination or place to visit?",
            "What is your favorite animal?",
            "What was your favorite subject in school?",
            "What do you usually do to relax or focus?"
        ]

        # Prepare input fields
        self.input_fields = []
        for question in self.questions:
            input_field = QLineEdit()
            input_field.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)
            self.form_layout.addRow(question, input_field)
            self.input_fields.append(input_field)

        layout.addLayout(self.form_layout)

        # Button to collect answers
        self.collect_btn = QPushButton("SAVE ANSWERS")
        self.collect_btn.setStyleSheet("""
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
        self.collect_btn.clicked.connect(self.collect_answers)
        layout.addWidget(self.collect_btn)

        # Display collected answers
        self.answers_display = QTextEdit()
        self.answers_display.setStyleSheet("""
            background-color: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New';
            border: 1px solid #005500;
            padding: 5px;
        """)
        self.answers_display.setReadOnly(True)
        layout.addWidget(self.answers_display)

    def collect_answers(self):
        """
        Collects answers from input fields and displays them.
        """
        answers = {}
        for idx, input_field in enumerate(self.input_fields, start=1):
            answer = input_field.text().strip()
            answers[f'question_{idx}'] = answer

        self.answers_display.clear()
        self.answers_display.append("COLLECTED ANSWERS:\n")
        for i, (key, value) in enumerate(answers.items(), 1):
            display_value = value if value else "[No Answer Provided]"
            self.answers_display.append(f"{i}. {display_value}")

        # Optionally: Save `answers` dict for later use if needed
        self.collected_answers = answers

# >>> End of SensorySuggestionWindow Class <<<

class PasswordGenerator:
    @staticmethod
    def generate_targeted_password(user_info, num_passwords=10):
        """Generate targeted passwords based on user information"""
        passwords = []
        base_info = [
            user_info.get('username', ''),
            user_info.get('email', '').split('@')[0],
            user_info.get('birthdate', ''),
            user_info.get('hobbies', '')
        ]
        
        # Generate variations
        for _ in range(num_passwords):
            password = []
            # Randomly combine parts of the information
            for info in base_info:
                if info:
                    # Take random slices of the info
                    if len(info) > 3:
                        start = random.randint(0, len(info)-3)
                        length = random.randint(2, min(5, len(info)-start))
                        password.append(info[start:start+length])
            
            # Add some special characters and numbers
            if password:
                password.append(random.choice("!@#$%^&*"))
                password.append(str(random.randint(10, 99)))
                random.shuffle(password)
                passwords.append(''.join(password))
        
        return passwords if passwords else ["No valid information provided"]

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

class GenerationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("TARGETED PASSWORD GENERATION")
        self.setGeometry(150, 150, 500, 400)
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Title
        title = QLabel("TARGET INFORMATION COLLECTION")
        title.setStyleSheet("font-family: 'Courier New'; font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Form layout for input fields
        form = QFormLayout()
        form.setLabelAlignment(Qt.AlignRight)
        
        self.username_input = QLineEdit()
        self.email_input = QLineEdit()
        self.birthdate_input = QLineEdit()
        self.hobbies_input = QLineEdit()
        
        for widget in [self.username_input, self.email_input, 
                      self.birthdate_input, self.hobbies_input]:
            widget.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)
        
        form.addRow("Target Username:", self.username_input)
        form.addRow("Target Email:", self.email_input)
        form.addRow("Target Birthdate:", self.birthdate_input)
        form.addRow("Target Hobbies:", self.hobbies_input)
        
        layout.addLayout(form)
        
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
            'username': self.username_input.text(),
            'email': self.email_input.text(),
            'birthdate': self.birthdate_input.text(),
            'hobbies': self.hobbies_input.text()
        }
        
        self.status_label.setText("GENERATING PASSWORDS...")
        QApplication.processEvents()  # Update UI
        
        # Simulate AI processing time
        time.sleep(2)
        
        passwords = PasswordGenerator.generate_targeted_password(user_info)
        
        # Save to file
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"targeted_passwords_{timestamp}.txt"
        with open(filename, 'w') as f:
            f.write("\n".join(passwords))
        
        self.status_label.setText(f"SAVED TO {filename}")
        QMessageBox.information(self, "Generation Complete", 
                               f"Generated {len(passwords)} passwords and saved to {filename}")

class SuggestionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("PERSONAL PASSWORD SUGGESTION")
        self.setGeometry(150, 150, 500, 400)
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

class UMRBAMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UMBRA // PASSWORD SECURITY SUITE")
        self.setGeometry(100, 100, 800, 600)
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
            "READY FOR USER INPUT"
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

def launch_gui():
    app = QApplication(sys.argv)
    
    # Set dark palette for the entire application
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(18, 18, 18))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(10, 10, 10))
    dark_palette.setColor(QPalette.AlternateBase, QColor(18, 18, 18))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(18, 18, 18))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Highlight, QColor(0, 85, 0))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)
    
    window = UMRBAMainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()
