import sys
import os

TASK_FILE = "tasks.txt"
TRASH_FILE = "trash.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.write("\n".join(tasks))

# Show help message
def show_help():
    print("""
To-Do CLI Tool Commands:
  add <task>           → Add a new task
  list                 → List all tasks
  done <n> <m> ...     → Mark one or more tasks as done
  done 1,2,3           → Also works
  undo                 → Undo the last completed task
""")

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {task}")

# List current tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

# Complete (and remove) one or more tasks
def complete_tasks(indices):
    tasks = load_tasks()
    trash = []

    try:
        indices = sorted(set(int(i) for i in indices), reverse=True)
        for i in indices:
            if 0 < i <= len(tasks):
                removed = tasks.pop(i - 1)
                trash.append(removed)
                print(f"Completed task: {removed}")
            else:
                print(f"Invalid task number: {i}")
        save_tasks(tasks)
        with open(TRASH_FILE, "a") as f:
            for item in reversed(trash):
                f.write(item + "\n")
    except ValueError:
        print("Please enter valid task numbers.")

# Undo the last removed task
def undo():
    if not os.path.exists(TRASH_FILE):
        print("No tasks to undo.")
        return

    with open(TRASH_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        print("Trash is empty.")
        return

    last_task = lines[-1].strip()
    tasks = load_tasks()
    tasks.append(last_task)
    save_tasks(tasks)

    with open(TRASH_FILE, "w") as f:
        f.writelines(lines[:-1])

    print(f"Restored task: {last_task}")

# Entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1]
        if command == "add":
            add_task(" ".join(sys.argv[2:]))
        elif command == "list":
            list_tasks()
        elif command == "done":
            if len(sys.argv) > 2:
                raw_input = " ".join(sys.argv[2:]).replace(",", " ")
                indices = raw_input.split()
                complete_tasks(indices)
            else:
                print("Please specify one or more task numbers to complete.")
        elif command == "undo":
            undo()
        else:
            show_help()

