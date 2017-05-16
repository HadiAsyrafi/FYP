from Tkinter import *
import ttk
from PIL import Image, ImageTk

class mainGui:

    def __init__(self, master):
        self.master = master
        master.title("OTG Reader")
	root.resizable(width=False, height=True)


	image = Image.open("case2.png")
	image = ImageTk.PhotoImage(image)
	bg = ttk.Label(root, image = image)
	bg.place(x=0, y=0, relwidth=1, relheight=1)
	bg.image = image


	self.mainframe = ttk.Frame(bg, padding="3 3 12 12")
	self.mainframe.pack(fill="both", expand=True, padx=40, pady=130)

	self.textPad(self.mainframe)

	self.url = StringVar()
	self.menuvar = StringVar()
	self.message = "Enter URL"
        self.url.set(self.message)

	choices = { 'Wikipedia','Browse','Capture'}
	self.menuvar.set('Wikipedia')
	self.menuvar.trace('w', self.change_dropdown)

	ttk.Label(self.mainframe).grid(row=0, column=2, sticky=E)
	ttk.Label(self.mainframe, text="Summ").grid(row=1, column=1, sticky=E)
	ttk.Label(self.mainframe, text="High").grid(row=1, column=2, sticky=E)
	ttk.Label(self.mainframe, text="Sent").grid(row=1, column=3, sticky=E)

        vcmd = master.register(self.validate)
        self.entry = Entry(self.mainframe, validate="key", validatecommand=(vcmd, '%P'), textvariable=self.url)


	self.menu = OptionMenu(self.mainframe, self.menuvar, *choices)
	self.menu.config(width=2)

        # Layout
	
	self.entry.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)
        self.menu.grid(row=0, column=3, sticky=W+E)


    def textPad(self,frame):
	
	textPad=ttk.Frame(frame)
	self.text=Text(textPad, relief="sunken", height=30, width=40)
		
	scroll=ttk.Scrollbar(textPad, command=self.text.yview)
	self.text.configure(yscrollcommand=scroll.set)
		
	scroll.pack(side=RIGHT, fill=Y)
	self.text.pack()
	textPad.grid(column=0, row=2, columnspan=4)
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
	
    def change_dropdown(*args):
    	print( self.menuvar.get() )
 

root = Tk()
root.geometry("%dx%d" % (390, 800))
my_gui = mainGui(root)
root.mainloop()

