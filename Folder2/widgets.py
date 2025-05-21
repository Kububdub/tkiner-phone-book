import tkinter as tk
from functions import *

class Entry(tk.Entry):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack()


class ContactList(tk.Label):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(text = get_contacts())

        self.pack()


class SaveButton(tk.Button):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(text = 'save contacts')


        self.pack()
