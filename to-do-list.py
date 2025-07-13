
class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = False
            print(f'Task "{task}" added.')
        else:
            print(f'Task "{task}" already exists.')

    def update_task(self, task, completed):
        if task in self.tasks:
            self.tasks[task] = completed
            status = 'completed' if completed else 'not completed'
            print(f'Task "{task}" marked as {status}.')
        else:
            print(f'Task "{task}" does not exist.')

    def view_tasks(self):
        print("\nYour To-Do List:")
        for task, completed in self.tasks.items():
            status = '✔️' if completed else '❌'
            print(f"{task}: {status}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task you want to update: ")
            completed = input("Is the task completed? (yes/no): ").lower() == 'yes'
            todo_list.update_task(task, completed)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

