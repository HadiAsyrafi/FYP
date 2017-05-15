# -*- coding: utf-8 -*-

import textract
import glob
from lang_detector import lang_detect

counter = 0
lang_cnt = 0
hit = 0
miss = 0

language = ['danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'malay', 'norwegian', 'portuguese', 'spanish', 'swedish', 'turkish']

lst = glob.glob("/home/hadi/Documents/FYP/Short Stories/*.txt")

for item in sorted(lst):

	txt = textract.process(item)
	lang = lang_detect(txt)
	result = lang.detect_language()
	print item + '    ' + result + '\n'
	print language[lang_cnt]
	if result == language[lang_cnt]:
		hit += 1

	else:
		miss += 1

	counter += 1

	if counter > 4:
		counter = 0
		lang_cnt += 1

	print 'Hit = {}, Miss = {} \n\n'.format(hit, miss)

print 'Accuracy = {0:.2f}%'.format((hit/float(hit+miss))*100)
