import urllib2
import re
from bs4 import BeautifulSoup

class web_scraper(object):
	
	def __init__ (self, site = 'Wikipedia'):

		url = "https://en.wikipedia.org/wiki/" + site
		page = urllib2.urlopen(url)			
		soup = BeautifulSoup(page, "html.parser")	

		soup.find(id = 'toc').extract()

		for tag in soup('table'):
			tag.extract()

		for tag in soup(role = 'note'):
			tag.extract()

		for tag in soup(class_ = 'chart'):
			tag.extract()

		for tag in soup(class_ = 'mw-editsection'):
			tag.extract()

		for tag in soup('sup'):
			tag.extract()

		for tag in soup(class_ = "thumb"):
			tag.extract()

		for tag in soup(string = re.compile("See also:")):
			tag.extract()


		self.title = soup.find(id = 'firstHeading').string

		text = ""
		content_text = soup.find('div', id = 'mw-content-text')
		self.txt = self.find_string(content_text, text)

	def find_string(self, tag, store):

		for child in tag.children:

			if child.string is None :
				store = self.find_string(child, store)

			else:
				string = unicode(child.string)
				if (string == "See also") or (string == "References"):
					break;
				store = store + string
		
		return store
