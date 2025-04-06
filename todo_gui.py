import tkinter as tk
from tkinter import messagebox, simpledialog
import os

TASK_FILE = "tasks.txt"
TRASH_FILE = "trash.txt"

# ----- File I/O -----
def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        f.write("\n".join(tasks))

def append_to_trash(tasks):
    with open(TRASH_FILE, "a") as f:
        for task in tasks:
            f.write(task + "\n")

def undo_last():
    if not os.path.exists(TRASH_FILE):
        return None

    with open(TRASH_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        return None

    last_task = lines[-1].strip()
    with open(TRASH_FILE, "w") as f:
        f.writelines(lines[:-1])
    return last_task

# ----- GUI -----
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do CLI GUI")
        self.tasks = load_tasks()

        # Entry
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Buttons
        tk.Button(root, text="Add Task", command=self.add_task).pack()
        tk.Button(root, text="Mark as Done", command=self.mark_done).pack()
        tk.Button(root, text="Undo", command=self.undo_task).pack(pady=5)

        # Listbox
        self.task_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50)
        self.task_listbox.pack(pady=10)
        self.refresh_listbox()

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)
            self.refresh_listbox()
            self.entry.delete(0, tk.END)

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select at least one task.")
            return

        done_tasks = [self.tasks[i] for i in selected]
        for i in reversed(selected):
            del self.tasks[i]

        save_tasks(self.tasks)
        append_to_trash(done_tasks)
        self.refresh_listbox()

    def undo_task(self):
        task = undo_last()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)
            self.refresh_listbox()
        else:
            messagebox.showinfo("Nothing to Undo", "No tasks in trash.")

# Run it
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

