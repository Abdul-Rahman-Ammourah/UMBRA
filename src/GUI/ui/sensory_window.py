from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QLabel, QFormLayout, 
                            QLineEdit, QPushButton, QTextEdit)
from PyQt5.QtCore import Qt
#from password_sug.password_sug import PasswordSuggester

class SensorySuggestionWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("SENSORY QUESTIONS INPUT")
        self.setGeometry(150, 150, 600, 700)
        self.setStyleSheet("background-color: #121212; color: #00ff00;")
        self.collected_answers = {}
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

        self.generate_btn = QPushButton("GENERATE PASSWORDS")
        self.generate_btn.setStyleSheet(self.collect_btn.styleSheet())
        self.generate_btn.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_btn)

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
        answers = {}
        for idx, input_field in enumerate(self.input_fields, start=1):
            answer = input_field.text().strip()
            answers[f'question_{idx}'] = answer

        self.answers_display.clear()
        self.answers_display.append("COLLECTED ANSWERS:\n")
        for i, (key, value) in enumerate(answers.items(), 1):
            display_value = value if value else "[No Answer Provided]"
            self.answers_display.append(f"{i}. {display_value}")

        self.collected_answers = answers

    def generate_passwords(self):
        self.collect_answers()
        if not self.collected_answers:
            self.answers_display.append("\n[ERROR] No answers collected.")
            return

        self.answers_display.append("\n[INFO] Generating passwords using DeepSeek...\n")

        suggester = PasswordSuggester(model="deepseek")
        passwords = suggester.suggest_passwords(self.collected_answers)

        self.answers_display.append("AI-SUGGESTIONS PASSWORDS:\n")
        for i, pw in enumerate(passwords, 1):
            self.answers_display.append(f"{i}. {pw}")

    def generate_passwords(self):
        # ... (same generate_passwords code as original) ...
        pass