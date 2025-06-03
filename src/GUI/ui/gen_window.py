"""Password Generation GUI Module.

This module provides a terminal-style interface for targeted password generation
using personal information. The interface features:
- Typewriter effect console output
- Target profile collection form
- Real-time generation status
- Cyberpunk aesthetic styling
"""

from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QGridLayout,
    QLineEdit, QPushButton, QMessageBox, QApplication, QTextEdit
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon, QTextCursor
import os
from GUI.core.generator import password_generator

class GenerationWindow(QDialog):
    """Main password generation dialog window.
    
    Inherits from QDialog to provide a modal interface for the password
    generation workflow with cyberpunk terminal styling.

    Attributes:
        terminal (QTextEdit): Console-style output display
        username_input (QLineEdit): Target name field
        birthdate_input (QLineEdit): Birth year field  
        hobbies_input (QLineEdit): Hobbies/interests field
        fav_input (QLineEdit): Favorite items field
        city_input (QLineEdit): Location field
        chunksize_input (QLineEdit): Password count field
        generate_btn (QPushButton): Main action button
        status_label (QLabel): Operation status display

    Signals:
        (Inherited from QDialog)
    """

    def __init__(self, parent=None):
        """Initialize the generation window.
        
        Args:
            parent (QWidget, optional): Parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("UMBRA - Password Generation")
        self.setGeometry(600, 300, 700, 600)
        self.setStyleSheet("""
            background-color: #121212;
            color: #00ff00;
            font-family: 'Courier New';
        """)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.png'))
        self.init_ui()

    def init_ui(self):
        """Initialize UI components and layout."""
        layout = QVBoxLayout(self)

        # Terminal output
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
        layout.addWidget(self.terminal)

        # [Rest of UI initialization...]

    def typewriter_effect(self, text, delay=30):
        """Animate text output with typewriter effect.
        
        Args:
            text (str): Text to display
            delay (int): Milliseconds between characters
        """
        if not hasattr(self, 'char_queue'):
            self.char_queue = []
        self.char_queue.extend(text)
        if not hasattr(self, 'type_timer'):
            self.type_timer = QTimer(self)
            self.type_timer.timeout.connect(self.process_next_char)
        self.type_timer.start(delay)

    def process_next_char(self):
        """Process next character in typewriter queue."""
        if self.char_queue:
            ch = self.char_queue.pop(0)
            self.terminal.moveCursor(QTextCursor.End)
            self.terminal.insertPlainText(ch)
            self.terminal.moveCursor(QTextCursor.End)
        else:
            self.type_timer.stop()

    def generate_passwords(self):
        """Handle password generation workflow.
        
        1. Validates input fields
        2. Displays target profile
        3. Initiates generation
        4. Handles results
        """
        try:
            chunksize = int(self.chunksize_input.text() or 100)
            if chunksize <= 0:
                raise ValueError
        except ValueError:
            chunksize = 100
            self.typewriter_effect("Using default 100 passwords\n")

        profile = {
            'Uname': self.username_input.text(),
            'Byear': self.birthdate_input.text(),
            'Fav': self.fav_input.text(),
            'City': self.city_input.text(),
            'Hobby': self.hobbies_input.text(),
            'Chunksize': chunksize
        }

        # [Rest of generation logic...]

    def finish_generation(self, user_info):
        """Finalize generation and save results.
        
        Args:
            user_info (dict): Profile information used for generation
        """
        passwords, time_taken = password_generator(**user_info)
        if not passwords:
            self.typewriter_effect("\n[ERROR] Generation failed\n")
            return

        # [Rest of save logic...]