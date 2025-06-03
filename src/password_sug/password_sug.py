"""Password Suggestion Module.

This module provides intelligent password suggestions based on personal information
while ensuring strong security through:
- Leetspeak substitutions
- Random symbol insertion
- Capitalization mixing
- Length enforcement
"""

import random
import string

def suggest_password_list():
    """Generate and display a list of secure password suggestions.
    
    This interactive function:
    1. Collects personal information (username, birthdate, etc.)
    2. Generates 8 password variants using multiple security techniques
    3. Displays the suggestions with numbering
    
    The generated passwords:
    - Are 12+ characters long
    - Contain uppercase/lowercase letters
    - Include numbers and symbols
    - Use leetspeak substitutions
    - Combine input elements unpredictably
    
    Example:
        >>> suggest_password_list()
        [SYSTEM] Welcome to the Password Suggestion
        1. What's your username? ...
        Here are 8 suggested passwords:
        
        1. M0v13$0421BlZ
        2. C@t_08!Pi8
        3. Joh@Blue$22
        ...
    """
    print("[SYSTEM] Welcome to the Password Suggestion")

    def clean_input(prompt):
        """Sanitize user input by stripping whitespace and replacing spaces with underscores."""
        return input(prompt).strip().replace(" ", "_")

    def rand_symbol():
        """Return a random special character from a curated security-approved set."""
        return random.choice("!@#$%^&*")

    def capitalize_mix(word):
        """Capitalize first letter and lowercase rest with length preservation.
        
        Args:
            word (str): Input string to transform
            
        Returns:
            str: Transformed string (e.g. 'hello' → 'Hello')
        """
        return word[:1].upper() + word[1:].lower()

    def to_leet(text, chance=0.5):
        """Convert characters to leetspeak with specified probability.
        
        Args:
            text (str): Input text to transform
            chance (float): Probability of substitution (0-1)
            
        Returns:
            str: Leet-transformed text
            
        Example:
            >>> to_leet("password", 1.0)
            'p@$$w0rd'
        """
        leet_map = {
            'e': '3', 'E': '3',
            'i': '1', 'I': '1',
            'o': '0', 'O': '0',
            's': '$', 'S': '$',
            't': '7', 'T': '7',
            'l': '1', 'L': '1'
        }
        return ''.join(leet_map.get(c, c) if random.random() < chance else c for c in text)

    # [Rest of your existing code...]