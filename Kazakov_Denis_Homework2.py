#Denis Kazakov, CSCI 4502, 102298967
import numpy as np
import matplotlib.pyplot as plt
import sys
import re

arguments = sys.argv
data = open(arguments[1], "r")
data_rows = []
for i,dataLine in enumerate(data):
	if (i>2):
		data_rows.append(dataLine.split(','))
print data_rows [2]
regex = re.compile(r"^\"[0-9]*\.[0-9]*\"",re.IGNORECASE)
for line in data_rows:
	for word in line:
		word = regex.sub(r'\1', word)
		print word
print data_rows [2]
columns = zip(*data_rows) #{1,2,3} + {4,5,6} => {(1,4),(2,5),(3,6)}



##1
#print normalized valued of Volume: v(i) = v(i)/v_max-v_min
