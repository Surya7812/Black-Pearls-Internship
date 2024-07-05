import tkinter as tk
from tkinter import messagebox, ttk
import json
from datetime import datetime

class Task:
    def __init__(self, title, description='', priority=1, completed=False, due_date=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = completed
        self.due_date = due_date

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            tasks_data = [{'title': task.title, 'description': task.description,
                           'priority': task.priority, 'completed': task.completed,
                           'due_date': task.due_date} for task in self.tasks]
            json.dump(tasks_data, f, indent=4)

    def add_task(self, title, description='', priority=1, due_date=None):
        new_task = Task(title, description, priority, False, due_date)
        self.tasks.append(new_task)
        self.save_tasks()
        self.update_task_listbox()

    def delete_task(self, index):
        try:
            del self.tasks[index]
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Invalid task index!")

    def update_task(self, index, title=None, description=None, priority=None, due_date=None):
        try:
            task = self.tasks[index]
            if title:
                task.title = title
            if description:
                task.description = description
            if priority is not None:
                task.priority = priority
            if due_date:
                task.due_date = due_date
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Invalid task index!")

    def complete_task(self, index):
        try:
            task = self.tasks[index]
            task.completed = True
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Invalid task index!")

    def list_tasks(self):
        return self.tasks

    def filter_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def filter_tasks_by_completed(self, completed):
        return [task for task in self.tasks if task.completed == completed]

    def filter_tasks_by_due_date(self, due_date):
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
            return [task for task in self.tasks if task.due_date and task.due_date.date() == due_date]
        except ValueError:
            messagebox.showwarning("Warning", "Invalid due date format. Please use YYYY-MM-DD.")
            return []

    def update_task_listbox(self):
        task_listbox.delete(0, tk.END)
        for task in self.tasks:
            task_listbox.insert(tk.END, task.title)

    def on_task_select(self, event):
        try:
            index = task_listbox.curselection()[0]
            task = self.tasks[index]
            title_var.set(task.title)
            description_var.set(task.description)
            priority_var.set(task.priority)
            due_date_var.set(task.due_date.strftime('%Y-%m-%d') if task.due_date else '')
            completed_var.set(task.completed)
        except IndexError:
            pass

    def clear_entry_fields(self):
        title_var.set('')
        description_var.set('')
        priority_var.set(1)
        due_date_var.set('')
        completed_var.set(False)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

def add_task():
    title = title_var.get()
    description = description_var.get()
    priority = int(priority_var.get())
    due_date = due_date_var.get()
    task_manager.add_task(title, description, priority, due_date)
    task_manager.show_message("Task Added", "Task has been successfully added!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        task_manager.delete_task(index)
        task_manager.show_message("Task Deleted", "Task has been successfully deleted!")
    except IndexError:
        task_manager.show_message("Warning", "Please select a task to delete!")

def update_task():
    try:
        index = task_listbox.curselection()[0]
        title = title_var.get()
        description = description_var.get()
        priority = int(priority_var.get())
        due_date = due_date_var.get()
        task_manager.update_task(index, title, description, priority, due_date)
        task_manager.show_message("Task Updated", "Task has been successfully updated!")
    except IndexError:
        task_manager.show_message("Warning", "Please select a task to update!")

def complete_task():
    try:
        index = task_listbox.curselection()[0]
        task_manager.complete_task(index)
        task_manager.show_message("Task Completed", "Task has been marked as completed!")
    except IndexError:
        task_manager.show_message("Warning", "Please select a task to mark as completed!")

def list_tasks():
    tasks = task_manager.list_tasks()
    if not tasks:
        task_manager.show_message("No Tasks", "No tasks found.")
    else:
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task_listbox.insert(tk.END, task.title)

def filter_by_priority():
    priority = int(priority_var_filter.get())
    filtered_tasks = task_manager.filter_tasks_by_priority(priority)
    display_filtered_tasks(filtered_tasks)

def filter_by_completed():
    completed = completed_var_filter.get() == "True"
    filtered_tasks = task_manager.filter_tasks_by_completed(completed)
    display_filtered_tasks(filtered_tasks)

def filter_by_due_date():
    due_date = due_date_var_filter.get()
    filtered_tasks = task_manager.filter_tasks_by_due_date(due_date)
    display_filtered_tasks(filtered_tasks)

def display_filtered_tasks(filtered_tasks):
    if not filtered_tasks:
        task_manager.show_message("No Tasks", "No tasks found.")
    else:
        task_listbox.delete(0, tk.END)
        for task in filtered_tasks:
            task_listbox.insert(tk.END, task.title)

# Initialize Tkinter app
root = tk.Tk()
root.title("To-Do List Application")

# Initialize TaskManager
task_manager = TaskManager()

# Variables for task details
title_var = tk.StringVar()
description_var = tk.StringVar()
priority_var = tk.IntVar(value=1)
due_date_var = tk.StringVar()
completed_var = tk.BooleanVar(value=False)

# Labels and Entry fields for task details
tk.Label(root, text="Title:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
tk.Entry(root, textvariable=title_var, width=40).grid(row=0, column=1, columnspan=3, padx=10, pady=5)
tk.Label(root, text="Description:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
tk.Entry(root, textvariable=description_var, width=40).grid(row=1, column=1, columnspan=3, padx=10, pady=5)
tk.Label(root, text="Priority:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
ttk.Combobox(root, textvariable=priority_var, values=[1, 2, 3, 4, 5], width=6).grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=2, padx=10, pady=5, sticky=tk.E)
tk.Entry(root, textvariable=due_date_var, width=15).grid(row=2, column=3, padx=10, pady=5)
tk.Checkbutton(root, text="Completed", variable=completed_var).grid(row=3, column=1, columnspan=2, padx=10, pady=5)

# Task Listbox
tk.Label(root, text="Tasks:").grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.grid(row=5, column=0, columnspan=4, padx=10, pady=5)
task_listbox.bind('<<ListboxSelect>>', task_manager.on_task_select)

# Buttons for actions
add_button = tk.Button(root, text="Add Task", width=10, command=add_task)
add_button.grid(row=6, column=0, padx=10, pady=5)
delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task)
delete_button.grid(row=6, column=1, padx=10, pady=5)
update_button = tk.Button(root, text="Update Task", width=10, command=update_task)
update_button.grid(row=6, column=2, padx=10, pady=5)
complete_button = tk.Button(root, text="Complete Task", width=12, command=complete_task)
complete_button.grid(row=6, column=3, padx=10, pady=5)

# Buttons for listing and filtering tasks
list_button = tk.Button(root, text="List All Tasks", width=15, command=list_tasks)
list_button.grid(row=7, column=0, padx=10, pady=5)
filter_priority_button = tk.Button(root, text="Filter by Priority", width=15, command=filter_by_priority)
filter_priority_button.grid(row=7, column=1, padx=10, pady=5)
filter_completed_button = tk.Button(root, text="Filter by Completed", width=15, command=filter_by_completed)
filter_completed_button.grid(row=7, column=2, padx=10, pady=5)
filter_due_date_button = tk.Button(root, text="Filter by Due Date", width=15, command=filter_by_due_date)
filter_due_date_button.grid(row=7, column=3, padx=10, pady=5)

# Entry fields and variables for filtering tasks
priority_var_filter = tk.StringVar(value="1")
tk.Label(root, text="Filter by Priority:").grid(row=8, column=0, padx=10, pady=5, sticky=tk.E)
ttk.Combobox(root, textvariable=priority_var_filter, values=["1", "2", "3", "4", "5"], width=6).grid(row=8, column=1, padx=10, pady=5)

completed_var_filter = tk.StringVar(value="False")
tk.Label(root, text="Filter by Completed:").grid(row=8, column=2, padx=10, pady=5, sticky=tk.E)
ttk.Combobox(root, textvariable=completed_var_filter, values=["False", "True"], width=6).grid(row=8, column=3, padx=10, pady=5)

due_date_var_filter = tk.StringVar()
tk.Label(root, text="Filter by Due Date (YYYY-MM-DD):").grid(row=9, column=0, padx=10, pady=5, sticky=tk.E)
tk.Entry(root, textvariable=due_date_var_filter, width=15).grid(row=9, column=1, padx=10, pady=5)

# Initialize task listbox
task_manager.update_task_listbox()

# Start GUI main loop
root.mainloop()
