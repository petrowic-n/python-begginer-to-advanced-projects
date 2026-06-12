# Store tasks
tasks = []

# Show Menu
def show_menu():
    print("************************")
    print("1) Add task")
    print("2) View tasks")
    print("3) Mark done")
    print("4) Quit")
    print("************************")

# Add Task
def add_task():
    text = input("Enter task: ")
    tasks.append({"text": text, "done": False})
    print(f"Added: {text}")

# View Task
def view_task():
    if not tasks:
        print("No tasks added!")
        return
    print("\nYour tasks: ")
    for i, task in enumerate(tasks, 1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{i}. {status} {task['text']}")

# Mark Done
def mark_done():
    view_task()
    if not tasks:
        return
    try:
        num = int(input("Choose task to mark as done? ")) - 1
        tasks[num]["done"] = True
        print("Marked as done")
    except(ValueError, IndexError):
        print("Invalid number, try again.")


while True:
    show_menu()
    user_input = input("Choose action (1-4): ")

    if not user_input.isdigit():
        print("Please enter a number between  (1-4)")
    
    if user_input == "1":
        add_task()
    elif user_input == "2":
        view_task()
    elif user_input == "3":
        mark_done()
    elif user_input == "4":
        quit()

    



# Loop the user until Quits

# Mark task done by number