import tkinter as tk
from widgets import *
from functions import *

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('contact list')
        self.geometry('1000x800')

        
        self.name = Entry(self)

        self.num = Entry(self)

        self.savebtn = SaveButton(self)
        self.savebtn.configure(command = lambda: save_buffer(self,  self.contactlist, self.savebtn, self.name.get(), self.num.get()))

        self.contactlist = ContactList(self)      

        




root = MainApp()

root.mainloop()
