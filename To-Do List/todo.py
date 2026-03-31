def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added.")


def remove_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        print(f"Removed: {removed}")
    except:
        print("Invalid input")


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f]
    except:
        return []


def main():
    tasks = load_tasks()

    while True:
        print("\n1. View  2. Add  3. Remove  4. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice")


main()
