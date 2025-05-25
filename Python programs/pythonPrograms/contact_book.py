# Contact Book (CRUD operations, file-based)
import json
import os

FILENAME = 'contacts.json'

def load_contacts():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as f:
        return json.load(f)

def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("Contact added.")

def view_contacts(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def delete_contact(contacts):
    name = input("Name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Deleted.")
    else:
        print("Not found.")

def main():
    contacts = load_contacts()
    while True:
        print("1. Add 2. View 3. Delete 4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
