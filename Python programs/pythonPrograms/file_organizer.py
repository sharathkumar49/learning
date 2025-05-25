# File Organizer (sort files in folders by type)
import os
import shutil

def organize(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            ext = filename.split('.')[-1]
            folder = os.path.join(directory, ext.upper() + '_Files')
            os.makedirs(folder, exist_ok=True)
            shutil.move(os.path.join(directory, filename), os.path.join(folder, filename))

if __name__ == "__main__":
    path = input("Enter directory to organize: ")
    organize(path)
    print("Files organized by type.")
