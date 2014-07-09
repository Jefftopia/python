# -*- coding: utf-8 -*-
"""
Created on Tue June 17 2014

@author: jsmith
"""

import csv

def readDbCols(vals):

	name = str(vals)

	table = {}
	table['name'] = []
	table['type'] = []
	table['nullable'] = []
	table['default'] = []
	table['description'] = []
	table['#'] = []
	table['drop'] = []

	stanza = '''
	<var name="{0}" precision="1" scale="None" type="{1}">
		<label>{0}</label>
		<description>{3}</description>
		<definition><![CDATA[@{2}({0})]]></definition>
	</var>'''

	dictReader = csv.DictReader(open(vals, 'rb'), fieldnames=['name', 'type', 'nullable', 'default', 'description', '#', 'drop'], delimiter=',', quotechar='"')

	writeDict(dr=dictReader,d=table)

	writeStanzas(d=table,s=stanza,n=name)

def writeDict(dr,d):

	for i in dr:
	    for j in i:
		if j == 'type':
			if i[j] == 'text':
				d[j].append('c')
			elif i[j] == 'boolean':
				d[j].append('l')
			elif i[j] == 'double precision':
				d[j].append('d')
			elif i[j] == 'integer':
				d[j].append('i')
			else:
				d[j].append('NA')
		else:
			d[j].append(i[j])
	return d

def writeStanzas(d,s,n):

	f = open("vars.xml","w")

	for i in range(0,len(d['name'])-1):
		print i,s.format(d['name'][i],d['type'][i],n,d['description'][i])
		f.write(str(s.format(d['name'][i],d['type'][i],n,d['description'][i]) + '\n'))

	f.close()

readDbCols(raw_input("Select a db columns file:  "))
