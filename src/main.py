"""UMBRA - Password Security Tool Main Module.

This module serves as the central hub for all UMBRA functionality,
providing both command-line interface and GUI access to password
generation, suggestion, and cracking tools.
"""

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from GUI.ui.main_window import UMRBAMainWindow
from password_gen.password_gen import generate_password_list
from password_sug.password_sug import suggest_password_list
from Cracker.Decrypter import cracker


def print_logo():
    """Display the UMBRA ASCII art logo in the console.
    
    Example:
        >>> print_logo()
        ██    ██ ███    ███ ██████  ██████   █████  
        ██    ██ ████  ████ ██   ██ ██   ██ ██   ██ 
        ...
    """
    logo = r"""
██    ██ ███    ███ ██████  ██████   █████  
██    ██ ████  ████ ██   ██ ██   ██ ██   ██ 
██    ██ ██ ████ ██ ██████  ██████  ███████ 
██    ██ ██  ██  ██ ██      ██   ██ ██   ██ 
 ██████  ██      ██ ██      ██   ██ ██   ██ 
                                            
       UMBRA - Password Security Tool
    """
    print(logo)


def generate_password():
    """Generate a list of secure passwords.
    
    This function invokes the password generation module to create
    a list of cryptographically secure passwords.
    
    See Also:
        :mod:`password_gen.password_gen` - The underlying password generator
    """
    generate_password_list()
    

def suggest_password():
    """Suggest a secure password based on best practices.
    
    This function provides password suggestions following current
    security recommendations.
    """
    suggest_password_list()


def launch_gui():
    """Launch the UMBRA graphical user interface.
    
    Initializes and displays the main PyQt5 application window with
    all password management functionality.
    
    Note:
        The window is set to stay on top of other windows by default.
    """
    print("[SYSTEM] Launching GUI...")
    app = QApplication(sys.argv)
    window = UMRBAMainWindow()

    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()
    window.raise_()
    window.activateWindow()
    sys.exit(app.exec_())


def interactive_mode():
    """Handle the command-line interactive mode.
    
    Provides a text-based menu system for accessing all UMBRA functions.
    Available commands:
    
    - generate/gen/g: Generate passwords
    - gui/menu/m: Launch GUI
    - suggest/s/sug: Get password suggestions
    - cracker/crack/c: Run password cracker
    - exit/quit/q/e/x: Quit the program
    """
    while True:
        command = input("\n[UMBRA] >> ").strip().lower()
        
        if command in ("generate", "gen", "g"):
            generate_password()
        elif command in ("gui", "menu", "m"):
            launch_gui()
        elif command in ("suggest", "s", "sug"):
            suggest_password()
        elif command in ("exit", "quit", "q", "e", "x"):
            print("[SYSTEM] Exiting UMBRA. Stay safe!")
            break
        elif command in ("cracker", "crack", "c"):
            cracker()
            break
        else:
            print("[ERROR] Unknown command. Type 'gui', 'generate', 'suggest', or 'exit'.")


if __name__ == "__main__":
    """Main entry point for the UMBRA Password Security Tool."""
    print_logo()
    print("UMBRA Terminal v1.0\n"
          "Copyright (c) 2025 UMBRA Systems\n\n"
          "[SYSTEM] Initializing password systems...\n"
          "[SYSTEM] Establishing secure environment...\n"
          "[SYSTEM] All systems operational.\n\n"
          "Type 'gui' to launch the GUI.\n"
          "Type 'generate' to create a password list.\n"
          "Type 'suggest' to get a secure password.\n"
          "Type 'cracker' to crack an encrypted file.\n"
          "Type 'exit' to quit the program.\n")

    interactive_mode()