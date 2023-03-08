# ---- UI Documentation ----
"""
A file for store the user interface.
"""
# ---- End UI Documentation ----

# ---- Imports ----
from tkinter import *
# ---- End Imports ----

class CenterWidgetMixin:

    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws / 2 - w / 2)
        y = int(hs / 2 - h / 2)

        # how it works geometry("WIDTHxHEIGHT+OFFSET_X+OFFSET_Y")
        self.geometry(f"{w}x{h}+{x}+{y}")


class MainWindow(Tk, CenterWidgetMixin):

    def __init__(self):
        super().__init__()
        self.title("Clients Manager")
        self.build()
        self.center()

    def build(self):
        button = Button(self, text="Hello", command=self.hello)
        button.pack()

    def hello(self):
        print("Hello world!")
        self.destroy()

    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)

        # how it works geometry("WIDTHxHEIGHT+OFFSET_X+OFFSET_Y")
        self.geometry(f"{w}x{h}+{x}+{y}")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()