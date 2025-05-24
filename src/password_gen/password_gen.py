import os
import requests
from typing import List, Tuple

def password_generator(Uname: str = "Ahmed", Byear: str = "1999", Fav: str = "Camping", City: str = "Japan", Hobby: str = "Jazz", Chunksize: int = 100) -> Tuple[List[str], float]:
    """
    Sends user data to a local GPT-2 model backend API to generate passwords.

    Args:
        Uname (str): Target Username.
        Byear (str): Target Birthday.
        Fav (str): Target Favorite item/thing.
        City (str): Target City.
        Hobby (str): Target Hobby.
        Chunksize (int): Number of iterations (generates multiple outputs per batch).

    Returns:
        Tuple[List[str], float]: A tuple containing a list of unique generated passwords and the time taken.
    """
    try:
        response = requests.post(
            "http://192.168.1.197:8000/generate-passwords",
            json={
                "Uname": Uname,
                "Byear": Byear,  
                "Fav": Fav,
                "City": City,
                "Hobby": Hobby,
                "Chunksize": Chunksize
            }
        )
        response.raise_for_status()
        json_response = response.json()
        
        # Handle case where API returns a list directly
        if isinstance(json_response, list):
            return json_response, 0.0
        
        # Handle case where API returns a dictionary
        return json_response.get("results", []), json_response.get("time_taken_seconds", 0.0)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to contact password generation API: {e}")
        return [], 0.0

def generate_password_list():
    print("[SYSTEM] Generating password list...")

    uname = input("Enter target's name: ")
    byear = input("Enter birth year: ")
    fav = input("Enter favorite thing: ")
    city = input("Enter city: ")
    hobby = input("Enter hobby: ")
    chunksize_input = input("Enter the number of passwords to generate (default 100): ")

    try:
        chunksize = int(chunksize_input)
    except ValueError:
        chunksize = 100

    passwords, timetaken = password_generator(uname, byear, fav, city, hobby, chunksize)

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

    if len(passwords) != chunksize:
        try:
            with open("src\\ai\\GeneratedPasswords\\filler.txt", "r", encoding="utf-8") as f:
                filler_passwords = f.read().splitlines()
            while len(passwords) < chunksize:
                passwords.extend(filler_passwords[:chunksize - len(passwords)])
            passwords = passwords[:chunksize]
        except FileNotFoundError:
            print("[WARNING] filler.txt not found. Saving fewer passwords.")

    with open(filename, "w", encoding="utf-8") as f:
        for pw in passwords:
            f.write(pw + "\n")

    print(f"[SYSTEM] Time taken: {timetaken} seconds.")
    print(f"[SYSTEM] Generated {len(passwords)} passwords and saved to {filename}.")
