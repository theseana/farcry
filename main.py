from tkcalendar import DateEntry

from tkinter import *
from tkinter.ttk import Notebook, Treeview, Scrollbar

from database import StudentInsert, StudentSelect


def length(a , b, c):
    if len(n_id.get()) == 10 and n_id.get().isdigit():
        e1.config(bg="#66BB6A")
    else:
        e1.config(bg="#ef5350")


def to_year(date):
    m, d, y = date.split('/')
    return "{}-{}-{}".format('20'+y, m.zfill(2) ,d.zfill(2))


def student_create():
    StudentInsert(name.get().lower(), 
                  family.get().lower(),
                  to_year(birth.get()),
                  n_id.get(),
                  addr.get())
    name.set('')
    family.set('')
    birth.set('')
    n_id.set('')
    addr.set('')
    
       
root = Tk()

note = Notebook()

s_insert = Frame()
# s_update = Frame()
s_search = Frame()

note.add(s_insert, text='Insert')
# note.add(s_update, text='Update')
note.add(s_search, text='Search')


note.grid(row=0, column=0)

# #################################################################### #
Label(s_insert, text='Name').grid(row=0, column=0)
name = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text='Family').grid(row=1, column=0)
family = StringVar()
Entry(s_insert, textvariable=family).grid(row=1, column=1)

Label(s_insert, text='B. Date').grid(row=2, column=0)
birth = StringVar()
# Entry(s_insert, textvariable=birth).grid(row=2, column=1)
DateEntry(s_insert, textvariable=birth).grid(row=2, column=1, sticky=W+E)

Label(s_insert, text='N. ID').grid(row=3, column=0)
n_id = StringVar()
n_id.trace("w", length)
e1 = Entry(s_insert, textvariable=n_id)
e1.grid(row=3, column=1)

Label(s_insert, text='Address').grid(row=4, column=0)
addr = StringVar()
Entry(s_insert, textvariable=addr).grid(row=4, column=1)

Button(s_insert, text='Create', command=student_create).grid(row=5, column=0, columnspan=2, sticky=W+E)
Button(s_insert, text='Cancel', command=root.destroy).grid(row=6, column=0, columnspan=2, sticky=W+E)
# #################################################################### #
tree = Treeview(s_search)
vsb = Scrollbar(s_search, orient="vertical",command=tree.yview)
vsb.grid(row=0, column=1)
tree.configure(yscrollcommand=vsb.set)
tree["columns"]=("one","two","three")
tree.column("#0", width=30)
tree.column("one", width=80)
tree.column("two", width=100)
tree.column("three", width=90)
#############################################  update treeview --- serach select baham --- editable treeview
tree.heading("#0",text="ID",anchor=W)
tree.heading("one", text="Name")
tree.heading("two", text="Family")
tree.heading("three", text="Code",anchor=W)
persons = StudentSelect().get()
for person in persons:
    tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))
tree.grid(row=0, column=0)
# #################################################################### #
root.mainloop()