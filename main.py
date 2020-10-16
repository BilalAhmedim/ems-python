from model.Connect import connect

from tkinter import *
from view.new_window import new_window

root = Tk()

ButtonCreate = Button(root, text="Create Employee",width=20 ,height=4 ,pady=50, padx=50, border=0, bg="#536ed2", fg="#fff", font=('', 22), command=lambda: new_window('Create Employee'))
ButtonView = Button(root, text="View Employee",width=20 ,height=4 ,pady=50, padx=50, border=0, bg="#dac41d", fg="#fff", font=('', 22))
ButtonDailyUpdates = Button(root, text="Daily Updates",width=20 ,height=4 ,pady=50, padx=50, border=0, bg="#3cb187", fg="#fff", font=('', 22))
ButtonDelete = Button(root, text="Delete Employee Record",width=20 ,height=4 ,pady=50, padx=50, border=0, bg="#b33c3c", fg="#fff", font=('', 22))

ButtonCreate.grid(row=0, column=0, columnspan=4)
ButtonView.grid(row=0, column=4, columnspan=4)
ButtonDailyUpdates.grid(row=1, column=0, columnspan=4)
ButtonDelete.grid(row=1, column=4, columnspan=4)

root.mainloop()
