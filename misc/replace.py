# coding: UTF-8
#!/usr/bin/python
# coding: UTF-8

import re
import sys
import os

import codecs

files = os.listdir()
for file in files:
	rst = re.compile(".rst")
	if rst.search(file):
		read_file = None
		write_file = None
		temp_file = "temp_file"
		try:
		    read_file = codecs.open(file, 'r', 'UTF-8')
		    write_file = codecs.open(temp_file, 'w', 'UTF-8')
		    for line in read_file:
		        if line.find('%5C') != -1:
		            line = line.replace('%5C', '\\')
		        write_file.write(line)
		finally:
		    read_file.close()
		    write_file.close()

		if os.path.isfile(file) and os.path.isfile(temp_file):
		    os.remove(file)
		    os.rename(temp_file, file)
	
	else:
		pass