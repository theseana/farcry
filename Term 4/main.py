from tkcalendar import DateEntry

from tkinter import *
from tkinter.ttk import Notebook, Treeview, Scrollbar

from database import StudentInsert, StudentSelect,StudentSearch, StudentGet, StudentUpdate, GradeInsert


def grade():
    GradeInsert(
    std.get().split("-")[0],
    math.get(),
    physics.get(),
    chemistry.get(),
    history.get(),
    programming.get()
    )
    math.set('')
    physics.set('')
    chemistry.set('')
    history.set('')
    programming.set('')

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
    tree_update()


def tree_update():
    tree.delete(*tree.get_children())
    persons = StudentSelect().get()
    for person in persons:
        tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))


def student_search():
    name = search_name.get().lower()
    family = search_family.get().lower()
    tree.delete(*tree.get_children())
    persons = StudentSearch(name, family).get()
    for person in persons:
        tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))


def on_double_click(event):
    def student_update():
        StudentUpdate(name_top.get(),
            family_top.get(),
            id_top.get(),
            birth_top.get(),
            addr_top.get(),
            item['text']
            )
        top.destroy()
        tree_update()

    item_id = event.widget.focus()
    item = event.widget.item(item_id)
    person = StudentGet(item['text']).get()[0]

    top = Toplevel()

    Label(top, text="Name").grid(row=0, column=0)
    name_top = StringVar()
    name_top.set(person[1])
    Entry(top, textvariable=name_top).grid(row=0, column=1)

    Label(top, text="Family").grid(row=1, column=0)
    family_top = StringVar()
    family_top.set(person[2])
    Entry(top, textvariable=family_top).grid(row=1, column=1)

    Label(top, text="B. Date").grid(row=2, column=0)
    birth_top = StringVar()
    birth_top.set(person[3])
    Entry(top, textvariable=birth_top).grid(row=2, column=1)

    Label(top, text="ID").grid(row=3, column=0)
    id_top = StringVar()
    id_top.set(person[4])
    Entry(top, textvariable=id_top).grid(row=3, column=1)

    Label(top, text="Address").grid(row=4, column=0)
    addr_top = StringVar()
    addr_top.set(person[5])
    Entry(top, textvariable=addr_top).grid(row=4, column=1)

    Button(top, text="Edit", command=student_update).grid(row=5, column=0, columnspan=2)
    Button(top, text="Cancel", comman=top.destroy).grid(row=6, column=0, columnspan=2)

root = Tk()

note = Notebook()

s_insert = Frame()
s_search = Frame()
g_insert = Frame()

note.add(s_insert, text='Insert')
note.add(s_search, text='Search')
note.add(g_insert, text='Grade Insert')


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
Label(s_search, text='Name').grid(row=0, column=0)
search_name = StringVar()
Entry(s_search, textvariable=search_name).grid(row=0, column=1)

Label(s_search, text='Family').grid(row=1, column=0)
search_family = StringVar()
Entry(s_search, textvariable=search_family).grid(row=1, column=1)

Button(s_search, text='Search', command=student_search).grid(row=0, column=2, rowspan=2)
tree = Treeview(s_search)
vsb = Scrollbar(s_search, orient="vertical",command=tree.yview)
vsb.grid(row=2, column=3)
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
tree.grid(row=2, column=0, columnspan=3)
tree.bind("<Double-Button-1>", on_double_click)
# #################################################################### #
Label(g_insert, text='Math').grid(row=0, column=0)
math = StringVar()
Entry(g_insert, textvariable=math).grid(row=0, column=1)

Label(g_insert, text='Chemistry').grid(row=1, column=0)
chemistry = StringVar()
Entry(g_insert, textvariable=chemistry).grid(row=1, column=1)

Label(g_insert, text='Physics').grid(row=2, column=0)
physics = StringVar()
Entry(g_insert, textvariable=physics).grid(row=2, column=1)

Label(g_insert, text='History').grid(row=3, column=0)
history = StringVar()
Entry(g_insert, textvariable=history).grid(row=3, column=1)

Label(g_insert, text='Programming').grid(row=4, column=0)
programming = StringVar()
Entry(g_insert, textvariable=programming).grid(row=4, column=1)

Label(g_insert, text='Student ID').grid(row=5, column=0)
values = []
for _ in StudentSelect().get():
    values.append(f"{_[0]}-{_[1]}{_[2]}")
std = StringVar()
Spinbox(g_insert, textvariable=std,state='readonly', values=tuple(values)).grid(row=5, column=1)
Button(g_insert, text='Create', command=grade).grid(row=6, column=0, columnspan=2, sticky=W+E)
##################################

root.mainloop()
