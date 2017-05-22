# -*- coding: utf-8 -*-

# import libraries
from Tkinter import *
import cv2
import ttk
import time
import imutils
import textract
import threading
import numpy as np
import Tkinter, tkFileDialog

from PIL import Image, ImageTk
from cam2 import PhotoBoothApp
from imutils.video import VideoStream

# import classes
from sentiment import *
from summariser import *
from web_scraper import web_scraper
from lang_detector import lang_detect
from highlighter import highlighter



class mainGui:

    def __init__(self, master):
	# master
        self.master = master
	self.master.geometry("%dx%d+%d+%d" % (390, 800, 500, 0))
        self.master.title("OTG Reader")
	self.master.resizable(width=False, height=True)

	# image
	bg_image = Image.open("Backup/Picture/case2.png")
	bg_image = ImageTk.PhotoImage(bg_image)

	smiley_image = Image.open("Backup/Picture/smiley4.png")
	resized = smiley_image.resize((30, 30),Image.ANTIALIAS)
        smiley_image = ImageTk.PhotoImage(resized)

	book_image = Image.open("Backup/Picture/book.png")
	resized = book_image.resize((33, 30),Image.ANTIALIAS)
        book_image = ImageTk.PhotoImage(resized)

	hg_image = Image.open("Backup/Picture/hg.png")
	resized = hg_image.resize((35, 30),Image.ANTIALIAS)
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
	choices = { 'Wikipedia','Browse','Capture'}

	# init
	self.init()
	self.caminit()
	self.menuvar.set('Wikipedia')
	vcmd = master.register(self.validate)
        
	# widget
	self.entry = Entry(self.mainframe, validate="all", validatecommand=(vcmd, '%P'), textvariable=self.url)
	self.menu = OptionMenu(self.mainframe, self.menuvar, *choices, command=self.menu_)
	self.textPad(self.mainframe)
	self.lang_label = ttk.Label(self.mainframe, textvariable=self.language, width=11, relief='sunken')
	self.sentiment = ttk.Label(self.mainframe, textvariable=self.sentiment_label, width=10, relief='raised')
	self.smiley = Button(self.mainframe, image=smiley_image, command=self.sentiment_analysis, bd=0)
	self.summarizer = Button(self.mainframe, image=book_image, command=self.summarize, bd=0)
	self.highlight = Button(self.mainframe, image=hg_image, command=self.highlighting, bd=0)

	# Layout
	bg.place(x=0, y=0, relwidth=1, relheight=1)
	self.entry.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)
        self.menu.grid(row=0, column=3, sticky=W+E)
	self.lang_label.grid(row=1, column=0, sticky=N+S, pady=3)
	self.sentiment.grid(row=1, column=1, sticky=N+S, pady=3)
	self.smiley.grid(row=1, column=2, sticky=E, padx='3 0')
	self.summarizer.grid(row=1, column=3, sticky=W+N+S, padx='7 0')
	self.highlight.grid(row=1, column=3, sticky=E+N+S, padx='0 7')

	# reassign
	bg.image = bg_image
	self.smiley = smiley_image
	self.summarizer = book_image
	self.highlight = hg_image

	# bind
	self.entry.bind('<FocusIn>', self.on_entry_click)
	self.entry.bind('<FocusOut>', self.on_focusout)
	self.entry.bind('<Return>', self.wiki_scraper)
	master.bind ('<Escape>', self.close)

	# config
	self.menu.config(width=7)


    # methods
    def init(self):
	self.high = False
	self.sum = False
	self.ori_text = ''
	self.pro_text = ''
	self.before_sum = ''
	self.url.set(self.message)
	self.language.set('    Language')
	self.sentiment_label.set('  Sentiment')
	return

    def caminit(self):
	self.outputPath = '/home/hadi/Documents/FYP/Picture'
	self.frame = None
	self.thread = None
	self.stopEvent = None
	return

    def cam(self):
	print("[INFO] warming up camera...")
	self.vs = VideoStream(1).start()
	time.sleep(2.0)

	self.window = Toplevel(self.master)
	self.window.geometry("+%d+%d" % (530, 170))
	self.window.panel = None

	btn = ttk.Button(self.window, text="Snapshot!", command=self.takeSnapshot)
	btn.pack(side="bottom", fill="both", expand="yes", padx=10,pady=10)
 
	
	self.stopEvent = threading.Event()
	self.videoLoop()
 

	self.window.wm_title("PyImageSearch PhotoBooth")
	self.window.wm_protocol("WM_DELETE_WINDOW", self.onClose)
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
	textPad.grid(column=0, row=2, columnspan=4, pady=3)
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

	elif value == 'Capture':
		self.cam()

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
	self.entry.delete(0, "end")
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
	lingua = lang.detect_language().capitalize()
	if len(lingua) > 8:
		self.language.set('   ' + lingua)
	else:
		self.language.set('     ' + lingua)

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

	elif self.language.get() != '     English':
		return

	splitter = Splitter()
	postagger = POSTagger()
	splitted_sentences = splitter.split(self.pro_text)
	pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
	dicttagger = DictionaryTagger(['dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])
	dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
	score = sentiment_score(dict_tagged_sentences)
	if score > 1:
		self.sentiment_label.set("    Positive")
	elif score < -1:
		self.sentiment_label.set("   Negative")
	else:
		self.sentiment_label.set("    Neutral")
	return

    def summarize(self):
	self.sum = not self.sum
	if self.sum:
		try:
			summ = summariser(unicode(self.pro_text, 'utf-8'), len(self.pro_text)/50)
		except TypeError:
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

    def videoLoop(self):
	try:
		if not self.stopEvent.is_set():
			time.sleep(0.1)
			self.frame = self.vs.read()
			self.save = self.frame
			self.frame = imutils.resize(self.frame, width=300)
		
			# Convert from BGR order to RGB order
			# Convert to PIL and then ImageTk format
			image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
			image = Image.fromarray(image)
			image = ImageTk.PhotoImage(image)
			
			# if the panel is not None, we need to initialize it
			if self.window.panel is None:
				self.window.panel = ttk.Label(self.window, image=image)
				self.window.panel.image = image
				self.window.panel.pack(side="left", padx=10, pady=10)
		
			# otherwise, simply update the panel
			else:
				self.window.panel.configure(image=image)
				self.window.panel.image = image
 
	except RuntimeError, e:
		print("[INFO] caught a RuntimeError")

	self.window.panel.after(10, self.videoLoop)


    def takeSnapshot(self):
	path = "/home/hadi/Documents/FYP/textract/captured.png"
	cv2.imwrite(path, self.save)
	txt = textract.process(path)
	self.ori_text = txt
	self.pro_text = self.ori_text
	self.update_text(self.pro_text)
	self.lang_detector(self.ori_text)
	print("Image Captured Succesfully")
	self.onClose()


    def onClose(self):
	print("[INFO] closing...")
	self.stopEvent.set()
	self.vs.stop()
	del(self.vs)
	self.window.destroy()
	return


    def close(self, event):
	self.master.quit()
	return
	 

root = Tk()
my_gui = mainGui(root)
root.mainloop()

