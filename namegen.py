import random
import os

# Directories containing name files
BOYS_FOLDER = "boys"
GIRLS_FOLDER = "girls"
LAST_NAMES_FOLDER = "last_name"
NAME_FILE="used_names.txt"

# Function to load all names from files in a folder
def load_names_from_folder(folder):
    names = []
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                names.extend(file.read().splitlines())
    return names

# Load names into memory
male_first_names = load_names_from_folder(BOYS_FOLDER)
female_first_names = load_names_from_folder(GIRLS_FOLDER)
male_middle_names = load_names_from_folder(BOYS_FOLDER)  # Reuse boys folder for male middle names
female_middle_names = load_names_from_folder(GIRLS_FOLDER)  # Reuse girls folder for female middle names
last_names = load_names_from_folder(LAST_NAMES_FOLDER)

# Function to generate a name based on sex
def generate_name(sex):
    if sex.lower() in ["male", "m", "boy", "man", "b"]:
        first_name = random.choice(male_first_names)
        middle_name = random.choice(male_middle_names)
    elif sex.lower()  in ["female", "f", "girl", "g", "woman"]:
        first_name = random.choice(female_first_names)
        middle_name = random.choice(female_middle_names)
    else:
        return None

    last_name = random.choice(last_names)
    return f"{first_name} {middle_name} {last_name}"

# Function to load used names from file
def load_used_names():
    if os.path.exists(NAME_FILE):
        with open(NAME_FILE, "r") as file:
            return set(file.read().splitlines())
    return set()

# Function to save a name to the file
def save_name(name):
    with open(NAME_FILE, "a") as file:
        file.write(name + "\n")

# Main program
def main():
    used_names = load_used_names()
    print("Welcome to the Name Generator!")

    while True:
        action = input("Enter 'g' to generate a name, 'q' to quit: ").strip().lower()

        if action == "g":
            sex = input("Enter sex (male/female): ").strip().lower()
            name = generate_name(sex)

            if not name:
                print("Invalid sex. Please try again.")
                continue

            if name in used_names:
                print("Generated name already used. Trying again...")
                continue

            print(f"Generated Name: {name}")
            used_names.add(name)
            save_name(name)

        elif action == "q":
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
