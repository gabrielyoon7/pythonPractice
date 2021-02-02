from tkinter import *

def process():
    print("Hi")

window=Tk()
button=Button(window,text="클릭하세요!", command=process)
button["fg"]="yellow"
button["bg"]="green"
button.pack()

window.mainloop()
