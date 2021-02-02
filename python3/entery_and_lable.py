from tkinter import *

window=Tk()
l1=Label(window, text="F")
l2=Label(window, text="C")
l1.pack()
l2.pack()

e1=Entry(window)
e2=Entry(window)
e1.pack()
e2.pack()

b1=Button(window, text="F->C")
b2=Button(window, text="C->F")
b1.pack()
b2.pack()

l2['text']="new"

window.mainloop()
