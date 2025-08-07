    `import os

FILENAME = "todo.txt"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("📭 No tasks in your to-do list.")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks):
            print(f"{idx + 1}. {task}")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append("[ ] " + task)
            save_tasks(tasks)
            print("✅ Task added.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= index < len(tasks):
                    if "[x]" not in tasks[index]:
                        tasks[index] = tasks[index].replace("[ ]", "[x]")
                        save_tasks(tasks)
                        print("✅ Task marked as completed.")
                    else:
                        print("⚠️ Task is already completed.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            show_tasks(tasks)
            try:
                index = int(input("Enter task number to delete: ")) - 1
                if 0 <= index < len(tasks):
                    removed = tasks.pop(index)
                    save_tasks(tasks)
                    print(f"🗑️ Removed: {removed}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "5":
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
