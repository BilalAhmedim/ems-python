from tkinter import *
from view.CreateEmployee import CreateEmployee


class MainWindows:
    def __init__(self):
        root = Tk()
        root.title("Employee Management System")

        button_create = Button(root,
                               text="Create Employee",
                               width=20, height=4, pady=50, padx=50,
                               border=0, bg="#536ed2", fg="#fff",
                               font=('', 22),
                               command=lambda: CreateEmployee('Create Employee'))

        button_view = Button(root,
                             text="View Employee", width=20, height=4, pady=50,
                             padx=50, border=0, bg="#dac41d", fg="#fff", font=('', 22),
                             command=lambda: CreateEmployee('View Employee Records'))

        button_daily_updates = Button(root,
                                      text="Daily Updates", width=20, height=4, pady=50, padx=50,
                                      border=0, bg="#3cb187", fg="#fff", font=('', 22),
                                      command=lambda: CreateEmployee('Daily Update & Feeds'))

        button_delete = Button(root,
                               text="Delete Employee Record", width=20, height=4, pady=50, padx=50,
                               border=0, bg="#b33c3c", fg="#fff", font=('', 22),
                               command=lambda: CreateEmployee('Delete Employee Record'))

        button_create.grid(row=0, column=0, columnspan=4)
        button_view.grid(row=0, column=4, columnspan=4)
        button_daily_updates.grid(row=1, column=0, columnspan=4)
        button_delete.grid(row=1, column=4, columnspan=4)

        root.mainloop()
