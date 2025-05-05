# 📘 UMBRA Usage Guide

Welcome to the UMBRA Usage Guide. This document will walk you through the steps to effectively utilize the UMBRA tool for password list generation and security enhancement.

## Prerequisites

Before using UMBRA, ensure you have the following prerequisites:

- Python 3 installed
- Necessary dependencies listed in `requirements.txt`

## Installation

To install UMBRA, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Abdul-Rahman-Ammourah/UMBRA.git
   ```
2. Navigate to the UMBRA directory:
   ```bash
   cd UMBRA
   ```
3. Make the script executable:
   ```bash
   chmod +x umbra.sh
   ```
4. Run the setup script:
   ```bash
   ./umbra.sh
   ```

## Running UMBRA

UMBRA can be run in both interactive and graphical modes.

### Interactive Mode

1. Launch UMBRA in interactive mode:
   ```bash
   python src/main.py
   ```
2. You will be presented with a prompt. Enter one of the following commands:

   - `generate` or `gen` or `g`: Create a password list using user inputs.
   - `gui`: Launch the graphical user interface.
   - `suggest` or `s`: Get secure password suggestions.
   - `exit`: Quit the program.

### Graphical User Interface (GUI)

1. To launch the GUI directly, run:
   ```bash
   python src/main.py
   ```
2. At the prompt, type `gui` and press Enter.
3. Use the GUI for targeted password generation and suggestions.

## Use Cases

- **Penetration Testing**: Generate smarter password lists for ethical hacking and security assessments.
- **Cybersecurity Awareness**: Demonstrate how easily weak passwords can be guessed.
- **Personal Security**: Assist users in strengthening their password habits.

## Disclaimer

UMBRA is intended for educational and ethical cybersecurity purposes only. Misuse of this tool for unauthorized access or malicious activities is strictly prohibited.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

For more information, visit our [GitHub repository](https://github.com/Abdul-Rahman-Ammourah/UMBRA).
