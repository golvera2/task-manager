import tkinter as tk

class TaskManager:
    def __init__(self, master):
        self.master = master
        master.title("Task Manager")

        self.tasks = []
        self.create_widgets()
        self.create_menu()

    def create_widgets(self):
        self.task_list = tk.Listbox(self.master)
        self.task_list.pack()

        self.add_task_frame = tk.Frame(self.master)
        self.add_task_frame.pack()

        self.task_entry = tk.Entry(self.add_task_frame)
        self.task_entry.pack(side='left')

        self.add_task_button = tk.Button(self.add_task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side='left')

    def create_menu(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_tasks)
        file_menu.add_command(label="Open", command=self.open_tasks)

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.task_list.insert("end", task)
        self.task_entry.delete(0, "end")

    def save_tasks(self):
        filepath = filedialog.asksaveasfilename()
        if filepath:
            with open(filepath, 'w') as f:
                for task in self.tasks:
                    f.write(task
