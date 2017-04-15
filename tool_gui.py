from Tkinter import *
import ttk

class mainGui:

    def __init__(self, master):
        self.master = master
        master.title("Wikipedia Tools")
	root.resizable(width=False, height=False)

	self.mainframe = ttk.Frame(master, padding="3 3 12 12", borderwidth=5, width=600, height=300)
	self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

	self.textPad(self.mainframe)

	self.url = StringVar()
	self.message = "Enter URL"
        self.url.set(self.message)

        vcmd = master.register(self.validate)
        self.entry = Entry(self.mainframe, validate="key", validatecommand=(vcmd, '%P'), textvariable=self.url)


	self.search_button = Button(self.mainframe, text="Search", command=self.search_url)

        # Layout
	
	self.entry.grid(row=0, column=1, columnspan=2, sticky=N+S+W+E)
        self.search_button.grid(row=0, column=3, columnspan=1, sticky=W+E)


    def textPad(self,frame):
	#add a frame and put a text area into it
	textPad=ttk.Frame(frame, padding="3 3 12 12", borderwidth=5)
	self.text=Text(textPad, relief="sunken")
		
	# add a vertical scroll bar to the text area
	scroll=ttk.Scrollbar(textPad, command=self.text.yview)
	self.text.configure(yscrollcommand=scroll.set)
		
	#pack everything
	self.text.grid(column=0, row=0, columnspan=5, rowspan=3)
	scroll.grid(column=4, row=0, rowspan=3, sticky=E)
	textPad.grid(column=0, row=2, columnspan=5, rowspan=3)
	return

    def validate(self):
	return True


    def search_url(self):
	return

    def update_text(self):
	self.textPad.config(state=NORMAL)
    	#self.textPad.delete(1.0, END)
    	#self.textPad.insert(END, text)
    	self.textPad.config(state=DISABLED)

root = Tk()
my_gui = mainGui(root)
root.mainloop()

