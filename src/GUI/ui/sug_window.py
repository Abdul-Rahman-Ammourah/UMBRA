"""Password Suggestion Dialog Window.

Provides personalized password suggestions based on user-provided information
with security transformations including:
- Leetspeak substitutions
- Random symbol insertion
- Capitalization mixing
- Personal data combinations
"""
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QFormLayout,
                             QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import random

class PasswordSuggestionWindow(QDialog):
    """Interactive password suggestion dialog.

    Args:
        parent (QWidget, optional): Parent widget. Defaults to None.
    """
    def __init__(self, parent=None):
        """Initialize window with cyberpunk styling."""
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("UMBRA - Password Suggestion")
        self.setGeometry(650, 300, 600, 600)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.png'))
        self.setStyleSheet("""
            background-color: #121212;
            color: #00ff00;
            font-family: 'Courier New';
        """)
        self.init_ui()

    def init_ui(self):
        """Setup form inputs, generate button, and output display."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Form layout
        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignLeft)
        self.form_layout.setSpacing(15)

        # Input fields with placeholders
        self.fields = {
            'username': QLineEdit(),
            'birthdate': QLineEdit(),
            'favorite_thing': QLineEdit(),
            'color': QLineEdit(),
            'food': QLineEdit(),
            'animal': QLineEdit()
        }

        # Configure all fields with placeholders
        field_style = """
            QLineEdit {
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 8px;
                font-family: 'Courier New';
                min-width: 250px;
            }
            QLineEdit::placeholder {
                color: #007700;
                font-style: italic;
            }
        """
        
        # Set placeholders and styles
        self.fields['username'].setPlaceholderText("e.g., john_doe")
        self.fields['birthdate'].setPlaceholderText("e.g., 19900115")
        self.fields['favorite_thing'].setPlaceholderText("e.g., StarWars")
        self.fields['color'].setPlaceholderText("e.g., Blue")
        self.fields['food'].setPlaceholderText("e.g., Pizza")
        self.fields['animal'].setPlaceholderText("e.g., Cats")
        
        for field in self.fields.values():
            field.setStyleSheet(field_style)

        # Add fields to form
        self.form_layout.addRow("1. Username:", self.fields['username'])
        self.form_layout.addRow("2. Birthdate (YYYYMMDD):", self.fields['birthdate'])
        self.form_layout.addRow("3. Favorite thing (movie, car, etc.):", self.fields['favorite_thing'])
        self.form_layout.addRow("4. Favorite color:", self.fields['color'])
        self.form_layout.addRow("5. Favorite food:", self.fields['food'])
        self.form_layout.addRow("6. Favorite animal:", self.fields['animal'])

        layout.addLayout(self.form_layout)

        # Generate button
        self.generate_btn = QPushButton("GENERATE PASSWORDS")
        self.generate_btn.setStyleSheet("""
            QPushButton {
                background-color: #003300;
                color: #00ff00;
                border: 2px solid #00aa00;
                padding: 12px;
                font-weight: bold;
                font-family: 'Courier New';
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005500;
            }
            QPushButton:pressed {
                background-color: #002200;
            }
        """)
        self.generate_btn.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_btn)

        # Output area
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            QTextEdit {
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 12px;
                font-family: 'Courier New';
            }
        """)
        layout.addWidget(self.output)

    def clean_input(self, text):
        """Sanitize user input by stripping whitespace and replacing spaces.
        
        Args:
            text (str): Raw input text
            
        Returns:
            str: Cleaned text
        """
        return text.strip().replace(" ", "_")

    def rand_symbol(self):
        """Get random special character from security-approved set.
        
        Returns:
            str: Random symbol
        """
        return random.choice("!@#$%^&*")

    def capitalize_mix(self, word):
        """Capitalize first letter and lowercase remainder.
        
        Args:
            word (str): Input word
            
        Returns:
            str: Proper case word
        """
        if not word:
            return ""
        return word[:1].upper() + word[1:].lower()

    def to_leet(self, text, chance=0.5):
        """Convert characters to leetspeak with probability.
        
        Args:
            text (str): Input text
            chance (float): Substitution probability (0-1)
            
        Returns:
            str: Leet-transformed text
        """
        leet_map = {
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '$', 'S': '$',
            't': '7', 'T': '7',
            'l': '1', 'L': '1'
        }
        result = []
        for c in text:
            if c in leet_map and random.random() < chance:
                result.append(leet_map[c])
            else:
                result.append(c)
        return ''.join(result)

    def generate_passwords(self):
        """Generate and display password suggestions from form inputs."""
        # Clear previous output
        self.output.clear()
        
        # Get cleaned input values
        inputs = {key: self.clean_input(field.text()) for key, field in self.fields.items()}
        
        # Validate required fields
        if not all(inputs.values()):
            self.output.append("[ERROR] Please fill in all fields.")
            return
            
        try:
            year, month, day = inputs['birthdate'][:4], inputs['birthdate'][4:6], inputs['birthdate'][6:]
        except:
            self.output.append("[ERROR] Birthdate must be in YYYYMMDD format")
            return

        # Generate password suggestions
        suggestions = []
        
        # Template 1: FavoriteThing + day + symbol + color + Z
        pwd = f"{self.capitalize_mix(inputs['favorite_thing'])}{day}{self.rand_symbol()}{inputs['color'][:2].capitalize()}Z"
        suggestions.append(self.to_leet(pwd))
        
        # Template 2: Animal + _ + month + symbol + food + 8
        pwd = f"{self.capitalize_mix(inputs['animal'])}_{month}{self.rand_symbol()}{inputs['food'][:2].capitalize()}8"
        suggestions.append(self.to_leet(pwd))
        
        # Template 3: Username + @ + color + symbol + year
        pwd = f"{self.capitalize_mix(inputs['username'][:3])}@{inputs['color'].capitalize()}{self.rand_symbol()}{year[-2:]}"
        suggestions.append(self.to_leet(pwd))
        
        # Template 4: Food + _ + year + ! + random
        pwd = f"{self.capitalize_mix(inputs['food'])}_{year}!{random.randint(10,99)}"
        suggestions.append(self.to_leet(pwd))
        
        # Template 5: Animal + Luv + symbol + birthdate
        pwd = f"{self.capitalize_mix(inputs['animal'])}Luv{self.rand_symbol()}{inputs['birthdate'][-4:]}"
        suggestions.append(self.to_leet(pwd))
        
        # Template 6: Favorite + symbol + 4 + color + _ + month
        pwd = f"{self.capitalize_mix(inputs['favorite_thing'])}{self.rand_symbol()}4{inputs['color'].capitalize()}_{month}"
        suggestions.append(self.to_leet(pwd))
        
        # Template 7: Food + Crave + day + symbol
        pwd = f"{self.capitalize_mix(inputs['food'])}Cr@ve{day}{self.rand_symbol()}"
        suggestions.append(self.to_leet(pwd))
        
        # Template 8: Username + symbol + Fav + birthdate + animal
        pwd = f"{self.capitalize_mix(inputs['username'])}{self.rand_symbol()}Fav{inputs['birthdate'][-2:]}{inputs['animal'][:1].upper()}"
        suggestions.append(self.to_leet(pwd))

        # Display results
        self.output.append("[SYSTEM] Generated 8 strong passwords:\n")
        for i, pwd in enumerate(suggestions, 1):
            self.output.append(f"{i}. {pwd}")
