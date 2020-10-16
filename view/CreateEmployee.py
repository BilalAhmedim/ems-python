from tkinter import *
from view.NewWidow import NewWindow


class CreateEmployee(NewWindow):

    def __init__(self,title):
        super().__init__(title)
        # Labels
        # Bio
        label_id = Label(self.window, text="ID", width=10, font=('',16),anchor=W, justify=LEFT)
        label_name = Label(self.window, text="Name", width=10, font=('',16),anchor=W, justify=LEFT)
        label_role = Label(self.window, text="Role", width=10, font=('',16),anchor=W, justify=LEFT)
        label_photo = Label(self.window, text="Photo", width=10, font=('',16),anchor=W, justify=LEFT)
        # Salary
        label_salary = Label(self.window, text="Basic Salary", width=10, font=('',16),anchor=W, justify=LEFT)
        label_advance = Label(self.window, text="Advance", width=10, font=('',16),anchor=W, justify=LEFT)
        # Contact
        label_mobile = Label(self.window, text="Mobile No", width=10, font=('',16),anchor=W, justify=LEFT)
        label_aadhar = Label(self.window, text="Aadhar No", width=10, font=('',16),anchor=W, justify=LEFT)
        label_address = Label(self.window, text="Address", width=10, font=('',16),anchor=W, justify=LEFT)

        # Place Labels
        label_id.grid(row=0, column=0, columnspan=1)
        label_name.grid(row=1, column=0, columnspan=1)
        label_role.grid(row=2, column=0, columnspan=1)
        label_photo.grid(row=3, column=0, columnspan=1)
        label_salary.grid(row=4, column=0, columnspan=1)
        label_advance.grid(row=5, column=0, columnspan=1)
        label_mobile.grid(row=6, column=0, columnspan=1)
        label_aadhar.grid(row=7, column=0, columnspan=1)
        label_address.grid(row=8, column=0, columnspan=1)

        # Inputs



