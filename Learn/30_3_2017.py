Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(open('three_sisters.html'))
>>> def has_class_but_no_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')

>>> soup.find_all(has_class_but_no_id)
[<p class="title">
<b>
     The Dormouse's story
    </b>
</p>, <p class="story">
    	Once upon a time there were three little sisters; and their names were
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>, <p class="story">
	...
   </p>]
>>> def not_lacie(href):
	return href and not re.compile("lacie").search(href)

>>> soup.find_all(href=not_lacie)

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    soup.find_all(href=not_lacie)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1126, in find_all
    return self._find_all(name, attrs, text, limit, generator, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 427, in _find_all
    found = strainer.search(i)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1276, in search
    found = self.search_tag(markup)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1248, in search_tag
    if not self._matches(attr_value, match_against):
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1314, in _matches
    return match_against(markup)
  File "<pyshell#10>", line 2, in not_lacie
    return href and not re.compile("lacie").search(href)
NameError: global name 're' is not defined
>>> import re
>>> soup.find_all(href=not_lacie)
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.find_all(not_lacie)

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    soup.find_all(not_lacie)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1126, in find_all
    return self._find_all(name, attrs, text, limit, generator, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 427, in _find_all
    found = strainer.search(i)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1276, in search
    found = self.search_tag(markup)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1232, in search_tag
    or (markup and self._matches(markup, self.name))
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1314, in _matches
    return match_against(markup)
  File "<pyshell#10>", line 2, in not_lacie
    return href and not re.compile("lacie").search(href)
TypeError: expected string or buffer
>>> soup.find_all(not_lacie)

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    soup.find_all(not_lacie)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1126, in find_all
    return self._find_all(name, attrs, text, limit, generator, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 427, in _find_all
    found = strainer.search(i)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1276, in search
    found = self.search_tag(markup)
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1232, in search_tag
    or (markup and self._matches(markup, self.name))
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1314, in _matches
    return match_against(markup)
  File "<pyshell#10>", line 2, in not_lacie
    return href and not re.compile("lacie").search(href)
TypeError: expected string or buffer
>>> for tag in soup.find_all(re.compile("t")):
    print(tag.name)

    
html
title
>>> tag
<title>
    The Dormouse's story
   </title>
>>> isinstance(tag.next_element, NavigableString)

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    isinstance(tag.next_element, NavigableString)
NameError: name 'NavigableString' is not defined
>>> form bs4 import NavigableString
SyntaxError: invalid syntax
>>> from bs4 import NavigableString
>>> isinstance(tag.next_element, NavigableString)
True
>>> def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

>>> for tag in soup.find_all(surrounded_by_strings):
    print tag.name

    
head
title
body
p
b
p
a
a
a
p
>>> for tag in soup.find_all(re.compile("t")):
    print(tag.name)

    
html
title
>>> for tag in soup.find_all(surrounded_by_strings):
    print tag.name

    
head
title
body
p
b
p
a
a
a
p
>>> soup.find_all("title")
[<title>
    The Dormouse's story
   </title>]
>>> soup.find_all('title')
[<title>
    The Dormouse's story
   </title>]
>>> soup.find_all("p", 'title')
[<p class="title">
<b>
     The Dormouse's story
    </b>
</p>]
>>> soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.find_all(id='link2')
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.find(string=re.compile("sisters"))
>>> import re
>>> soup.find(string=re.compile("sisters"))
>>> soup.find_all(string=re.compile("sisters"))
[]
>>> soup.find(string=re.compile("a"))
>>> print soup.find(string=re.compile("a"))
None
>>> string = re.compile("a")
>>> string
<_sre.SRE_Pattern object at 0x7fc03bc51ad0>
>>> soup.find(string)
<head>
<title>
    The Dormouse's story
   </title>
</head>
>>> soup.find(string)
<head>
<title>
    The Dormouse's story
   </title>
</head>
>>> soup.find(string=re.compile("a"))
>>> soup.find(string)
<head>
<title>
    The Dormouse's story
   </title>
</head>
>>> soup.find(string=re.compile("sisters"))
>>> soup.find_all(href=re.compile("elsie"))
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
>>> type (href)

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    type (href)
NameError: name 'href' is not defined
>>> re.compile('elsie')
<_sre.SRE_Pattern object at 0x7fc033ff5be8>
>>> soup.find_all(href=re.compile("elsie"), id='link1')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
>>> data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
>>> data_soup.find_all(data-foo="value")
SyntaxError: keyword can't be an expression
>>> data_soup.find_all(attrs={"data-foo": "value"})
[<div data-foo="value">foo!</div>]
>>> soup.find(string=re.compile("sisters"))
>>> soup.find(string=re.compile("it"))
>>> pprint(soup.find_all(text=re.compile("sisters")))

Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    pprint(soup.find_all(text=re.compile("sisters")))
NameError: name 'pprint' is not defined
>>> soup.find_all(text=re.compile("sisters"))
[u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t']
>>> soup.find_all(string=re.compile("sisters"))
[]
>>> soup.find_all("a", "class")
[]
>>> soup.find_all('p', 'title')
[<p class="title">
<b>
     The Dormouse's story
    </b>
</p>]
>>> soup.find_all("a", "sister")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.find_all("a", class='sister')
SyntaxError: invalid syntax
>>> soup.find_all("a", class_='sister')
[]
>>> soup.find_all("a", class_="sister")
[]
>>> soup.find_all("a")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> import celery

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    import celery
ImportError: No module named celery
>>> import re
>>> print(re.__version__)
2.2.1
>>> print(bs4.__version__)

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(bs4.__version__)
NameError: name 'bs4' is not defined
>>> print(BeautifulSoup.__version__)

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    print(BeautifulSoup.__version__)
AttributeError: type object 'BeautifulSoup' has no attribute '__version__'
>>> BeautifulSoup.version

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    BeautifulSoup.version
AttributeError: type object 'BeautifulSoup' has no attribute 'version'
>>> from bs4 import BeautifulSoup
>>> soup.find_all(text=re.compile('sisters'))
[u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t']
>>> soup.find_all(string=re.compile('sisters'))
[]
>>> soup.find_all(re.compile('sisters'))
[]
>>> soup.find(string=re.compile('sisters'))
>>> 
