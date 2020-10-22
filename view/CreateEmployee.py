from tkinter import *
from view.NewWidow import NewWindow
from PIL import Image, ImageTk


class CreateEmployee(NewWindow):

    def __init__(self, title):
        super().__init__(title)
        # Image
        load = Image.open('E:/site/python/ems-python/assets/user-picture.png')
        render = ImageTk.PhotoImage(load)
        # Creating
        # Frames
        self.window.config(padx=20, pady=20)
        frame_id = Frame(self.window, padx=20, pady=10)
        frame_name = Frame(self.window, padx=20, pady=10)
        frame_role = Frame(self.window, padx=20, pady=10)
        frame_photo = Frame(self.window, padx=20, pady=10)
        frame_salary = Frame(self.window, padx=20, pady=10)
        frame_advance = Frame(self.window, padx=20, pady=10)
        frame_mobile = Frame(self.window, padx=20, pady=10)
        frame_aadhar = Frame(self.window, padx=20, pady=10)
        frame_address = Frame(self.window, padx=20, pady=10)
        frame_submit = Frame(self.window, padx=20, pady=20)
        # Labels
        label_id = Label(frame_id, text="ID", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_name = Label(frame_name, text="Name", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_role = Label(frame_role, text="Role", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_photo = Label(frame_photo, text="Photo", width=5, font=('', 16), anchor=E, justify=LEFT)
        label_image = Label(frame_photo, image=render)
        label_image.image = render  # Reference object for prevent to goto garbage collector
        label_salary = Label(frame_salary, text="Basic Salary", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_advance = Label(frame_advance, text="Advance", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_mobile = Label(frame_mobile, text="Mobile No", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_aadhar = Label(frame_aadhar, text="Aadhar No", width=10, font=('', 16), anchor=W, justify=LEFT)
        label_address = Label(frame_address, text="Address", width=10, font=('', 16), anchor=W, justify=LEFT)

        # Inputs
        entry_id = Entry(frame_id, font=('', 16))
        entry_name = Entry(frame_name, font=('', 16))
        entry_role = Entry(frame_role, font=('', 16))
        entry_salary = Entry(frame_salary, font=('', 16))
        entry_advance = Entry(frame_advance, font=('', 16))
        entry_mobile = Entry(frame_mobile, font=('', 16))
        entry_aadhar = Entry(frame_aadhar, font=('', 16))
        entry_address = Entry(frame_address, font=('', 16))
        # Button
        browse_button = Button(frame_photo, text="Browse", font=('', 16), padx=10)
        submit_button = Button(frame_submit, text="Submit", font=('', 16), padx=10)

        # Placing
        # Labels
        label_photo.grid(row=0, column=1)
        label_image.grid(row=1, column=1)
        label_id.grid(row=0, column=0)
        label_name.grid(row=1, column=0)
        label_role.grid(row=2, column=0)
        label_salary.grid(row=3, column=0)
        label_advance.grid(row=4, column=0)
        label_mobile.grid(row=5, column=0)
        label_aadhar.grid(row=6, column=0)
        label_address.grid(row=7, column=0)
        # Entry
        entry_id.grid(row=0, column=1)
        entry_name.grid(row=1, column=1)
        entry_role.grid(row=2, column=1)
        entry_salary.grid(row=3, column=1)
        entry_advance.grid(row=4, column=1)
        entry_mobile.grid(row=5, column=1)
        entry_aadhar.grid(row=6, column=1)
        entry_address.grid(row=7, column=1)
        # Button
        submit_button.grid(row=8, column=0)
        browse_button.grid(row=2, column=1)
        # Frames
        frame_photo.grid(row=0, column=1, rowspan=6)
        frame_id.grid(row=0, column=0)
        frame_name.grid(row=1, column=0)
        frame_role.grid(row=2, column=0)
        frame_salary.grid(row=3, column=0)
        frame_advance.grid(row=4, column=0)
        frame_mobile.grid(row=5, column=0)
        frame_aadhar.grid(row=6, column=0)
        frame_address.grid(row=7, column=0)
        frame_submit.grid(row=8, column=0)

