from sensory_suggestion_window import SensorySuggestionWindow
from password_suggestion import PasswordSuggester
from PyQt5.QtWidgets import QApplication
import sys

def main():
    # Initialize Qt application
    app = QApplication(sys.argv)

    # Open sensory questions window
    sensory_window = SensorySuggestionWindow()
    sensory_window.exec_()  # User fills and saves answers

    # Collect answers
    answers = getattr(sensory_window, 'collected_answers', {})
    if not answers:
        print("[ERROR] No answers collected.")
        sys.exit()

    # Choose model: DeepSeek or QROK
    print("\nGenerating passwords using DeepSeek model...\n")
    deep_suggester = PasswordSuggester(model="deepseek")
    deep_passwords = deep_suggester.suggest_passwords(answers)

    print("Results from DeepSeek:")
    for i, pw in enumerate(deep_passwords, 1):
        print(f"{i}. {pw}")

    print("\nGenerating passwords using QROK model...\n")
    qrok_suggester = PasswordSuggester(model="qrok")
    qrok_passwords = qrok_suggester.suggest_passwords(answers)

    print("Results from QROK:")
    for i, pw in enumerate(qrok_passwords, 1):
        print(f"{i}. {pw}")

    sys.exit()

if __name__ == "__main__":
    main()



