import urllib2

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib2.urlopen(wiki)  #return HTML file

from bs4 import BeautifulSoup

soup = BeautifulSoup(page)

print soup.title

print soup.title.string




