import tkinter as tk
import UI.Template as Template


class Main(Template.Template):
    def __init__(self, master=None):
        super().__init__(master)
        self.setupUi()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    root.mainloop()
