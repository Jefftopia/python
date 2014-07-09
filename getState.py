# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 17:47:59 2014

@author: jsmith
"""

import xml.etree.ElementTree as ET

def getState(xml):
	tree = ET.parse(xml)
	root = tree.getroot()
	namespace = "{http://escmatrix.com/schema/deploytools}"
	modules = []

	for i in root.findall(".//{0}label".format(namespace)):
		modules.append(i.text)
		print i.text
		
	printState(modules)  
  
def printState(modules):
	f = open("server_state.txt","w")
	for i in modules:
		f.write(str(i + '\n'))

	f.close()

getState(raw_input("Select a deployment xml file:  "))
