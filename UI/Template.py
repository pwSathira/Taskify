import tkinter as tk
from tkinter import ttk


class Template(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Taskify")
        self.master.geometry("1280x720")
        self.master.iconbitmap("Resources/check.ico")

        self.setupUi()
        self.pack()


    def setupUi(self):
        # Define user interface elements here

        # Checkbox
        self.checkbox_var = tk.BooleanVar()
        original_unchecked_image = tk.PhotoImage(file="Resources/unchecked.png")
        original_checked_image = tk.PhotoImage(file="Resources/checked.png")
        scale_factor = 10
        self.checked_image = original_checked_image.subsample(scale_factor, scale_factor)
        self.unchecked_image = original_unchecked_image.subsample(scale_factor, scale_factor)
        self.checkbox_label = tk.Label(self, image=self.unchecked_image)
        self.checkbox_label.grid(row=0, column=0, padx=0, pady=50)
        self.checkbox_label.bind("<Button-1>", self.toggle_checkbox)
        print(self.checkbox_var.get())

    def toggle_checkbox(self, event):
        if self.checkbox_var.get():
            self.checkbox_label.configure(image=self.unchecked_image)
            self.checkbox_var.set(False)
        else:
            self.checkbox_label.configure(image=self.checked_image)
            self.checkbox_var.set(True)

