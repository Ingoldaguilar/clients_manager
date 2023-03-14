# ---- UI Documentation ----
"""
A file for store the user interface.
"""
# ---- End UI Documentation ----

# ---- Imports ----
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, WARNING
import helpers
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

class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Create client")
        self.build()
        self.center()

        # user can't interact with the main window
        # if it's another opened.
        self.transient(parent)
        self.grab_set()

    def create_client(self):
        self.master.treeview.insert(
            parent='', index='end', iid=self.ssn.get(),
            values=(self.ssn.get(), self.name.get(), self.last_name.get())
        )
        self.close()

    def close(self):
        # destroy a window
        self.destroy()
        self.update()

    def validate(self, event, index):
        value = event.widget.get()
        valid = helpers.valid_ssn(value, db.Clients.l) if index == 0 \
                else (value.isalpha() and len(value) >= 2 and len(value) <= 30)
        event.widget.configure({"bg":"Green" if valid else "Red"})

        # change the button status based on choose
        self.validations[index] = valid
        self.create.config(state=NORMAL if self.validations == [1,1,1] else DISABLED)

    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text="SSN (2 ints and 1 upper char)").grid(row=0, column=0)
        Label(frame, text="Name (2 to 30 chars)").grid(row=0, column=1)
        Label(frame, text="LastName (2 to 30 chars)").grid(row=0, column=2)

        ssn = Entry(frame)
        ssn.grid(row=1, column=0)
        # event
        ssn.bind('<KeyRelease>', lambda event: self.validate(event, 0) )

        name = Entry(frame)
        name.grid(row=1, column=1)
        name.bind('<KeyRelease>', lambda event: self.validate(event, 1) )

        LastName = Entry(frame)
        LastName.grid(row=1, column=2)
        LastName.bind('<KeyRelease>', lambda event: self.validate(event, 2) )

        frame = Frame(self)
        frame.pack(pady=10)
        create = Button(frame, text="create", command=self.create_client)
        create.configure(state=DISABLED)
        create.grid(row=0, column=0)
        Button(frame, text="cancel", command=self.close).grid(row=0, column=1)

        self.validations = [0, 0, 0]
        self.create = create
        self.ssn = ssn
        self.name = name
        self.last_name = LastName

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
        Button(frame, text="Create", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modify", command=None).grid(row=0, column=1)
        Button(frame, text="Delete", command=self.delete).grid(row=0, column=2)

        # access to the treeview from another methods
        self.treeview = treeview

    def delete(self):
        client = self.treeview.focus()
        if client:
            field = self.treeview.item(client, 'values')
            confirm = askokcancel(
                title="Deleting confirmation",
                message=f"Are you sure you want to delete {field[1]} {field[2]}",
                icon=WARNING
            )
            if confirm:
                self.treeview.delete(client)

    def create(self):
        CreateClientWindow(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()