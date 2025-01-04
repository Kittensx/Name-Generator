
import os
import shutil
import subprocess
import zipfile
import requests

GITHUB_REPO_URL = "https://github.com/Kittensx/Name-Generator/raw/refs/heads/main/name_files.zip"

REQUIRED_FOLDERS = ["boys", "girls", "last_name"]

def check_and_download_folders(install_dir):
    missing_folders = [folder for folder in REQUIRED_FOLDERS if not os.path.exists(os.path.join(install_dir, folder))]
    
    if not missing_folders:
        print("All required folders are present.")
        return True

    print("Missing folders detected:", ", ".join(missing_folders))
    print("Attempting to download missing folders from GitHub...")
    
    try:
        zip_path = os.path.join(install_dir, "name_files.zip")
        
        # Download the zip file using requests
        response = requests.get(GITHUB_REPO_URL, stream=True)
        response.raise_for_status()  # Raise an error for bad status codes
        
        with open(zip_path, "wb") as zip_file:
            for chunk in response.iter_content(chunk_size=8192):
                zip_file.write(chunk)
        
        # Check if the downloaded file is a valid zip file
        if not zipfile.is_zipfile(zip_path):
            raise ValueError("Downloaded file is not a valid zip file.")
        
        # Extract the zip file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(install_dir)
        
        # Clean up
        os.remove(zip_path)
        print("Folders downloaded and set up successfully.")
        return True
    
    except Exception as e:
        print("Error occurred while downloading or setting up folders.")
        print("Error details:", str(e))
        print("Please ensure you have an active internet connection and try again.")
        return False

        
def main():
    print("Welcome to the Name Generator Installer!")
    
    install_dir = os.getcwd()
    print(f"Installing in the current directory: {install_dir}")
    
    if not check_and_download_folders(install_dir):
        print("Installation failed due to missing folders.")
        return
        
    
    print("Installation completed successfully! You can run the program using 'run_namegen.bat'.")

if __name__ == "__main__":
    main()
