from tkinter import *

window=Tk()
w=Label(window, text="box #1", bg="red", fg="white")
w.place(x=0,y=0)
w=Label(window, text="box #2", bg="red", fg="white")
w.place(x=20,y=20)
w=Label(window, text="box #3", bg="red", fg="white")
w.place(x=40,y=40)

window.mainloop()
