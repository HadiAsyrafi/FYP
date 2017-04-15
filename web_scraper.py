import urllib2
from bs4 import BeautifulSoup

text = ""

url = "file:///home/hadi/Documents/FYP/Automatic%20summarization%20-%20Wikipedia.html"

page = urllib2.urlopen(url)			
soup = BeautifulSoup(page, "html.parser")	

#soup = BeautifulSoup(open('three_sisters.html'), 'html.parser')
#content_text = soup.body

soup.table.extract()

title = soup.head.title
print title.string

text = ""

content_text = soup.find('div', id = 'mw-content-text')

def find_string(tag, store):
	for child in tag.children:

		if child.string is None :
			store = find_string(child, store)

		else:
			store = store + unicode(child.string)
		
	return store

text = find_string(content_text, text)

print text
