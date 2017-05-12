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
	    words = [word.lower() for word in tokens]

	    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
	    for language in stopwords.fileids():
	    # [danish, dutch, english, finnish, french, german, hungarian, italian, norwegian, portuguese, spanish, swedish, turkish]

		stopwords_set = set(stopwords.words(language))
		words_set = set(words)
		common_elements = words_set.intersection(stopwords_set)

		languages_ratios[language] = len(common_elements)

	    return languages_ratios


	def detect_language(self):
	

	    ratios = self._calculate_languages_ratios()

	    print ratios

	    most_rated_language = max(ratios, key=ratios.get)

	    return most_rated_language
