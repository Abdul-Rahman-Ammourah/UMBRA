import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
#from GUI.umbra_gui import UMRBAMainWindow
from GUI.ui.main_window import UMRBAMainWindow
from password_gen.password_gen import generate_password_list
from password_sug.password_sug import suggest_password_list
from Cracker.Decrypter import cracker
def print_logo():
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
    generate_password_list()
    
def suggest_password():
    suggest_password_list()
def launch_gui():
    print("[SYSTEM] Launching GUI...")
    app = QApplication(sys.argv)
    window = UMRBAMainWindow()

    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()
    window.raise_()
    window.activateWindow()

    window.show()

    sys.exit(app.exec_())
def interactive_mode():
    while True:
        command = input("\n[UMBRA] >> ").strip().lower()
        
        if command == "generate" or command == "gen" or command == "g":
            generate_password()
        elif command == "gui" or command == "menu" or command == "m":
            launch_gui()
        elif command == "suggest" or command == "s" or command == "sug":
            suggest_password()
        elif command == "exit" or command == "quit" or command == "q" or command == "e" or command == "x":
            print("[SYSTEM] Exiting UMBRA. Stay safe!")
        elif command == "cracker" or command == "crack" or command == "c":
            cracker()
            break
        else:
            print("[ERROR] Unknown command. Type 'gui', 'generate', 'suggest', or 'exit'.")

if __name__ == "__main__":
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
