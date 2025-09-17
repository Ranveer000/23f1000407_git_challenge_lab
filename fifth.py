tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

add_task("Learn Python")
add_task("Practice Git")
add_task("Complete assignments")

show_tasks()
