# -*- coding: utf-8 -*-

# lang detector

'''from lang_detector import lang_detect

txt = open('Short Stories/turkish.txt', 'r').read()

lang = lang_detect(txt)

print lang.text

print lang.detect_language()'''

# highlighter

from highlighter import highlighter

txt = open('Short Stories/english.txt', 'r').read()

hg = highlighter(txt)

print hg.txt

hg.highlight()
