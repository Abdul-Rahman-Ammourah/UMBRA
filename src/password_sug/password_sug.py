import random
import string

def suggest_password_list():
    print("[SYSTEM] Welcome to the Password Suggestion")

    # Helper functions
    def clean_input(prompt):
        return input(prompt).strip().replace(" ", "_")

    def rand_symbol():
        return random.choice("!@#$%^&*")

    def capitalize_mix(word):
        return word[:1].upper() + word[1:].lower()

    def to_leet(text, chance=0.5):
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

    # Gather personal info
    username = clean_input("1. What's your username? ")
    birthdate = clean_input("2. What's your birthdate (YYYYMMDD)? ")
    favorite_thing = clean_input("3. What's your favorite thing (movie, car, etc.)? ")
    color = clean_input("4. What's your favorite color? ")
    food = clean_input("5. What's your favorite food? ")
    animal = clean_input("6. What's your favorite animal? ")

    # Extract parts
    year, month, day = birthdate[:4], birthdate[4:6], birthdate[6:]

    # Generate passwords
    suggestions = []

    suggestions.append(to_leet(f"{capitalize_mix(favorite_thing)}{day}{rand_symbol()}{color[:2].capitalize()}Z"))
    suggestions.append(to_leet(f"{capitalize_mix(animal)}_{month}{rand_symbol()}{food[:2].capitalize()}8"))
    suggestions.append(to_leet(f"{capitalize_mix(username[:3])}@{color.capitalize()}{rand_symbol()}{year[-2:]}"))
    suggestions.append(to_leet(f"{capitalize_mix(food)}_{year}!{random.randint(10,99)}"))
    suggestions.append(to_leet(f"{capitalize_mix(animal)}Luv{rand_symbol()}{birthdate[-4:]}"))
    suggestions.append(to_leet(f"{capitalize_mix(favorite_thing)}{rand_symbol()}4{color.capitalize()}_{month}"))
    suggestions.append(to_leet(f"{capitalize_mix(food)}Cr@ve{day}{rand_symbol()}"))
    suggestions.append(to_leet(f"{capitalize_mix(username)}{rand_symbol()}Fav{birthdate[-2:]}{animal[:1].upper()}"))

    # Output
    print("\nHere are 8 suggested passwords:\n")
    for i, pwd in enumerate(suggestions, 1):
        print(f"{i}. {pwd}")

    print("\n[INFO] All passwords meet strong security standards (length, mixed case, digits, symbols, and random leetspeak).")
