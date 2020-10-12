from tkinter import *




root = Tk()
r = StringVar()
r.trace("w", length)
e1 = Entry(root, textvariable=r)
e1.pack()
root.mainloop()