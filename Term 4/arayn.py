from tkinter import *
from tkinter.ttk import Notebook,Treeview
from database import StudentInsert,StudentSelect
def lenght(a, b, c):
if len(n_id.get()) == 10 and n_id.get() .isdigit():
e1.config(bg="#ef5350")
else:
e1.config(bg="#66BB6A")
def to_year(date):
m, d, y = date.split('/')
return "{}-{}-{}".format('20'+y, m.zfill(2) ,d.zfill(2))
def student_create():
StudentInsert(name.get().lower(),
family.get().lower(),
to_year(birth.get()),
n_id.get(),
addr.get(),)
name.set("")
family.set("")
birth.set("")
n_id.set("")
addr.set("")
root = Tk()
note = Notebook()
s_insert = Frame()
# s_update = Frame()
s_search = Frame()
note.add(s_insert, text='Insert')
# note.add(s_update, text='Update')
note.add(s_search, text='Search')
note.pack()
# #################################################################### #
Label(s_insert, text='Name').pack()
name = StringVar()
Entry(s_insert, textvariable=name).pack()
Label(s_insert, text='Family').pack()
family = StringVar()
Entry(s_insert, textvariable=family).pack()
Label(s_insert, text='B. Date').pack()
birth = StringVar()
Entry(s_insert, textvariable=birth).pack()
Label(s_insert, text='N. ID').pack()
n_id = StringVar()
n_id.trace("w", lenght)
Entry(s_insert, textvariable=n_id).pack()
Label(s_insert, text='Address').pack()
addr = StringVar()
Entry(s_insert, textvariable=addr).pack()
Button(s_insert,text="create",command=student_create).pack()
Button(s_insert, text='Cancel', command=root.destroy).pack()
# #################################################################### #
Label(s_search, text='Name').grid(row=0, column=0)
search_name = StringVar()
Entry(s_search, textvariable=search_name).grid()
Label(s_insert, text='Family').grid(row=1, column=0)
search_family = StringVar()
Entry(s_insert, textvariable=search_family).grid(row=1, column=1)
Button(s_search, text='search', command=student_search).grid(row=0, column=2, rowspan=2)
tree = Treeview(s_search, selectmode='browse')
vsb = Scrollbar(s_search, orient="vertical",command=tree.yview)
vsb.grid(row=1 , column=3)
tree.configure(yscrollcommand=vsb.set)
tree["columns"]=("one","two","three")
tree.column("#0", width=30)
tree.column("one", width=120)
tree.column("two", width=120)
tree.column("three", width=90)
tree.heading("#0", text="ID" ,anchor=W)
tree.heading("one", text="Name")
tree.heading("two", text="Family")
tree.heading("three", text="Code" ,anchor=W)
persons = StudentSelect().get()
for person in persons:
tree.insert("",person[0], text=person[0], values=(person[1], person[2], person[4]))
tree.grid(row=2, column=0, columnspan=3)
# #################################################################### #
root.mainloop()