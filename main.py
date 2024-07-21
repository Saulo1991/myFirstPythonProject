def add_task(tasks, task):
    tasks.append(task)

def list_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task(tasks, task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found")

tasks = []
while True:
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        task = input("Enter task to add: ")
        add_task(tasks, task)
    elif choice == '2':
        list_tasks(tasks)
    elif choice == '3':
        task = input("Enter task to remove: ")
        remove_task(tasks, task)
    elif choice == '4':
        break
    else:
        print("Invalid option, please choose again.")
