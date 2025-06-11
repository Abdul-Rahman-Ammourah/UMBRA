"""AES-GCM Password Cracking Module.

This module provides functionality to:
- Crack AES-GCM encrypted files using generated password lists
- Handle cryptographic operations securely
- Detect original file types after decryption
- Provide progress feedback during cracking attempts

Security Note:
- Uses PBKDF2 for key derivation (1000 iterations by default)
- Verifies authentication tags before decryption
- Handles corrupted/malformed files gracefully
"""

import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from utils.decrypt_utils import detect_file_type

def cracker():
    """Interactive AES-GCM password cracking workflow.
    
    Steps:
    1. Collects encrypted file path
    2. Lists available password wordlists
    3. Attempts decryption with selected wordlist
    4. Saves successfully decrypted files
    
    File Handling:
    - Expects files with format: [salt(16)][nonce(16)][tag(16)][ciphertext]
    - Outputs to: <original_name>_decrypted.<detected_extension>
    
    Returns:
        str: The successful password if found, None otherwise
        
    Example:
        >>> cracker()
        [SYSTEM] AES-GCM Password Cracker Initialized
        Enter the path to the encrypted file: test.enc
        ...
        [✓] Password found: correct_password
        [INFO] Detected file type: .pdf
        'correct_password'
    """
    print("[SYSTEM] Initializing Cracker...")

    # File input validation
    enc_file = input("Enter encrypted file path: ").strip()
    if not os.path.isfile(enc_file):
        print(f"[ERROR] File not found: {enc_file}")
        return None

    # Password directory setup
    password_dir = os.path.join("src", "ai", "GeneratedPasswords")
    if not os.path.isdir(password_dir):
        print(f"[ERROR] Missing password directory: {password_dir}")
        return None

    # Password file selection
    password_files = sorted([
        f for f in os.listdir(password_dir)
        if f.startswith("password") and f.endswith(".txt")
    ])

    if not password_files:
        print("[ERROR] No password lists available")
        return None

    print("\nAvailable password lists:")
    for idx, fname in enumerate(password_files, 1):
        print(f"{idx}. {fname}")

    try:
        choice = int(input(f"Select wordlist (1-{len(password_files)}): ").strip())
        selected_file = password_files[choice - 1]
    except (ValueError, IndexError):
        print("[ERROR] Invalid selection")
        return None

    # Cryptographic processing
    with open(enc_file, 'rb') as f:
        data = f.read()

    if len(data) < 48:  # 16+16+16+min_ciphertext
        print("[ERROR] Invalid file structure")
        return None

    salt, nonce, tag = data[:16], data[16:32], data[32:48]
    ciphertext = data[48:]
    output_base = f"{os.path.splitext(enc_file)[0]}_decrypted"

    # Password cracking attempt
    with open(os.path.join(password_dir, selected_file)) as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(f"\n[STATUS] Testing {len(passwords)} passwords...")

    for i, pwd in enumerate(passwords, 1):
        try:
            key = PBKDF2(pwd, salt, dkLen=32)
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            
            ext = detect_file_type(plaintext)
            output_path = f"{output_base}{ext}"
            
            with open(output_path, 'wb') as f:
                f.write(plaintext)
                
            print(f"\n[SUCCESS] Password: {pwd}\n")
            print(f"File saved to: {output_path}\n")
            return pwd
            
        except (ValueError, KeyError):
            if i % 300 == 0:
                print(f"Attempted {i}/{len(passwords)}...")

    print("\n[FAILURE] No matching password found")
    return None