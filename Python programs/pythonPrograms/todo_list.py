# Basic To-Do List (file or in-memory)
FILENAME = 'todo.txt'

def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        for task in tasks:
            f.write(task + '\n')

def main():
    tasks = load_tasks()
    while True:
        print("1. View 2. Add 3. Remove 4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        elif choice == '2':
            task = input("Task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == '3':
            idx = int(input("Task number to remove: ")) - 1
            if 0 <= idx < len(tasks):
                tasks.pop(idx)
                save_tasks(tasks)
        elif choice == '4':
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
