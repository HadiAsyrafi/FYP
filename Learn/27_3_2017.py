Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup(three_sisters.html, 'html.parser')

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    soup = BeautifulSoup(three_sisters.html, 'html.parser')
NameError: name 'three_sisters' is not defined
>>> soup = BeautifulSoup(open('three_sisters.html'))
>>> head_tag = soup.head
>>> head_tag
<head>
<title>
    The Dormouse's story
   </title>
</head>
>>> head_tag.contents
[u'\n', <title>
    The Dormouse's story
   </title>, u'\n']
>>> head_tag.contents[0]
u'\n'
>>> head_tag.contents[1]
<title>
    The Dormouse's story
   </title>
>>>  head_tag.contents[2]
 
  File "<pyshell#8>", line 1
    head_tag.contents[2]
    ^
IndentationError: unexpected indent
>>> soup.contents
[<html>
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
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
</html>, u'\n']
>>> soup.contents[0]
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
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
</html>
>>> soup.contents[1]
u'\n'
>>> soup.contents[2]

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    soup.contents[2]
IndexError: list index out of range
>>> soup.contents[0].name
'html'
>>> soup.contents[1].name

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    soup.contents[1].name
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 667, in __getattr__
    self.__class__.__name__, attr))
AttributeError: 'NavigableString' object has no attribute 'name'
>>> for child in title_tag.children:
	print child

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    for child in title_tag.children:
NameError: name 'title_tag' is not defined
>>> for child in head_tag.children:
	print child

	


<title>
    The Dormouse's story
   </title>


>>> for child in soup.children:
	print child

	
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
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
</html>


>>> for child in head_tag.descendants:
	print child

	


<title>
    The Dormouse's story
   </title>

    The Dormouse's story
   


>>> head_tag.string
>>> title_tag = head_tag.contents
>>> title_tag
[u'\n', <title>
    The Dormouse's story
   </title>, u'\n']
>>> title_tag = head_tag.contents[1]
>>> title_tag
<title>
    The Dormouse's story
   </title>
>>> title_tag.string
u"\n    The Dormouse's story\n   "
>>> title_tag.comtents
>>> title_tag.contents
[u"\n    The Dormouse's story\n   "]
>>> title_tag.contents[0]
u"\n    The Dormouse's story\n   "
>>> type(title_tag.contents[0])
<class 'bs4.element.NavigableString'>
>>> soup.string
>>> print soup.string
None
>>> for string in soup.string:
	print string

	

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    for string in soup.string:
TypeError: 'NoneType' object is not iterable
>>> for string in soup.strings:
	print string

	





    The Dormouse's story
   









     The Dormouse's story
    





    	Once upon a time there were three little sisters; and their names were
	
Elsie
,
	
Lacie
and
	
Tillie
; and they 		lived at the bottom of a well.



	...
   






>>> for string in soup.string:
	print repr(string)

	

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for string in soup.string:
TypeError: 'NoneType' object is not iterable
>>> for string in soup.strings:
	print repr(string)

	
u'\n'
u'\n'
u"\n    The Dormouse's story\n   "
u'\n'
u'\n'
u'\n'
u'\n'
u"\n     The Dormouse's story\n    "
u'\n'
u'\n'
u'\n    \tOnce upon a time there were three little sisters; and their names were\n\t'
u'Elsie'
u',\n\t'
u'Lacie'
u'and\n\t'
u'Tillie'
u'; and they \t\tlived at the bottom of a well.'
u'\n'
u'\n\t...\n   '
u'\n'
u'\n'
u'\n'
>>> for string in soup.stripped_strings:
	print repr(string)

	
u"The Dormouse's story"
u"The Dormouse's story"
u'Once upon a time there were three little sisters; and their names were'
u'Elsie'
u','
u'Lacie'
u'and'
u'Tillie'
u'; and they \t\tlived at the bottom of a well.'
u'...'
>>> link = soup.a
>>> link
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> for parent in link.parents:
	if parent is None:
		print parent

		
>>> for parent in link.parents:
	if parent is None:
		print parent
	else:
		print parent.name

		
p
body
html
[document]
>>> for parent in link.parents:
	print parent

	
<p class="story">
    	Once upon a time there were three little sisters; and their names were
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<body>
<p class="title">
<b>
     The Dormouse's story
    </b>
</p>
<p class="story">
    	Once upon a time there were three little sisters; and their names were
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
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
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
</html>
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
	<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
	<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>and
	<a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>; and they 		lived at the bottom of a well.</p>
<p class="story">
	...
   </p>
</body>
</html>

>>> for parent in link.parents:
	print parent.name

	
p
body
html
[document]
>>> sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
>>> print sibling_soup.prettify
<bound method BeautifulSoup.prettify of <html><body><a><b>text1</b><c>text2</c></a></body></html>>
>>> print sibling_soup.prettify()
<html>
 <body>
  <a>
   <b>
    text1
   </b>
   <c>
    text2
   </c>
  </a>
 </body>
</html>
>>> sibling_soup.b
<b>text1</b>
>>> sibling_soup.b.next_sibling
<c>text2</c>
>>> import re
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
    
>>> import reimport re
SyntaxError: invalid syntax
>>> import re
>>> for tag in soup.find_all(re.compile("^b")):
    print(tag.name)

    
body
b
>>> soup.find_all(["a", "b"])
[<b>
     The Dormouse's story
    </b>, <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> for tag in soup.find_all(True):
    print(tag.name)

    
html
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
>>> tag
<p class="story">
	...
   </p>
>>> def has_class_but_no_id(soup):
	return soup.has_attr('class') and not soup.has_attr('id')

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
>>> 
