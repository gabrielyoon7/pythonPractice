from PIL import Image, ImageTk, ImageFilter
import tkinter as tk

window=tk.Tk()
canvas=tk.Canvas(window, width=1000, height=1000)
canvas.pack()

img=Image.open("e:\\yellow.gif")

out=img.filter(ImageFilter.BLUR)

tk_img=ImageTk.PhotoImage(out)

canvas.create_image(500,500,image=tk_img)

window.mainloop()
