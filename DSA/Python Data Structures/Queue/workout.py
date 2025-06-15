import os

# Get all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Print the file names
for file in files:
    print(file)
