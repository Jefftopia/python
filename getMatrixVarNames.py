# -*- coding: utf-8 -*-
"""
Created on Wed June 25 2014

@author: jsmith
"""

import xml.etree.ElementTree as ET
import csv

def getMatrixVarNames(xml):

	tree = ET.parse(xml)
	print "tree is", repr(tree)
	
	container = tree.find("variables")
	print "container is", repr(container)
	
	data = []
	for i in container:
		a = i.get("name")			
		l = i.findtext("label")
		data.append([l, a])
	
	with open('labels.csv', 'wb') as csvfile:
		labelWriter = csv.writer(csvfile)
		for i in range(0,len(data)-1):
			labelWriter.writerow(data[i])
	
getMatrixVarNames(raw_input("Select a matrix xml var list:  "))
