from tkinter import *
from tkinter import messagebox
from tkinter import filedialog



def open():
    file=filedialog.askopenfile(parent=window, mode='r')
    if file != None:
        lines=file.read()
        text.insert('1.0', lines)
        file.close()
        
def save():
    file = filedialog.asksaveasfile(parent=window, mode='w')
    if file != None:
        lines = text.get('1.0', END+'-1c')
        file.write(lines)
        file.close()

def exit():
    if messagebox.askokcancel("Quit","wanna quit?"):
        window.destroy()

def about():
    label=messagebox.showinfo("About", "Memo Program")

window=Tk()
text=Text(window,height=30,width=80)
text.pack()

menu=Menu(window)
window.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Exit", command=exit)
helpmenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

window.mainloop()
