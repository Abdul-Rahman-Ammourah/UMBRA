import sys
from PyQt5.QtWidgets import QApplication
from GUI.umbra_gui import UMRBAMainWindow
from password_gen.password_gen import generate_password_list
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
    print("[SYSTEM] Suggesting a secure password...")
    #password_suggestor()
def launch_gui():
    print("[SYSTEM] Launching GUI...")
    app = QApplication(sys.argv)
    window = UMRBAMainWindow()
    window.show()
    sys.exit(app.exec_())
def interactive_mode():
    print("[SYSTEM] UMBRA Interactive Mode Activated.")
    while True:
        command = input("\n[UMBRA] >> ").strip().lower()
        
        if command == "generate":
            generate_password()
        elif command == "gui":
            launch_gui()
        elif command == "suggest":
            suggest_password()
        elif command == "exit":
            print("[SYSTEM] Exiting UMBRA. Stay safe!")
            break
        else:
            print("[ERROR] Unknown command. Type 'generate', 'suggest', or 'exit'.")

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
          "Type 'exit' to quit the program.\n")

    interactive_mode()
