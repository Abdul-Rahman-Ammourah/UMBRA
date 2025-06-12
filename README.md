# UMBRA - AI Password Generator and Suggestion Tool  

## 🛠 About  

**UMBRA** is an open-source command-line tool designed to enhance password security assessments using. Instead of relying on brute force or generic dictionary attacks, UMBRA takes personal data to generate **highly targeted password lists**, improving efficiency in penetration testing and cybersecurity audits.  

## 🚀 Features  

- 🤖 **AI-Assisted Password Generation** – Uses intelligent techniques to create realistic password variations.  
- 🔐 **Secure Password Suggestions** – Helps users create strong yet memorable passwords.  
- ⚡ **Lightweight & Efficient** – Designed to be fast and resource-friendly on Linux/Windows systems.  
## 📦 Dependencies  

UMBRA requires the following Python packages:

- `flask-cors>=5.0.1` – For handling CORS in Flask-based APIs.

- `PyQt5>=5.15.11` – For optional GUI functionality.

- `requests>=2.32.3` – For making HTTP requests.

- `sphinx>=7.2.6` – For generating project documentation.
- `sphinxcontrib-mermaid>=0.9.0` – To integrate Mermaid diagrams in docs.

📥 To install all required packages:
```bash
pip install -r requirements.txt
```


## 🔧 Installation  

### 🐧Linux
```bash
git clone https://github.com/Abdul-Rahman-Ammourah/UMBRA.git
cd UMBRA
chmod +x umbra.sh
./umbra.sh
```
### 👨‍💻Windows
```
git clone https://github.com/Abdul-Rahman-Ammourah/UMBRA.git
cd UMBRA
umbra.bat
```

### 🤖Model Installation

- Download the model from [here](https://drive.google.com/drive/folders/12fkda0zmt8-euxRu2EeF_Sor9vpnE401?usp=sharing).
- Place the model in the `backend` directory.

## 📌 Use Cases
- 🛡️ Penetration Testing – Generate smarter password lists for ethical hacking and security assessments.
- 📢 Cybersecurity Awareness – Demonstrate how easily weak passwords can be guessed.
- 🔑 Personal Security – Assist users in strengthening their password habits.

## ⚠️ Disclaimer
UMBRA is intended for educational and ethical cybersecurity purposes only. Misuse of this tool for unauthorized access or malicious activities is strictly prohibited.

## 📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
