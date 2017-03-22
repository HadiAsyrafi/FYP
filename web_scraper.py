import urllib2
from bs4 import BeautifulSoup

url = "http://www.thestar.com.my/news/nation/2017/03/22/lima-2017-malaysia-officially-receives-its-latest-rmaf-a400m-aircraft/"

page = urllib2.urlopen(url)	#query website and return html

soup = BeautifulSoup(page)	#parse html in BS format

#print soup.prettify()		#look at html structure

#print soup.script

#print soup.find_all("p")

all_para = soup.find_all("div")
for para in all_para:
	print para
