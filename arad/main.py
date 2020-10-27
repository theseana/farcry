from database import StudentInsert, StudentSelect, StudentGet, StudentSearch
from tkinter import *  
from tkinter.ttk import Notebook, Treeview
from tkcalendar import DateEntry


def length(a, b, c):
    if len(n_id.get()) == 10 and n_id.get().isdigit():
        e1.config(bg="#66BB6A")
    else:
        e1.config(bg="#ef5351")

def to_year(data):
    m, d, y= data.split('/')
    return "{}-{}-{}".format('20'+y, m.zfill(2), d.zfill(2))

def student_create():
    StudentInsert(
        name.get().lower(),
        family.get().lower(),
        to_year(birth.get()),
        n_id.get(),
        addr.get().lower(),
           )
    name.set('')
    family.set('')
    birth.set('')
    n_id.set('')
    addr.set('')
    tree.delete(*tree.get_children())
    persons = StudentSelect().get()
    for person in persons:
        tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))

def student_search():
    name = searchname.get().lower()
    family = searchfamily.get().lower()
    tree.delete(*tree.get_children())
    persons = StudentSearch(name, family).get()
    for person in persons:
        tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))


def on_double_click(event):
    item_id = event.widget.focus()
    item = event.widget.item(item_id)
    person = StudentGet(item['text']).get()[0]


root = Tk()

note = Notebook()
s_insert = Frame()
s_search = Frame()
note.add(s_insert, text="Insert")
note.add(s_search, text="search")
note.grid(row=0, column=0)
Label(s_insert, text='name').grid(row=0, column=0)
name = StringVar()
Entry(s_insert, textvariable=name).grid(row=0, column=1)

Label(s_insert, text='family').grid(row=1, column=0)
family = StringVar()
Entry(s_insert, textvariable=family).grid(row=1, column=1)

Label(s_insert, text='B Date').grid(row=2, column=0)
birth = StringVar()
Entry(s_insert, textvariable=birth).grid(row=2, column=1)

Label(s_insert, text='N. ID').grid(row=3, column=0)
n_id = StringVar()
n_id.trace("w", length)
e1 = Entry(s_insert, textvariable=n_id)
e1.grid(row=3, column=1)

Label(s_insert, text='Address').grid(row=4, column=0)
addr = StringVar()
Entry(s_insert, textvariable=addr).grid(row=4, column=1)

Button(s_insert, text='Create', command=student_create).grid(row=5, column=0)

#braye tedad ston n name o carshon
Label(s_search, text='Name').grid(row=0, column=0)
searchname = StringVar()
Entry(s_search, textvariable=searchname).grid(row=0, column=1)

Label(s_search, text='family').grid(row=1, column=0)
searchfamily = StringVar()
Entry(s_search, textvariable=searchfamily).grid(row=1, column=1)

Button(s_search,text='search', command=StudentInsert).grid(row=0, column=2, rowspan=2)
tree=Treeview(s_search, selectmode='browse')
vsb = Scrollbar(s_search, orient="vertical",command=tree.yview)
vsb.grid(row=2, column=3)
tree.configure(yscrollcommand=vsb.set)

tree["column"]=("one", "two", "three")
tree.column("#0", width=30)
tree.column("one", width=120)
tree.column("two", width=120)
tree.column("three", width=90)

tree.heading("#0", text="ID",anchor=W)
tree.heading("one", text="NAME")
tree.heading("two", text="FAMILY")
tree.heading("three", text="CODE",anchor=W)
person = StudentSelect().get()
for person in person:    
    tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))
tree.grid(row=2, column=0, columnspan=3)
tree.bind("<Double-Button-1>", on_double_click)

root.mainloop()
