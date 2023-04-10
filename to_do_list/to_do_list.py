# create the task list
tasks = []

# function to view tasks
def view_tasks():
    print("Task list: ")
    order = 1
    for task in tasks:
        print(f"{order}) {task}")
        order += 1
    print()

# function to add task to the list
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")
    print()

# create a function that deletes tasks
def delete_task():
    view_tasks()
    task = int(input("Enter task to delete (number): "))

    if task <= len(tasks) and task >= 1:
        tasks.remove(tasks[task - 1])
        print("Task deleted successfully.")
    else:
        print("Task not found.")
    print()
    
# function to show the menu
def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. Delete task")
    print("3. View tasks")
    print("4. Quit")
    print()

# display the menu and handle user input
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
    print()