import requests

class PasswordGenerator:
    @staticmethod
    def generate_targeted_password(user_info, num_passwords=10):
        """Generate targeted passwords based on user information"""
        
        Uname = user_info.get('Uname', ''),
        Byear = user_info.get('Byear', ''),
        Fav = user_info.get('Fav', ''),
        City = user_info.get('City', ''),
        Hobby = user_info.get('Hobby', ''),
        Chunksize = user_info.get('Chunksize', 100)

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