#!/bin/bash

# Exit on error
set -e

# Variables
VENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
MAIN_PY="src/main.py"

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 and try again."
    echo "To install Python 3, run: sudo apt-get install python3"
    exit 1
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv "$VENV_DIR"

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_DIR/bin/activate"

# Upgrade pip and install dependencies
echo "Upgrading pip and installing dependencies..."
pip install --upgrade pip
pip install -r "$REQUIREMENTS_FILE"

# Run main.py
echo "Running main.py..."
python "$MAIN_PY"
