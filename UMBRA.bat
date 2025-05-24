@echo off
setlocal

:: Variables
set "VENV_DIR=venv"
set "REQUIREMENTS_FILE=requirements.txt"
set "MAIN_PY=src\main.py"

:: Check if Python is installed
where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3 and try again.
    echo To install Python, visit https://www.python.org/downloads/
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv %VENV_DIR%

:: Activate virtual environment
echo Activating virtual environment...
call %VENV_DIR%\Scripts\activate.bat

:: Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: Install dependencies
if exist "%REQUIREMENTS_FILE%" (
    echo Installing dependencies from %REQUIREMENTS_FILE%...
    pip install -r %REQUIREMENTS_FILE%
) else (
    echo Error: %REQUIREMENTS_FILE% not found.
    echo Please ensure the requirements file is present in the current directory.
    exit /b 1
)

:: Run main.py
if exist "%MAIN_PY%" (
    echo Running main.py...
    python %MAIN_PY%
) else (
    echo Error: %MAIN_PY% not found.
    echo Please ensure the main.py file is present in the src directory.
    exit /b 1
)

endlocal
