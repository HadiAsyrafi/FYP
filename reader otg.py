from Tkinter import *
import ttk
import textract
import Tkinter, tkFileDialog

from PIL import Image, ImageTk
from web_scraper import web_scraper
from lang_detector import lang_detect
from highlighter import highlighter
from sentiment import *
from summariser import *

class mainGui:

    def __init__(self, master):
	# master
        self.master = master
	self.master.geometry("%dx%d+%d+%d" % (390, 800, 500, 0))
        self.master.title("OTG Reader")
	self.master.resizable(width=False, height=True)

	# image
	bg_image = Image.open("Picture/case2.png")
	bg_image = ImageTk.PhotoImage(bg_image)

	smiley_image = Image.open("Picture/smiley4.png")
	resized = smiley_image.resize((32, 32),Image.ANTIALIAS)
        smiley_image = ImageTk.PhotoImage(resized)

	book_image = Image.open("Picture/book.png")
	resized = book_image.resize((36, 32),Image.ANTIALIAS)
        book_image = ImageTk.PhotoImage(resized)

	hg_image = Image.open("Picture/hg.png")
	resized = hg_image.resize((40, 32),Image.ANTIALIAS)
        hg_image = ImageTk.PhotoImage(resized)

	# mainframe

	bg = ttk.Label(root, image=bg_image)
	self.mainframe = ttk.Frame(bg, padding="3 3 12 12")
	self.mainframe.pack(fill="both", expand=True, padx=40, pady=130)

	# variable
	self.url = StringVar()
	self.menuvar = StringVar()
	self.language = StringVar()
	self.sentiment_label = StringVar()
	self.message = "Enter Topic"
	choices = { 'Wiki','Browse','Capture'}

	# init
	self.init()
	self.menuvar.set('Wiki')
	vcmd = master.register(self.validate)
        
	# widget

	self.entry = Entry(self.mainframe, validate="all", validatecommand=(vcmd, '%P'), textvariable=self.url)
	self.menu = OptionMenu(self.mainframe, self.menuvar, *choices, command=self.menu_)
	self.textPad(self.mainframe)
	self.lang_label = ttk.Label(self.mainframe, textvariable=self.language, width=12, relief='sunken').grid(row=1, column=0, sticky=N+S, pady=1)
	self.sentiment = ttk.Label(self.mainframe, textvariable=self.sentiment_label, width=9, relief='raised').grid(row=1, column=1, sticky=N+S, pady=1)
	self.smiley = Button(self.mainframe, image=smiley_image, command=self.sentiment_analysis, bd=0).grid(row=1, column=2, sticky=E, padx=1)
	self.summarizer = Button(self.mainframe, image=book_image, command=self.summarize, bd=0).grid(row=1, column=3, sticky=W+N+S)
	self.highlight = Button(self.mainframe, image=hg_image, command=self.highlighting, bd=0).grid(row=1, column=3, sticky=E+N+S)

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
    def init(self):
	self.high = False
	self.sum = False
	self.ori_text = ''
	self.pro_text = ''
	self.before_sum = ''
	self.url.set(self.message)
	self.language.set('     Language')
	self.sentiment_label.set(' Sentiment')
	return
	

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


    def update_text(self, display):
	self.text.config(state=NORMAL)
    	self.text.delete(1.0, END)
    	self.text.insert(END, display)
    	self.text.config(state=DISABLED)
	return
	
    def menu_(self, value):
	self.init()
	if value == 'Browse':
		file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
		if file != None:
		    txt = textract.process(file.name)
		    print "File loaded successfully"
		    self.ori_text = txt
		    self.pro_text = self.ori_text
		    self.update_text(self.pro_text)
		    self.lang_detector(self.ori_text)
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
	self.init()
	if site:
		scraper = web_scraper(site)
		txt = scraper.txt
		self.ori_text = txt
		self.pro_text = self.ori_text
		self.update_text(self.pro_text)
		self.lang_detector(self.ori_text)
		print 'Scraping Complete'
	return

    def lang_detector(self, txt):
	lang = lang_detect(txt)
	self.language.set('     ' + lang.detect_language().capitalize())

    def highlighting(self):
	self.high = not self.high
	if self.high:
		hg = highlighter(self.pro_text)
		hg.highlight()
		word_list = self.pro_text.split()
		tags = ["tg" + str(k) for k in range(len(word_list))]
		self.text.config(state=NORMAL)
	    	self.text.delete(1.0, END)
		for ix, word in enumerate(word_list):
			if any(word[:len(keyword)] == keyword for keyword in hg.keywords):
				self.color_text(tags[ix], word, 'blue')
			else:
				self.color_text(tags[ix], word)

		self.text.config(state=DISABLED)
		print 'Highlighting Complete'
	else:
		self.update_text(self.pro_text)
	return

    def color_text(self, tag, word, fg_color='black', bg_color='white'):
	# add a space to the end of the word
	if '.' in word:
		word = word + '\n\n'
	else:
		word = word + ' '
	self.text.insert('end', word)
	end_index = self.text.index('end')
	begin_index = "%s-%sc" % (end_index, len(word) + 1)
	self.text.tag_add(tag, begin_index, end_index)
	self.text.tag_config(tag, foreground=fg_color, background=bg_color)
	return

    def sentiment_analysis(self):
	if self.pro_text == '':
		return

	splitter = Splitter()
	postagger = POSTagger()
	splitted_sentences = splitter.split(self.pro_text)
	pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
	dicttagger = DictionaryTagger(['dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])
	dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
	score = sentiment_score(dict_tagged_sentences)
	if score > 0:
		self.sentiment_label.set("   Positive")
	else:
		self.sentiment_label.set("  Negative")
	return

    def summarize(self):
	self.sum = not self.sum
	if self.sum:
		summ = summariser(self.pro_text, len(self.pro_text)/50)
		output = summ.summarize()
		summarized = ''
		for data in output['mean_scored_summary']:
			summarized = summarized + data + '\n\n'
		print 'Summarizing Complete'
		self.before_sum = self.pro_text
		self.pro_text = summarized
		
		if self.high:
			self.high = not self.high
			self.highlighting()
			return
	else:
		if self.high:
			self.high = not self.high
			self.pro_text = self.before_sum
			self.highlighting()
			return
		else:
			self.pro_text = self.before_sum
	self.update_text(self.pro_text)
	return


    def close(self, event):
	self.master.quit()
	return
	 

root = Tk()
my_gui = mainGui(root)
root.mainloop()

