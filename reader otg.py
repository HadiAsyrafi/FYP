from Tkinter import *
import ttk
import textract
import Tkinter, tkFileDialog

from PIL import Image, ImageTk
from web_scraper import web_scraper
from lang_detector import lang_detect

class mainGui:

    def __init__(self, master):

	# master

        self.master = master
	self.master.geometry("%dx%d" % (390, 800))
        self.master.title("OTG Reader")
	self.master.resizable(width=False, height=True)

	# image
	bg_image = Image.open("Picture/case2.png")
	bg_image = ImageTk.PhotoImage(bg_image)

	smiley_image = Image.open("Picture/smiley4.png")
	resized = smiley_image.resize((40, 40),Image.ANTIALIAS)
        smiley_image = ImageTk.PhotoImage(resized)

	book_image = Image.open("Picture/book.png")
	resized = book_image.resize((40, 40),Image.ANTIALIAS)
        book_image = ImageTk.PhotoImage(resized)

	hg_image = Image.open("Picture/hg.png")
	resized = hg_image.resize((50, 40),Image.ANTIALIAS)
        hg_image = ImageTk.PhotoImage(resized)

	# mainframe

	bg = ttk.Label(root, image=bg_image)
	self.mainframe = ttk.Frame(bg, padding="3 3 12 12")
	self.mainframe.pack(fill="both", expand=True, padx=40, pady=130)

	# variable

	self.url = StringVar()
	self.menuvar = StringVar()
	self.language = StringVar()
	self.message = "Enter Topic"
	choices = { 'Wikipedia','Browse','Capture'}

	# init

	self.url.set(self.message)
	self.language.set('Language')
	self.menuvar.set('Wikipedia')
	vcmd = master.register(self.validate)
        
	# widget

	self.entry = Entry(self.mainframe, validate="all", validatecommand=(vcmd, '%P'), textvariable=self.url)
	self.menu = OptionMenu(self.mainframe, self.menuvar, *choices, command=self.menu)
	self.textPad(self.mainframe)
	self.lang_label = ttk.Label(self.mainframe, textvariable=self.language, width=8).grid(row=1, column=0)
	self.sentiment = ttk.Label(self.mainframe, text="Smtc").grid(row=1, column=1)
	self.smiley = Button(self.mainframe, image=smiley_image, bd=0).grid(row=1, column=2, sticky = E)
	self.summarizer = Button(self.mainframe, image=book_image, bd=0).grid(row=1, column=3, sticky = W)
	self.highlight = Button(self.mainframe, image=hg_image, bd=0).grid(row=1, column=3, sticky=E)

	# reassign
	
	bg.image = bg_image
	self.smiley = smiley_image
	self.summarizer = book_image
	self.highlight = hg_image

        # Layout

	bg.place(x=0, y=0, relwidth=1, relheight=1)
	self.entry.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)
        self.menu.grid(row=0, column=3, sticky=W+E)

	# bind

	self.entry.bind('<FocusIn>', self.on_entry_click)
	self.entry.bind('<FocusOut>', self.on_focusout)
	self.entry.bind('<Return>', self.wiki_scraper)
	master.bind ('<Escape>', self.close)
	# config

	self.menu.config(width=5)


    # methods

    def textPad(self,frame):
	
	# widget

	textPad=ttk.Frame(frame)
	self.text=Text(textPad, relief="sunken", height=26, width=40)	
	scroll=ttk.Scrollbar(textPad, command=self.text.yview)

	# configure / layout

	self.text.configure(yscrollcommand=scroll.set, state=DISABLED)
	self.text.config(state=DISABLED)
	scroll.pack(side=RIGHT, fill=Y)
	self.text.pack()		
	textPad.grid(column=0, row=2, columnspan=4)
	return

    def validate(self, value):
	return True


    def update_text(self, text):

	self.text.config(state=NORMAL)
    	self.text.delete(1.0, END)
    	self.text.insert(END, text)
    	self.text.config(state=DISABLED)
	self.lang_detector(text)
	return
	
    def menu(self, value):

	if value == 'Browse':
		file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
		if file != None:
		    data = file.read()
		    file.close()
	return

    def on_entry_click(self, event):

	if self.entry.get() == self.message:
		self.entry.delete(0, "end")
	return

    def on_focusout(self, event):

	if self.entry.get() == '':
		self.entry.insert(0, self.message)
	return

    def wiki_scraper(self, event):

	site = self.entry.get()

	if site:
		scraper = web_scraper(site)
		txt = scraper.txt
		self.update_text(txt)
	return

    def lang_detector(self, txt):
	lang = lang_detect(txt)
	self.language.set(lang.detect_language().capitalize())


    def close(self, event):
	self.master.quit()
	return
	 

root = Tk()
my_gui = mainGui(root)
root.mainloop()

