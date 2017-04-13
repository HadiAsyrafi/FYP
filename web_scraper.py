import urllib2
from bs4 import BeautifulSoup

text = ""

url = "https://en.wikipedia.org/wiki/Guy_Fawkes"

page = urllib2.urlopen(url)			#query website and return html

soup = BeautifulSoup(page, "html.parser")	#parse html in BS format

#soup = BeautifulSoup(open('three_sisters.html'), 'html.parser')

soup.table.extract()

title = soup.head.title
print title.string

text = ""

#body_content = soup.find_all('div', id = 'bodyContent')

content_text = soup.find('div', id = 'mw-content-text')
		
#content_text = soup.body

def find_string(tag, store):
	for child in tag.children:

		if child.string is None :
			store = find_string(child, store)

		else:
			store = store + unicode(child.string)
		
	return store

text = find_string(content_text, text)

print text
