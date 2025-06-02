import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def detect_file_type(data: bytes) -> str:
    signatures = {
        b'\x50\x4B\x03\x04': '.xlsx',
        b'\x25\x50\x44\x46': '.pdf',
        b'\x89\x50\x4E\x47': '.png',
        b'\xFF\xD8\xFF': '.jpg',
        b'\x42\x4D': '.bmp',
        b'\x7F\x45\x4C\x46': '.elf',
        b'\x52\x61\x72\x21\x1A\x07\x00': '.rar',
    }
    for magic, extension in signatures.items():
        if data.startswith(magic):
            return extension
    return '.txt' # Default to .txt if no signature matches