class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        self.tasks[task_name] = {"description": task_description, "status": "pending"}
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task_name, task_details in self.tasks.items():
                print(f"Task Name: {task_name}")
                print(f"Description: {task_details['description']}")
                print(f"Status: {task_details['status']}\n")

    def update_task(self):
        task_name = input("Enter task name to update: ")
        if task_name in self.tasks:
            task_details = self.tasks[task_name]
            print("Enter new details (press Enter to skip):")
            task_details["description"] = input(f"Description ({task_details['description']}): ") or task_details["description"]
            task_details["status"] = input(f"Status ({task_details['status']}): ") or task_details["status"]
            self.tasks[task_name] = task_details
            print("Task updated successfully!")
        else:
            print("Task not found.")

    def delete_task(self):
        task_name = input("Enter task name to delete: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print("Task deleted successfully!")
        else:
            print("Task not found.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("-------------------------------")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
