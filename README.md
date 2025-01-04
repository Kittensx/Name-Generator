# Name-Generator
A simple CLI (command line interface) to generate first, middle, and last names

# Name Generator Program

## Overview
The Name Generator program is a simple Python-based tool that generates random names using predefined lists of first names (male and female) and last names. The program allows users to generate names based on gender and keeps track of previously used names to prevent duplicates during a session.

### Features:
- Generates names based on user-input gender.
- Supports male and female first and middle names.
- Tracks previously used names to avoid repetition.
- Allows users to save generated names to a file (`used_names.txt`).

## How It Works
The program reads names from three directories:
1. `boys`: Contains files with male first and middle names.
2. `girls`: Contains files with female first and middle names.
3. `last_name`: Contains files with last names.

When the program starts, it loads all the names from these directories into memory. The user can then input a gender, and the program will randomly select a first, middle, and last name from the appropriate lists.

### Usage Instructions:
1. **Run the Program**: Once installed, run the program by executing `run_namegen.bat`.
2. **Generate a Name**: Enter 'g' to generate a new name, and specify the gender (male or female).
   a. To select a male name, enter any of the following: "male", "m", "boy", "man", "b"
   b. To select a female name, enter any of the following: "female", "f", "girl", "g", "woman"
4. **Quit the Program**: Enter 'q' to quit the program.

---

# Installation Guide

## Prerequisites
- Python 3.x must be installed on your system.
- An internet connection is required for downloading necessary files during installation.

## Requirements
- Requirements.txt: this program was installed and tested with requests==2.31.0. If your version of requests does not work, please try updating to at least this version. 
- pip install requests or pip install -r requirements.txt

## Installation Steps
1. **Download the Files**:
   - Clone or download the repository containing the program files from [GitHub](https://github.com/Kittensx/Name-Generator).
2. **Run the Installer**:
   - Double-click `run_install_namegen.bat` to start the installation process.
   - The installer will:
     - Check for the required directories (`boys`, `girls`, and `last_name`).
     - Download `name_files.zip` from GitHub if the directories are missing.
     - Extract the ZIP file and set up the directories.
3. **Run the Program**:
   - Once the installation is complete, double-click `run_namegen.bat` to launch the Name Generator program.

## Troubleshooting
- **Missing Directories**: If the required directories (`boys`, `girls`, `last_name`) are missing, ensure that `name_files.zip` is correctly downloaded and extracted.
- **Internet Connection Issues**: If the installer fails to download `name_files.zip`, check your internet connection and try running the installer again.
- **Python Not Installed**: Ensure Python 3.x is installed and added to your system's PATH.

For more information, visit the [GitHub Repository](https://github.com/Kittensx/Name-Generator).

---

This README provides details on how to use the Name Generator program and the installation process. If you encounter any issues, please refer to the Troubleshooting section or reach out via the GitHub repository.

