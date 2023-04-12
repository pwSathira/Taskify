import tkinter as tk
import UI.CheckBox as CheckBoxModule
from Database import DBTasks


class Template(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.master.title("Taskify")
        self.master.geometry("1280x720")
        self.master.iconbitmap("Resources/check.ico")
        self.setupUi()
        self.pack()

    def setupUi(self):
        # Define user interface elements here
        checkBoxList = []
        for i in range(3):
            self.addCheckBox(i, checkBoxList)

        DBTasks.DBTasks.__init__(self)
        tasks = DBTasks.DBTasks.getTasks(self, 1)
        print(tasks)

    def addCheckBox(self, index, checkBoxList):
        self.checkbox = CheckBoxModule.CheckBox(self, index=index)
        self.checkbox.grid(row=index, column=0)
        checkBoxList.append(self.checkbox)
