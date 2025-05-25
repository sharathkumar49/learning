# JSON Data Manipulation (Read/Write/Update)
import json
import os

FILENAME = 'data.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    data = load_data()
    while True:
        print("1. View 2. Add/Update 3. Delete 4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            print(json.dumps(data, indent=2))
        elif choice == '2':
            key = input("Key: ")
            value = input("Value: ")
            data[key] = value
            save_data(data)
        elif choice == '3':
            key = input("Key to delete: ")
            if key in data:
                del data[key]
                save_data(data)
        elif choice == '4':
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
