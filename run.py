# -*- coding: utf-8 -*-

import textract

# web scraper

'''from web_scraper import web_scraper

scraper = web_scraper(site = 'lenz\'s law')

txt = scraper.txt

print txt'''

# lang detector

'''from lang_detector import lang_detect

txt = textract.process("Short Stories/english.txt")

#txt = open('Short Stories/malay.txt', 'r').read()

lang = lang_detect(txt)

#print lang.text

print lang.detect_language()'''

# highlighter

'''from highlighter import highlighter

txt = textract.process("Short Stories/english.txt")

hg = highlighter(txt)

print hg.txt

hg.highlight()'''

# summariser

'''from summariser import *

txt = textract.process("Short Stories/english2.txt")

summ = summariser(txt, len(txt)/50)

output = summ.summarize()

print '\n\n'

for data in output['top_n_summary']:
	print data

print '\n\nDivider\n\n'

for data in output['mean_scored_summary']:
	print data'''


# sentiment analysis

'''from sentiment import *

txt = textract.process("Review/malaysia.txt")

print txt

splitter = Splitter()
postagger = POSTagger()

splitted_sentences = splitter.split(txt)
pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

dicttagger = DictionaryTagger(['dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])

dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

print sentiment_score(dict_tagged_sentences)'''
