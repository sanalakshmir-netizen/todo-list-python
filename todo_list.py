import tkinter as tk
from tkinter import messagebox


def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)


def delete_task():
    selected_task = task_listbox.curselection()

    if not selected_task:
        messagebox.showwarning("Warning", "Please select a task.")
        return

    task_listbox.delete(selected_task)


def clear_tasks():
    if task_listbox.size() == 0:
        return

    confirm = messagebox.askyesno(
        "Clear Tasks",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:
        task_listbox.delete(0, tk.END)


# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

# Title
title_label = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=20)

# Task input
task_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 12)
)
task_entry.pack(pady=10)

# Add button
add_button = tk.Button(
    root,
    text="Add Task",
    width=15,
    command=add_task
)
add_button.pack(pady=5)

# Task list
task_listbox = tk.Listbox(
    root,
    width=40,
    height=15,
    font=("Arial", 12)
)
task_listbox.pack(pady=15)

# Delete button
delete_button = tk.Button(
    root,
    text="Delete Selected",
    width=15,
    command=delete_task
)
delete_button.pack(pady=5)

# Clear button
clear_button = tk.Button(
    root,
    text="Clear All",
    width=15,
    command=clear_tasks
)
clear_button.pack(pady=5)

# Start application
root.mainloop()