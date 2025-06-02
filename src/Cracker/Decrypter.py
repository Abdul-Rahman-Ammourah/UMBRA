import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from utils.decrypt_utils import detect_file_type
def cracker():
    print("[SYSTEM] AES-GCM Password Cracker Initialized")

    enc_file = input("Enter the path to the encrypted file: ").strip()
    if not os.path.isfile(enc_file):
        print(f"[ERROR] File not found: {enc_file}")
        return

    password_dir = os.path.join("src", "ai", "GeneratedPasswords")
    if not os.path.isdir(password_dir):
        print(f"[ERROR] Password directory not found: {password_dir}")
        return

    password_files = sorted([
        f for f in os.listdir(password_dir)
        if f.startswith("password") and f.endswith(".txt")
    ])

    if not password_files:
        print("[ERROR] No password files found.")
        return

    print("\nAvailable password lists:")
    for idx, fname in enumerate(password_files, 1):
        print(f"{idx}. {fname}")

    try:
        choice = int(input("Select a password list by number: ").strip())
        if choice < 1 or choice > len(password_files):
            print("[ERROR] Invalid selection.")
            return
    except ValueError:
        print("[ERROR] Please enter a valid number.")
        return

    selected_wordlist = os.path.join(password_dir, password_files[choice - 1])
    output_base = os.path.splitext(enc_file)[0] + "_decrypted"  # No extension yet

    with open(enc_file, 'rb') as f:
        data = f.read()

    if len(data) < 48:
        print("[ERROR] Encrypted file is too short or malformed.")
        return

    salt = data[:16]
    nonce = data[16:32]
    tag = data[32:48]
    ciphertext = data[48:]

    with open(selected_wordlist, 'r', encoding='utf-8') as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(f"\n[INFO] Trying {len(passwords)} passwords from: {password_files[choice - 1]}")

    for i, pwd in enumerate(passwords, 1):
        key = PBKDF2(pwd, salt, dkLen=32)
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

        try:
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            
            file_extension = detect_file_type(plaintext)
            output_file = output_base + file_extension  
            
            with open(output_file, 'wb') as out_file:
                out_file.write(plaintext)
            print(f"\n[✓] Password found: {pwd}")
            print(f"[INFO] Detected file type: {file_extension}")
            print(f"[✓] Decrypted file saved as: {output_file}")
            return pwd
        except Exception:
            if i % 50 == 0 or i == len(passwords):
                print(f"[INFO] Tried {i}/{len(passwords)} passwords...")

    print("\n[-] Password not found in list.")
    return None