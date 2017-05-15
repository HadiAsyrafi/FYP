# -*- coding: utf-8 -*-

import textract
import glob
from summariser import *

lst = glob.glob("/home/hadi/Documents/FYP/English text/*.txt")

result = 0

for item in sorted(lst):

	total = 0
	print item

	txt = textract.process(item)
	actual = len(txt)

	summ = summariser(txt, len(txt)/50)
	output = summ.summarize()

	for data in output['mean_scored_summary']:
		#print data
		total = total + len(data)

	percent = (float(actual - total)/actual)*100

	result = result + percent

	print 'Actual = {}, Summarised = {}'.format(actual, total)
	print "% of summ = {0:.2f}%".format(percent)

print 'Average = {0:.2f}%'.format(result/10)
