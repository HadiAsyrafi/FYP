# -*- coding: utf-8 -*-
import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

class lang_detect(object):

	def __init__ (self, txt = 'None'):

		self.text = txt


	def _calculate_languages_ratios(self):
	    

	    languages_ratios = {}

	    tokens = wordpunct_tokenize(self.text)
	    self.words = [word.lower() for word in tokens]

	    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
	    for language in stopwords.fileids():
	    # [danish, dutch, english, finnish, french, german, hungarian, italian, norwegian, portuguese, spanish, swedish, turkish]

		stopwords_set = set(stopwords.words(language))
		words_set = set(self.words)
		common_elements = words_set.intersection(stopwords_set)

		languages_ratios[language] = len(common_elements)

	    return languages_ratios


	def _calculate_malay_language_ratios(self, languages_ratios):
	    
	    with open("malay_stopwords.txt") as f:
	    	stopwords_set = set(f.read().splitlines())

	    #stopwords_set = set(open("malay_stopwords.txt").readlines())
	    words_set = set(self.words)
	    common_elements = words_set.intersection(stopwords_set)
	    languages_ratios['malay'] = len(common_elements)
	    return languages_ratios


	def detect_language(self):
	

	    ratios = self._calculate_languages_ratios()
	    ratios = self._calculate_malay_language_ratios(ratios)
	    most_rated_language = max(ratios, key=ratios.get)

	    return most_rated_language
