# Loading existing items
# 1. create a new item
# 2. list items
# 3. mark item as complete
# 4. save items
import json

{"tasks": [
    {"tasks": "tasks is this", "complete": True}
]}

file_name = "todo_list.json"

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except:
        return {"tasks": []}


def ssave_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            json.dump(tasks,file)
    except:
        print("Filed to save.")
    

def view_tasks(tasks):
    print()
    task_list = tasks["tasks"]
    if len(task_list) == 0:
        print("No tasks to display.")
    else:
        print("Your To-Do List: ")
        for index, task in enumerate(task_list):
            status = "[Completed]" if task["complete"] else "[Pending]"
            print(f"{index + 1}. {task['description']}    {status}")


def create_tasks(tasks):
    discription = input("Enter the task discription: ").strip()
    if discription:
        tasks["tasks"].append({"discription": discription, "complete": False})
        ssave_tasks(tasks)
        print("Task added.")
    else:
        print("Description cannot be empty.")


def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: ").strip())
        if 1 <= task_number <= len(tasks):
            tasks["tasks"][task_number - 1]["complete"] = True
            ssave_tasks(tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except:
        print("Enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            create_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            print("Goodbye")
        else:
            print("Invalid choice. Please try again.")

main()
