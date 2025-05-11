import tkinter as tk

def save_buffer(contact_name, contact_num):
    if len(contact_name) > 0 and len(contact_name) < 20 and len(contact_num) > 5 and len(contact_num) < 20:
        savebtn.config(text = 'saving...')
        root.after(500, lambda: save_contact(contact_name, contact_num))
    else:
        savebtn.config(text = 'ERROR: invalid text')
        root.after(500, lambda: error())

def error():
     savebtn.config(text='save contacts')

def save_contact(contact_name, contact_num):
    
    f = open('contactlist.txt', 'a')
    f.write(f'{contact_name}: {contact_num}\n')
    f.close()
    savebtn.config(text='save contacts')
    contact_list.config(text = get_contacts())

def get_contacts():
    f = open('contactlist.txt', 'r')
    out = str('Contacts:\n\n')
    for line in f:
            out = out + line
    return out


root = tk.Tk()
root.title('contacts list')
root.geometry('800x500')
lbl1 = tk.Label(text = 'contact name')
lbl1.pack()

name = tk.Entry()
name.pack()
lbl2 = tk.Label(text = 'contact number')
lbl2.pack()

num = tk.Entry()
num.pack()

savebtn = tk.Button(text = 'save contacts', command = lambda: save_buffer(name.get(), num.get()))
savebtn.pack()

contact_list = tk.Label(text = get_contacts())
contact_list.pack()

root.mainloop()