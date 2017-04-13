from Tkinter import *
import ttk

class mainGui:

    def __init__(self, master):
        self.master = master
        master.title("Wikipedia Tools")
	root.resizable(width=False, height=False)
	master.geometry('860x540')

	self.mainframe = ttk.Frame(master, padding="3 3 12 12")
	self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'), textvariable=url)

	url = stringVar()

	self.add_button = Button(master, text="+", command=lambda: self.update("add"))

        

    def validate(self, url):
	return True

	

root = Tk()
my_gui = mainGui(root)
root.mainloop()

