
@echo off
REM Navigate to the directory where the bat file is located
cd /d "%~dp0"

REM Run the installer script using Python
python namegen.py
