Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup('<b class="boldest">Extremely Bold!</b>')
>>> tag = soup.b
>>> type(tag)
<class 'bs4.element.Tag'>
>>> tag.name
'b'
>>> tag
<b class="boldest">Extremely Bold!</b>
>>> tag.name = "blockquote"
>>> tag
<blockquote class="boldest">Extremely Bold!</blockquote>
>>> tag.name
'blockquote'
>>> tag.name = "b"
>>> tag['class']
['boldest']
>>> tag.attrs
{'class': ['boldest']}
>>> tag['class'] = 'Very bold'
>>> tag['id'] = 1
>>> tag
<b class="Very bold" id="1">Extremely Bold!</b>
>>> del tag['id']
>>> tag['class']
'Very bold'
>>> tag['id']

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tag['id']
  File "/usr/local/lib/python2.7/dist-packages/bs4/element.py", line 879, in __getitem__
    return self.attrs[key]
KeyError: 'id'
>>> css_soup = BeautifulSoup('<p class="body strike"></p>')
>>> ccss_soup.p

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    ccss_soup.p
NameError: name 'ccss_soup' is not defined
>>> css_soup.p
<p class="body strike"></p>
>>> css_soup.p['class']
['body', 'strike']
>>> rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
>>> rel_soup.a['rel']
['index']
>>> rel_soup.a['rel'] = ['index', 'contents']
>>> rel_soup.a['rel']
['index', 'contents']
>>> rel_soup.a
<a rel="index contents">homepage</a>
>>> tag.string
u'Extremely Bold!'
>>> type(tag.string)
<class 'bs4.element.NavigableString'>
>>> tag.string.replace_with("No longer bold")
u'Extremely Bold!'
>>> tag
<b class="Very bold">No longer bold</b>
>>> markup = "<b><! --Hey, buddy. How are you?--></b>"
>>> soup = BeautifulSoup(markup)
>>> comment = soup.b.string
>>> type(comment)
<type 'NoneType'>
>>> type(soup.b.string)
<type 'NoneType'>
>>> markup
'<b><! --Hey, buddy. How are you?--></b>'
>>> soup
<html><body><b></b></body></html>
>>> soup.b
<b></b>
>>> markup
'<b><! --Hey, buddy. How are you?--></b>'
>>> markup = "<b><!--Hey, buddy. How are you?--></b>"
>>> soup = BeautifulSoup(markup)
>>> soup
<html><body><b><!--Hey, buddy. How are you?--></b></body></html>
>>> comment = soup.b.string
>>> type(comment)
<class 'bs4.element.Comment'>
>>> comment
u'Hey, buddy. How are you?'
>>> soup.b.prettify()
u'<b>\n <!--Hey, buddy. How are you?-->\n</b>'
>>> print(soup.b.prettify())
<b>
 <!--Hey, buddy. How are you?-->
</b>
>>> from bs4 import CData
>>> cdata = CData("A CDATA block")
>>> comment.replace_with(cdata)
u'Hey, buddy. How are you?'
>>> print(soup.b.prettify())
<b>
 <![CDATA[A CDATA block]]>
</b>
>>> soup = BeautifulSoup(three_sisters.html, 'html.parser')

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    soup = BeautifulSoup(three_sisters.html, 'html.parser')
NameError: name 'three_sisters' is not defined
>>> soup = BeautifulSoup(open(three_sisters.html))

Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    soup = BeautifulSoup(open(three_sisters.html))
NameError: name 'three_sisters' is not defined
>>> soup = BeautifulSoup(open('three_sisters.html'))
>>> soup
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
    ; and they lived at the bottom of a well.
   </p>
<p class="story">
    ...
   </p>
</body>
</html>

>>> soup.prettify()
u'<html>\n <head>\n  <title>\n   The Dormouse\'s story\n  </title>\n </head>\n <body>\n  <p class="title">\n   <b>\n    The Dormouse\'s story\n   </b>\n  </p>\n  <p class="story">\n   Once upon a time there were three little sisters; and their names were\n   <a class="sister" href="http://example.com/elsie" id="link1">\n    Elsie\n   </a>\n   ,\n   <a class="sister" href="http://example.com/lacie" id="link2">\n    Lacie\n   </a>\n   and\n   <a class="sister" href="http://example.com/tillie" id="link2">\n    Tillie\n   </a>\n   ; and they lived at the bottom of a well.\n  </p>\n  <p class="story">\n   ...\n  </p>\n </body>\n</html>\n'
>>> print(soup.prettify())
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
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>

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
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>

>>> soup.head
<head>
<title>
    The Dormouse's story
   </title>
</head>
>>> soup.body.b
<b>
     The Dormouse's story
    </b>
>>> soup.a
<a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>
>>> soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>, <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>]
>>> print soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">
     Elsie
    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
     Lacie
    </a>, <a class="sister" href="http://example.com/tillie" id="link2">
     Tillie
    </a>]
>>> soup = BeautifulSoup(open('three_sisters.html'))
>>> soup.a
<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
>>> soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> print soup.find_all('a')
[<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link2">Tillie</a>]
>>> 
