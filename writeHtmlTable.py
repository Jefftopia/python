# -*- coding: utf-8 -*-
"""
Created on Wed June 25 2014

@author: jsmith
"""

import xml.etree.ElementTree as ET
import csv

def readCSV(spreadsheet):

	name = str(spreadsheet)

	table = {}
	table['label'] = []
	table['var'] = []
	table['description'] = []

	stanza1 = '''
	<li><a href="{0}">{1}</a></li>
	'''

	stanza2 = '''
	<div id="{0}">{1}</div>
	'''

	dictReader = csv.DictReader(open(vals, 'rb'), fieldnames=['label', 'var','description'], delimiter=',', quotechar='"')

	writeDict(dr=dictReader,d=table)

	writeStanzas(d=table,s=stanza,n=name)
 
def writeDict(dr,d):

	for i in dr:
	    for j in i:
		d[j].append(i[j])

	return d

def writeStanzas(d,s,n):

	f = open("vars.xml","w")

	for i in range(0,len(d['name'])-1):
		print i,s.format(d['name'][i],d['type'][i],n)
		f.write(str(s.format(d['name'][i],d['type'][i],n) + '\n'))

	f.close()

readCSV(raw_input("Select a layout file:  "))
