import json
import os

TASKS_FILE = "tasks.json" # File to store tasks

# Load tasks from file or initialize empty list
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Display tasks
def display_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task description: ")
    tasks.append({"task": task_name, "completed": False})
    print("Task added successfully!")

# Update a task
def update_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter the task number to update: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["task"] = input("Enter the new description: ")
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Mark task as completed
def mark_completed(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted_task = tasks.pop(task_no - 1)
                print(f"Deleted task: {deleted_task['task']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main function
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        try:
            choice = int(input("Enter your choice (1-6): "))
            if choice == 1:
                display_tasks(tasks)
            elif choice == 2:
                add_task(tasks)
            elif choice == 3:
                update_task(tasks)
            elif choice == 4:
                mark_completed(tasks)
            elif choice == 5:
                delete_task(tasks)
            elif choice == 6:
                save_tasks(tasks)
                print("Goodbye!")
                break
            else:
                print("Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
