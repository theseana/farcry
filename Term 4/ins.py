from tkinter import *


class Sepehr(Tk):

    def __init__(self):
        Tk.__init__(self)        
        self.name = StringVar()
        Entry(self, textvariable=self.name).pack()
        Button(self, text="Sepehr", command=self.dastoor).pack()


    def dastoor(self):
        print(self.name.get())

    def loop(self):  
        self.mainloop()