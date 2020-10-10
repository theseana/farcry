from tkinter import *
from tkinter.ttk import Notebook

root = Tk()

note = Notebook()

s_insert = Frame()
s_update = Frame()
s_delete = Frame()

note.add(s_insert, text='Insert')
note.add(s_update, text='Update')

note.grid(row=0, column=0)

# #################################################################### #
Label(s_insert, text='Name').grid(row=0, column=0)
name = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text='Family').grid(row=0, column=0)
family = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text='B. Date').grid(row=0, column=0)
birth = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text='N. ID').grid(row=0, column=0)
n_id = StringVar()
Entry(s_insert, textvariable=n_id).grid(row=0, column=1)

Label(s_insert, text='Address').grid(row=0, column=0)
addr = StringVar()
Entry(s_insert, textvariable=addr).grid(row=0, column=1)

# #################################################################### #
root.mainloop()