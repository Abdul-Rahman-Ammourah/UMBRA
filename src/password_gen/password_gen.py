from openai import OpenAI  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os
import csv

# Load environment variables from .env file
load_dotenv()

# Get DeepSeek API key
deep_seek_api_key = os.getenv('DEEP-SEEK-API')

# Initialize DeepSeek client
try:
    client = OpenAI(
        api_key=deep_seek_api_key,
        base_url="https://api.deepseek.com"
    )
except Exception as e:
    print(f"Error initializing DeepSeek client: {e}")
    client = None

def password_generator(user_input, total_length=12, num_uppercase=2, num_digits=2, num_special=2):
    """
    Generate passwords based on user input and password policies using DeepSeek AI.
    Args:
        user_input (list): List of strings from OSINT or user data.
        total_length (int): Desired total password length.
        num_uppercase (int): Number of uppercase letters required.
        num_digits (int): Number of digits required.
        num_special (int): Number of special characters required.

    Returns:
        list: List of generated passwords.
    """
    if client is None:
        print("DeepSeek client is not initialized.")
        return []

    # Check if user input exists
    if not user_input:
        print("No input data provided.")
        return []

    passwords = []

    for entry in user_input:
        # Create prompt based on user entry and password policy
        prompt = (
            f"You are a password generator AI. Based on the keyword '{entry}', generate a strong password. "
            f"Requirements: total length {total_length}, at least {num_uppercase} uppercase letters, {num_digits} digits, and {num_special} special characters. "
            f"Return ONLY the password without any explanation."
        )

        try:
            # Send request to DeepSeek AI
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are an expert password generator."},
                    {"role": "user", "content": prompt}
                ],
                stream=False
            )

            # Extract generated password
            generated_password = response.choices[0].message.content.strip()
            passwords.append(generated_password)

        except Exception as e:
            print(f"Error generating password for '{entry}': {e}")
            passwords.append("Error")

    return passwords
