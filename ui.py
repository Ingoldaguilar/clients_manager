# ---- UI Documentation ----
"""
A file for store the user interface.
"""
# ---- End UI Documentation ----

# ---- Imports ----
from tkinter import *
from tkinter import ttk
import database as db
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
        # frame for the program.
        frame = Frame(self)
        frame.pack()

        # create a table(treeview) in our frame.
        treeview = ttk.Treeview(frame)
        treeview['columns'] = ('SSN', 'Name', 'LastName')

        # column's configuration
        treeview.column("#0", width=0, stretch=NO) # refer to column 0
        treeview.column("SSN", anchor='w')
        treeview.column("Name", anchor='w')
        treeview.column("LastName", anchor='w')

        #header's configuration
        treeview.heading("SSN", text="SSN", anchor=CENTER)
        treeview.heading("Name",  text="Name", anchor=CENTER)
        treeview.heading("LastName",  text="LastName", anchor=CENTER)

        # scrollbar configuration
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # set scrollbar in the treeview
        treeview['yscrollcommand'] = scrollbar.set

        # show db information in the table
        for client in db.Clients.l:
            treeview.insert(
                parent='', index='end', iid=client.ssn,
                values=(client.ssn, client.name, client.last_name)
            )

        # pack the treeview
        treeview.pack()

        # Button's Frame
        frame = Frame(self)
        frame.pack(pady=20)

        # Buttons
        Button(frame, text="Create", command=None).grid(row=0, column=0)
        Button(frame, text="Modify", command=None).grid(row=0, column=1)
        Button(frame, text="Delete", command=None).grid(row=0, column=2)

        # access to the treeview from another methods
        self.treeview = treeview

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