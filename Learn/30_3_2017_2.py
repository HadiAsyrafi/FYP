Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(open('three_sisters.html'))

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/bs4/__init__.py", line 181
    markup_type=markup_type))
UserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("lxml"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 1 of the file <string>. To get rid of this warning, change code that looks like this:

 BeautifulSoup([your markup])

to this:

 BeautifulSoup([your markup], "lxml")

>>> soup
<html>\n<head>\n<title>\n    The Dormouse's story\n   </title>\n</head>\n<body>\n<p class="title">\n<b>\n     The Dormouse's story\n    </b>\n</p>\n<p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>\n<p class="story">\n\t...\n   </p>\n</body>\n</html>\n
>>> prettify()

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    prettify()
NameError: name 'prettify' is not defined
>>> soup.prettify()
u'<html>\n <head>\n  <title>\n   The Dormouse\'s story\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The Dormouse\'s story\n   </b>\n  </p>\n  <p class="story">\n   Once upon a time there were three little sisters; and their names were\n   <a class="sister" href="http://example.com/elsie" id="link1">\n    Elsie\n   </a>\n   ,\n   <a class="sister" href="http://example.com/lacie" id="link2">\n    Lacie\n   </a>\n   and\n   <a class="sister" href="http://example.com/tillie" id="link2">\n    Tillie\n   </a>\n   ; and they \t\tlived at the bottom of a well.\n  </p>\n  <p class="story">\n   ...\n  </p>\n </body>\n</html>\n'
>>> soup = BeautifulSoup(open('three_sisters.html'), 'html.parser')
>>> soup.prettify()
u'<html>\n <head>\n  <title>\n   The Dormouse\'s story\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The Dormouse\'s story\n   </b>\n  </p>\n  <p class="story">\n   Once upon a time there were three little sisters; and their names were\n   <a class="sister" href="http://example.com/elsie" id="link1">\n    Elsie\n   </a>\n   ,\n   <a class="sister" href="http://example.com/lacie" id="link2">\n    Lacie\n   </a>\n   and\n   <a class="sister" href="http://example.com/tillie" id="link2">\n    Tillie\n   </a>\n   ; and they \t\tlived at the bottom of a well.\n  </p>\n  <p class="story">\n   ...\n  </p>\n </body>\n</html>\n'
>>> print soup.prettify()
<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link2">
    Tillie
   </a>
   ; and they 		lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>

>>> soup.find_all(text=re.compile('sisters'))

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    soup.find_all(text=re.compile('sisters'))
NameError: name 're' is not defined
>>> import re
>>> soup.find_all(text=re.compile('sisters'))
[u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t']
>>> soup.find(text=re.compile('sisters'))
u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t'
>>> soup.find_all(string=re.compile('sisters'))
[u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t']
>>> soup.find_all("a", class_="sister")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6

>>> soup.find_all(class_=has_six_characters)
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> css_soup = BeautifulSoup('<p class="body strikeout"></p>')
>>> css_soup.find_all("p", class_="strikeout")
[<p class="body strikeout"></p>]
>>> 

css_soup.select("p.strikeout.body")
[<p class="body strikeout"></p>]
>>> 

css_soup.select("p.body.strikeout")
[<p class="body strikeout"></p>]
>>> soup.find_all(string=["Tillie", "Elsie", "Lacie"])
[u'Elsie', u'Lacie', u'Tillie']
>>> soup.find_all(string=re.compile("Dormouse"))
[u"\n    The Dormouse's story\n   ", u"\n     The Dormouse's story\n    "]
>>> soup.find_all("a", limit=2)
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
>>> soup.html.find_all("title", recursive=False)
[]
>>> soup.find_all("title", recursive=False)
[]
>>> soup.head.find_all("title", recursive=False)
[<title>\n    The Dormouse's story\n   </title>]
>>> a_string = soup.find(string="Lacie")
>>> a_string
u'Lacie'
>>> a_string.find_parents("a")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
>>> a_string.find_parents("p")
[<p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>]
>>> a_string.find_parents("body")
[<body>\n<p class="title">\n<b>\n     The Dormouse's story\n    </b>\n</p>\n<p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>\n<p class="story">\n\t...\n   </p>\n</body>]
>>> a_string.find_parents("p", class="title")
SyntaxError: invalid syntax
>>> a_string.find_parents("p", class_="title")
[]
>>> a_string.find_parents("p", class_="story")
[<p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>]
>>> soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> first_link.find_next_siblings("a")

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    first_link.find_next_siblings("a")
NameError: name 'first_link' is not defined
>>> first_link = soup.a
>>> first_link.find_next_siblings("a")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> first_story_paragraph = soup.find("p", "story")
>>> first_story_paragraph.find_next_sibling("p")
<p class="story">\n\t...\n   </p>
>>> last_link = soup.find("a", id="link3")
>>> last_link.find_previous_siblings("a")

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    last_link.find_previous_siblings("a")
AttributeError: 'NoneType' object has no attribute 'find_previous_siblings'
>>> last_link = soup.find("a", id="link3")
>>> last_link
>>> last_link = soup.find("a")
>>> last_link
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> soup.find("a", id="link3")
>>> soup.find("a", id="link1")
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> soup.find("a", id="link2")
<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
>>> soup.find("a", id="link3")
>>> last_link = soup.find("a", id="link2")
>>> last_link = soup.find("a")
>>> last_link = soup.find("a", id="link2")
>>> last_link.find_previous_siblings("a")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
>>> soup.select('title')
[<title>\n    The Dormouse's story\n   </title>]
>>> soup.select('p')
[<p class="title">\n<b>\n     The Dormouse's story\n    </b>\n</p>, <p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>, <p class="story">\n\t...\n   </p>]
>>> soup.select('p nth-of-type(3)')

Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    soup.select('p nth-of-type(3)')
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1463, in select
    'Unsupported or invalid CSS selector: "%s"' % token)
ValueError: Unsupported or invalid CSS selector: "nth-of-type(3)"
>>> soup.select("body a")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("a body")
[]
>>> soup.select('head title')
[<title>\n    The Dormouse's story\n   </title>]
>>> soup.select('head p')
[]
>>> soup.select('body b')
[<b>\n     The Dormouse's story\n    </b>]
>>> soup,select('body > b')

Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    soup,select('body > b')
NameError: name 'select' is not defined
>>> soup.select('body > b')
[]
>>> soup.select("p > a")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("p > a:nth-of-type(2)")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
>>> soup.select("p > nth-of-type(2)")

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    soup.select("p > nth-of-type(2)")
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1518, in select
    for candidate in _use_candidate_generator(tag):
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1479, in recursive_select
    for i in tag.select(next_token, recursive_candidate_generator):
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1463, in select
    'Unsupported or invalid CSS selector: "%s"' % token)
ValueError: Unsupported or invalid CSS selector: "nth-of-type(2)"
>>> soup.select("p:nth-of-type(3)")
[<p class="story">\n\t...\n   </p>]
>>> soup.select("pnth-of-type(3)")

Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    soup.select("pnth-of-type(3)")
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1463, in select
    'Unsupported or invalid CSS selector: "%s"' % token)
ValueError: Unsupported or invalid CSS selector: "pnth-of-type(3)"
>>> soup.select("p nth-of-type(3)")

Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    soup.select("p nth-of-type(3)")
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 1463, in select
    'Unsupported or invalid CSS selector: "%s"' % token)
ValueError: Unsupported or invalid CSS selector: "nth-of-type(3)"
>>> soup.select("p > #link1")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
>>> soup.select("p > link1")
[]
>>> soup.select("p > #link2")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("p > #sister")
[]
>>> soup.select("p > #http://example.com/elsie")
[]
>>> soup.select("#link1 ~ .sister")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("#link1 + .sister")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
>>> soup.select("#link1 ~ .sister")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("#link2 ~ .sister")
[<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("#link2 + .sister")
[<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("#link2 ~ .sister")
[<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select(".sister")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("#link1")
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
>>> soup.select("a#link2")
[<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> soup.select("p#link2")
[]
>>> soup.select("p.story")
[<p class="story">\n    \tOnce upon a time there were three little sisters; and their names were\n\t<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,\n\t<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and\n\t<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they \t\tlived at the bottom of a well.</p>, <p class="story">\n\t...\n   </p>]
>>> 
