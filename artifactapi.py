# -*- coding: utf-8 -*-
"""
Created on Wed JUL 02 2014

@author: jsmith
"""

import requests
import json

#def getJSON():

	


#def parseJSON():


r = requests.get('https://artifactory.escmatrix.com/artifactory/simple/libs-release-local/com/esc/dummy/1.1.0/dummy-1.1.0.pom', auth=('jsmith', 'Taiasw0rd1'))
print r
