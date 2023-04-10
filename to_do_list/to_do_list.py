# create the task list
tasks = []

# function to add task to the list
def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully.")

# create a function that deletes tasks
def delete_task():
    task = input("Enter task to delete: ")

    if task in tasks:
        tasks.remove(task)
        print("Task deleted successfully.")
    else:
        print("Task not found.")

# function to view tasks
def view_tasks():
    print("Task list: ")
    order = 1
    for task in tasks:
        print(f"{order}. {task}")
        order += 1



add_task()
delete_task()
view_tasks()
tasks