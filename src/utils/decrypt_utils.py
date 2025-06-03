"""File Type Detection Utilities.

Provides functionality to identify file types from binary signatures.
"""

def detect_file_type(data: bytes) -> str:
    """Detect file type from binary magic numbers.
    
    Args:
        data: First few bytes of the file (minimum 8 bytes recommended)
        
    Returns:
        str: File extension with leading dot (e.g. '.pdf')
        
    Example:
        >>> with open('document.pdf', 'rb') as f:
        ...     detect_file_type(f.read(8))
        '.pdf'
        
    Note:
        Requires minimum bytes:
        - 4 bytes for most formats
        - 7 bytes for RAR files
    """
    signatures = {
        b'\x50\x4B\x03\x04': '.xlsx',  # ZIP-based formats
        b'\x25\x50\x44\x46': '.pdf',   # PDF
        b'\x89\x50\x4E\x47': '.png',   # PNG
        b'\xFF\xD8\xFF': '.jpg',       # JPEG
        b'\x42\x4D': '.bmp',           # BMP
        b'\x7F\x45\x4C\x46': '.elf',   # Executable
        b'\x52\x61\x72\x21\x1A\x07\x00': '.rar',  # RAR archive
    }
    for magic, extension in signatures.items():
        if data.startswith(magic):
            return extension
    return '.txt'  # Default fallback