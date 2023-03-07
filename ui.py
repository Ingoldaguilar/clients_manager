# ---- UI Documentation ----
"""
A file for store the user interface.
"""
# ---- End UI Documentation ----

# ---- Imports ----
from tkinter import *
# ---- End Imports ----

class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("Clients Manager")
        self.build()

    def build(self):
        button = Button(self, text="Hello", command=self.hello)
        button.pack()

    def hello(self):
        print("Hello world!")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()