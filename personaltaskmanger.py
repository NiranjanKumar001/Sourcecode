import os

# File to store tasks
TASK_FILE = "tasks.txt"

# Function to load tasks from the file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to add a new task
def add_task(tasks):
    new_task = input("Enter the new task: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Task '{new_task}' added successfully!")
    else:
        print("Task cannot be empty.")

# Function to view all tasks
def view_tasks(tasks):
    if tasks:
        print("\nCurrent Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nNo tasks available.")

# Function to update a task
def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(tasks):
                updated_task = input("Enter the updated task: ").strip()
                if updated_task:
                    tasks[task_number - 1] = updated_task
                    save_tasks(tasks)
                    print(f"Task {task_number} updated to '{updated_task}'!")
                else:
                    print("Updated task cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                save_tasks(tasks)
                print(f"Task '{deleted_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to delete all tasks
def delete_all_tasks(tasks):
    confirm = input("Are you sure you want to delete all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks deleted successfully!")
    else:
        print("Operation cancelled.")

# Function to display the menu
def show_menu():
    print("\nPersonal Task Manager")
    print("----------------------")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Delete All Tasks")
    print("6. Exit")

# Main program loop
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            delete_all_tasks(tasks)
        elif choice == "6":
            print("Exiting Personal Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main()
