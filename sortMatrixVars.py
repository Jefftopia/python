# -*- coding: utf-8 -*-
"""
Created on Wed June 25 2014

@author: jsmith
"""

import xml.etree.ElementTree as ET

def sortMatrixVars(xml):

	tree = ET.parse(xml)
	print "tree is", repr(tree)
	
	container = tree.find("variables")
	print "container is", repr(container)
	
	data = []
	for i in container:
		key = i.findtext("label")
		data.append((key, i))

	data.sort()

	container[:] = [i[-1] for i in data]

	tree.write("sorted_vars.xml")

sortMatrixVars(raw_input("Select a matrix xml var list:  "))
