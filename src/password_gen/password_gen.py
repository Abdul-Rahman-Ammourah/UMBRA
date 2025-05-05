import os
import requests
from typing import List

def password_generator(Uname: str = "Ahmed", Byear: str = "1999", Fav: str = "Camping", City: str = "Japan", Hobby: str = "Jazz", Chunksize : int = 100) -> List[str]:
    """
    Sends user data to a local GPT-2 model backend API to generate passwords.
    
    Args:
        Uname (str): Target Username.
        Byeat (str): Target Birthday.
        Fav (str): Target Favorite item/thing.
        City (str): Target City.
        Hobby (str): Target Hobby.
        Chunksize (int): Number of iterations (multiplied by 5 outputs per batch).
    
    Returns:
        List[str]: A list of unique generated passwords.
    """
    try:
        response = requests.post(
            "http://192.168.1.197:8000/generate-passwords",  # Replace with your backend IP:PORT
            json={
                "Uname": Uname,
                "Byeat": Byear,
                "Fav": Fav,
                "City": City,
                "Hobby": Hobby,
                "Chunksize": Chunksize
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to contact password generation API: {e}")
        return []

def generate_password_list():
    print("[SYSTEM] Generating password list...")

    uname = input("Enter target's name: ")
    byear = input("Enter birth year: ")
    fav = input("Enter favorite thing: ")
    city = input("Enter city: ")
    hobby = input("Enter hobby: ")
    chunksize_input = input("Enter the number of passwords to generate (default 500): ")

    try:
        chunksize = int(chunksize_input)
    except ValueError:
        chunksize = 100

    passwords = password_generator(uname, byear, fav, city, hobby, chunksize)

    if not passwords:
        print("[ERROR] No passwords generated.")
        return

    # Save to file
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

    print(f"[SYSTEM] Generated {len(passwords)} passwords and saved to {filename}.")
