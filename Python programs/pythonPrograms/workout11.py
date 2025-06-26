import os
import shutil

companies = ['amazon', 'google', 'microsoft', 'meta', 'apple','walmart', 'turing', 'facebook', 'tesla', 'netflix', 'adobe', 'nvidia', 'ibm', 'oracle', 'salesforce', 'twitter', 'snapchat', 'spotify']
current_dir = os.getcwd()
# print(current_dir)
files = [f for f in os.listdir(current_dir) if os.path.isfile(f)]

for file_name in files:
    for company in companies:
        if company.lower() in file_name.lower():
            dest_folder = company.capitalize()
            dest_path = os.path.join(current_dir, dest_folder)
            
            # Create destination folder only if it doesn't exist
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
                print(f"Created folder '{dest_folder}'.")

            shutil.copy2(file_name, dest_path)
            os.remove(file_name)
            print(f"Moved and deleted '{file_name}' to '{dest_folder}' folder.")
            break
