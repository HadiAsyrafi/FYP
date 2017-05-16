from Tkinter import *
import ttk
from PIL import Image, ImageTk

root = Tk()
root.geometry("%dx%d" % (390, 800)) #390,800

image = Image.open("case2.png")
image = ImageTk.PhotoImage(image)
bg_label = ttk.Label(root, image = image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = image
root.mainloop()
