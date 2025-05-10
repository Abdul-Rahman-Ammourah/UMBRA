from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QFormLayout,
                             QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys
import random
import string


class PasswordSuggestionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.setWindowTitle("UMBRA")
        self.setGeometry(650, 300, 600, 600)
        self.setWindowIcon(QIcon(r'Assets\UMBRA.ico'))
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.form_layout = QFormLayout()
        self.form_layout.setLabelAlignment(Qt.AlignLeft)

        # Personal Info Inputs
        self.inputs = {
            'username': QLineEdit(),
            'email': QLineEdit(),
            'birthdate': QLineEdit(),  # Format: YYYYMMDD
            'favorites': QLineEdit()
        }

        for key, widget in self.inputs.items():
            widget.setStyleSheet("""
                background-color: #0a0a0a;
                color: #00ff00;
                border: 1px solid #005500;
                padding: 5px;
            """)

        self.form_layout.addRow("Username:", self.inputs['username'])
        self.form_layout.addRow("Email:", self.inputs['email'])
        self.form_layout.addRow("Birthdate (YYYYMMDD):", self.inputs['birthdate'])
        self.form_layout.addRow("Favorites (e.g. car, movie):", self.inputs['favorites'])

        # Sensory Questions
        self.sensory_labels = ["Favorite Color:", "Favorite Food:", "Favorite Animal:", "Relaxing Activity:"]
        self.sensory_fields = []

        for label in self.sensory_labels:
            line = QLineEdit()
            line.setStyleSheet(self.inputs['username'].styleSheet())
            self.form_layout.addRow(label, line)
            self.sensory_fields.append(line)

        layout.addLayout(self.form_layout)

        # Suggest Button
        self.suggest_btn = QPushButton("SUGGEST PASSWORDS")
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
        self.suggest_btn.clicked.connect(self.suggest_passwords)
        layout.addWidget(self.suggest_btn)

        # Output Display
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet("""
            background-color: #0a0a0a;
            color: #00ff00;
            font-family: 'Courier New';
            border: 1px solid #005500;
            padding: 5px;
        """)
        layout.addWidget(self.output)

    def suggest_passwords(self):
        self.output.clear()
        values = {}

        for key, field in self.inputs.items():
            values[key] = field.text().strip()

        sensory_values = [field.text().strip() for field in self.sensory_fields]

        # Extract useful parts
        username = values['username']
        email = values['email']
        birthdate = values['birthdate']
        favorites = values['favorites']
        color, food, animal, activity = (sensory_values + [""] * 4)[:4]

        # Helpers
        def initials(text):
            return ''.join([word[0] for word in text.split() if word]).upper()

        def rand_chars(n=3):
            return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

        def get_birth_parts():
            if len(birthdate) == 8 and birthdate.isdigit():
                return birthdate[:4], birthdate[6:]
            return "2000", "01"

        birth_year, birth_day = get_birth_parts()

        # Generate passwords using templates
        suggestions = []

        if favorites and color:
            suggestions.append(f"{random.randint(10,99)}{favorites[:2].capitalize()}#{color[-1]}")

        if activity and animal:
            suggestions.append(f"{activity.capitalize()}{random.randint(100,999)}#{animal[:1].upper()}")

        if username and birth_year:
            suggestions.append(f"{birth_year}{initials(username)}@{rand_chars(3)}")

        if color and food and birth_day:
            suggestions.append(f"{color[0].upper()}{initials(food)}{birth_day}!{food[:2]}")

        if username and favorites:
            suggestions.append(f"{initials(username)}_{favorites[:3]}@{random.randint(10,99)}")

        self.output.append("SUGGESTED PASSWORDS:\n")
        for i, pwd in enumerate(suggestions[:5], 1):
            self.output.append(f"{i}. {pwd}")

        self.output.append("\n[INFO] These passwords include upper/lowercase, numbers, and symbols.")

## Testing the GUI
# Uncomment the following lines to run the GUI directly
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PasswordSuggestionWindow()
#     window.show()
#     sys.exit(app.exec_())
