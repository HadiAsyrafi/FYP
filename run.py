# -*- coding: utf-8 -*-

# web scraper

from web_scraper import web_scraper

scraper = web_scraper(site = 'Kedah')

txt = scraper.txt

print txt

# lang detector

"""from lang_detector import lang_detect

txt = open('Short Stories/malay.txt', 'r').read()

lang = lang_detect(txt)

#print lang.text

print lang.detect_language()"""

# highlighter

'''from highlighter import highlighter

txt = open('Short Stories/english.txt', 'r').read()

hg = highlighter(txt)

print hg.txt

hg.highlight()'''

# summariser

from summariser import *

#txt = open('Short Stories/english2.txt', 'r').read()

summ = summariser(txt, len(txt)/50)

output = summ.summarize()

print '\n\n'

for data in output['top_n_summary']:
	print data

print '\n\nDivider\n\n'

for data in output['mean_scored_summary']:
	print data


# sentiment analysis

"""from sentiment import *

text = '''What can I say about this place. The staff of the restaurant is nice and the eggplant is not bad. Apart from that, very uninspired food, lack of atmosphere and too expensive. I am a staunch vegetarian and was sorely dissapointed with the veggie options on the menu. Will be the last time I visit, I recommend others to avoid.'''

splitter = Splitter()
postagger = POSTagger()

splitted_sentences = splitter.split(text)
pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

dicttagger = DictionaryTagger([ 'dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])

dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

print sentiment_score(dict_tagged_sentences)"""
