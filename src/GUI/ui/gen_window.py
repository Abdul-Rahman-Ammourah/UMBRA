from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QGridLayout,
    QLineEdit, QPushButton, QMessageBox, QApplication, QTextEdit
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QTextCursor
import time
from GUI.core.generator import PasswordGenerator
import os
class GenerationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("UMBRA")
        self.setGeometry(600, 300, 700, 600)
        self.setStyleSheet("""
            background-color: #121212;
            color: #00ff00;
            font-family: 'Courier New';
        """)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        # Terminal-style display
        self.terminal = QTextEdit(readOnly=True)
        self.terminal.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a0a;
                color: #00ff00;
                border: 2px solid #005500;
                padding: 10px;
                font-family: 'Courier New';
                font-size: 12px;
            }
        """)
        self.terminal.setMinimumHeight(150)
        layout.addWidget(self.terminal)

        # Title
        title = QLabel("TARGET INFORMATION COLLECTION")
        title.setStyleSheet("font-size: 16px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Form layout
        grid = QGridLayout()
        # First column
        grid.addWidget(QLabel("Name:"), 0, 0)
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("e.g., johnsmith")
        self.username_input.textChanged.connect(lambda txt: self.update_terminal("Name", txt))
        grid.addWidget(self.username_input, 0, 1)

        grid.addWidget(QLabel("Birthdate:"), 1, 0)
        self.birthdate_input = QLineEdit()
        self.birthdate_input.setPlaceholderText("e.g., 1990")
        self.birthdate_input.textChanged.connect(lambda txt: self.update_terminal("Birthdate", txt))
        grid.addWidget(self.birthdate_input, 1, 1)

        grid.addWidget(QLabel("Hobbies:"), 2, 0)
        self.hobbies_input = QLineEdit()
        self.hobbies_input.setPlaceholderText("e.g., gaming, reading")
        self.hobbies_input.textChanged.connect(lambda txt: self.update_terminal("Hobbies", txt))
        grid.addWidget(self.hobbies_input, 2, 1)

        # Second column
        grid.addWidget(QLabel("Favorite:"), 0, 2)
        self.fav_input = QLineEdit()
        self.fav_input.setPlaceholderText("e.g., pizza, BMW, Messi")
        self.fav_input.textChanged.connect(lambda txt: self.update_terminal("Favorite", txt))
        grid.addWidget(self.fav_input, 0, 3)

        grid.addWidget(QLabel("City:"), 1, 2)
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("e.g., New York, Jordan, Syria")
        self.city_input.textChanged.connect(lambda txt: self.update_terminal("City", txt))
        grid.addWidget(self.city_input, 1, 3)

        grid.addWidget(QLabel("Chunksize:"), 2, 2)
        self.chunksize_input = QLineEdit()
        self.chunksize_input.setPlaceholderText("Optional, default: 100")
        self.chunksize_input.textChanged.connect(lambda txt: self.update_terminal("Chunk Size", txt))
        grid.addWidget(self.chunksize_input, 2, 3)

        # Style inputs
        for w in [
            self.username_input, self.birthdate_input, self.hobbies_input,
            self.fav_input, self.city_input, self.chunksize_input
        ]:
            w.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)

        layout.addLayout(grid)

        # Generate button
        self.generate_btn = QPushButton("GENERATE TARGETED PASSWORDS")
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #003300;
                color: #00ff00;
                border: 1px solid #00aa00;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #005500;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_btn)

        # Status
        self.status_label = QLabel("READY FOR INPUT", alignment=Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Initialize terminal with typewriter
        self.typewriter_effect("Initializing TARGETED PASSWORD GENERATION system...\n")
        self.typewriter_effect("Loading target profile modules...\n")
        self.typewriter_effect("System ready for target data input.\n\n", delay=0)

    def typewriter_effect(self, text, delay=30):
        """Typewriter effect using a queue and single timer."""
        if not hasattr(self, 'char_queue'):
            self.char_queue = []
        self.char_queue.extend(text)
        if not hasattr(self, 'type_timer'):
            self.type_timer = QTimer(self)
            self.type_timer.timeout.connect(self.process_next_char)
        self.type_timer.setInterval(delay)
        if not self.type_timer.isActive():
            self.type_timer.start()

    def process_next_char(self):
        if self.char_queue:
            ch = self.char_queue.pop(0)
            self.terminal.moveCursor(QTextCursor.End)
            self.terminal.insertPlainText(ch)
            self.terminal.moveCursor(QTextCursor.End)
        else:
            self.type_timer.stop()

    def update_terminal(self, field, value):
        if not value:
            return
        lines = self.terminal.toPlainText().splitlines()
        for i, line in enumerate(lines):
            if line.startswith(f"{field}:"):
                lines[i] = f"{field}: {value}"
                break
        else:
            lines.append(f"{field}: {value}")
        # keep last 15
        if len(lines) > 15:
            lines = lines[-15:]
        self.terminal.setPlainText("\n".join(lines))
        self.terminal.moveCursor(QTextCursor.End)

    def generate_passwords(self):
        self.typewriter_effect("\n\nInitializing password generation sequence...\n")
        self.typewriter_effect("Compiling target data...\n")

        try:
            chunksize_val = int(self.chunksize_input.text())
            if chunksize_val <= 0:
                raise ValueError
        except ValueError:
            chunksize_val = 100  # Default value
    
        user_info = {
            'Uname': self.username_input.text(),
            'Byear': self.birthdate_input.text(),
            'Fav': self.fav_input.text(),
            'City': self.city_input.text(),
            'Hobby': self.hobbies_input.text(),
            'Chunksize': chunksize_val
    }   
    
        self.typewriter_effect("\nTARGET PROFILE:\n")
        for k, v in user_info.items():
            display_value = v if v else "None"
            self.typewriter_effect(f"- {k}: {display_value}\n")


        self.typewriter_effect("\nGenerating targeted password variants...\n")
        QApplication.processEvents()

        # Call the generation
        try:
            QTimer.singleShot(7500, lambda: self.finish_generation(user_info))
        except Exception as e:
            self.typewriter_effect("\n[ERROR] Password generation failed.\n")
            self.typewriter_effect(f"Reason: {str(e)}\n")
            self.status_label.setText("GENERATION FAILED")
            QMessageBox.critical(self, "Error", f"Failed to generate passwords:\n{str(e)}")

    def finish_generation(self, user_info):
        passwords = PasswordGenerator.generate_targeted_password(user_info)
        directory = "src\\ai\\GeneratedPasswords"
        os.makedirs(directory, exist_ok=True)
        counter = 1
        while True:
            filename = os.path.join(directory, f"passwords{counter}.txt")
            if not os.path.exists(filename):
                break
            counter += 1
    
        with open(filename, "w", encoding="utf-8") as f:
            for pw in passwords:
                f.write(pw + "\n")

        self.typewriter_effect("\nGeneration complete!\n")
        self.typewriter_effect(f"Created {len(passwords)} password variants\n")
        self.typewriter_effect(f"Results saved to: {filename}\n\n\n")

        self.status_label.setText(f"SAVED TO {filename}")