import urllib2
from bs4 import BeautifulSoup

url = "http://www.thestar.com.my/news/nation/2017/03/22/lima-2017-malaysia-officially-receives-its-latest-rmaf-a400m-aircraft/"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "html.parser")

print type(soup)

print soup.prettify()
