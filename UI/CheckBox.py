import tkinter as tk
import Logic.ImageUtil as imgUtil


class CheckBox(tk.Frame):
    def __init__(self, master=None, index=0, **kwargs):
        super().__init__(master, **kwargs)

        self.var = tk.BooleanVar()
        scale_factor = 10
        self.checked_image = imgUtil.ImageUtil.createImage(scale_factor, "Resources/checked.png")
        self.unchecked_image = imgUtil.ImageUtil.createImage(scale_factor, "Resources/unchecked.png")

        self.label = tk.Label(self, image=self.unchecked_image)
        self.label.grid(row=index, column=0, padx=0, pady=20)
        self.label.bind("<Button-1>", self.toggle_checkbox)

        self.text = tk.Text(self, height=0.1, width=20, font=("Times New Roman", 30))
        self.text.grid(row=index, column=1, padx=10, pady=10)

    def toggle_checkbox(self, event):
        self.var.set(not self.var.get())
        if self.var.get():
            self.label.config(image=self.checked_image)
        else:
            self.label.config(image=self.unchecked_image)


