from sensory_suggestion_window import SensorySuggestionWindow
from password_suggestion import PasswordSuggester

def generate_passwords_from_gui():
    sensory_window = SensorySuggestionWindow()
    sensory_window.exec_()  # This will auto-collect answers on close due to .accept override

    # Extract collected answers
    answers = getattr(sensory_window, 'collected_answers', {})
    if not answers:
        print("[ERROR] No answers were collected.")
        return

    suggester = PasswordSuggester(model="deepseek") 

    suggestions = suggester.suggest_passwords(answers)

    # Step 5: Print results
    print("\nAI-GENERATED PASSWORD SUGGESTIONS:")
    for i, pw in enumerate(suggestions, 1):
        print(f"{i}. {pw}")

# Run the generator if this file is executed
if __name__ == "__main__":
    generate_passwords_from_gui()


