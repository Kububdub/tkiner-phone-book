import tkinter as tk


def save_buffer(root, contactlist, savebtn, contact_name, contact_num):
    if len(contact_name) > 0 and len(contact_name) < 25 and len(contact_num) > 0 and len(contact_num) < 25:
        savebtn.config(text = 'saving...')
        root.after(500, lambda: save_contact(savebtn, contactlist, contact_name, contact_num))
    else:
        savebtn.config(text = 'ERROR: invalid text')
        root.after(500, lambda: error(savebtn))



def error():
     savebtn.config(text='save contacts')

     

def save_contact(savebtn, contactlist, contact_name, contact_num):
    
    f = open('contactlist.txt', 'a')
    f.write(f'{contact_name}: {contact_num}\n')
    f.close()
    savebtn.config(text='save contacts')
    contactlist.config(text = get_contacts())
    

def get_contacts():
    f = open('contactlist.txt', 'r')
    out = str('Contacts:\n\n')
    for line in f:
            out = out + line
    return out

    
