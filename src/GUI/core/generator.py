import requests
from typing import List, Tuple, Dict

def password_generator(user_info: Dict[str, str]) -> Tuple[List[str], float]:
    """
    Sends user_info to the local password generation API and returns generated passwords.

    Args:
        user_info (Dict[str, str]): Dictionary with keys Uname, Byear, Fav, City, Hobby, Chunksize.

    Returns:
        Tuple[List[str], float]: A tuple of (list of generated passwords, time taken).
    """
    try:
        response = requests.post(
            "http://192.168.1.197:8000/generate-passwords",
            json={
                "Uname": user_info.get("Uname", ""),
                "Byear": user_info.get("Byear", ""),
                "Fav": user_info.get("Fav", ""),
                "City": user_info.get("City", ""),
                "Hobby": user_info.get("Hobby", ""),
                "Chunksize": user_info.get("Chunksize", 100)
            }
        )
        response.raise_for_status()
        json_response = response.json()

        if isinstance(json_response, list):
            return json_response, 0.0

        return json_response.get("results", []), json_response.get("time_taken_seconds", 0.0)

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to contact password generation API: {e}")
        return [], 0.0
