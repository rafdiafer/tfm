#!/usr/bin/python3.6
import sys
import re
import os.path
import time
import urllib.parse

if len(sys.argv) != 5:
    print('Format: comparelines.py file_to_compare_1 file_to_compare_2 name_coincide_file folder')
    sys.exit()

nombre_coincide_file = sys.argv[4] + '/coincide_' + sys.argv[3] + '.txt'
coincide_file = open(nombre_coincide_file, 'w+')
nombre_no_coincide_file = sys.argv[4] + '/no_coincide_' + sys.argv[3] + '.txt'
no_coincide_file = open(nombre_no_coincide_file, 'w+')
contador_coincide = 0
contador_no_coincide = 0
file1 = sys.argv[1]
file2 = sys.argv[2]

try:
	with open(file1, 'r') as uris1:
		for uri in uris1:

			uri = uri.replace("http://192.168.103.2/","")

			tam_uri = len(uri)
			if len(uri) < 60:
				N = tam_uri - 1
			else:
				N = 60 # only compares the 100 first chars of the uri

			uri = uri[0:N]
			found = False

			with open(file2, 'r') as uris2:
				for compareuri in uris2:
					if found == False:
						if compareuri.find(uri) > 0:
							found = True 
						else:
							found = False

				if found == False:
					contador_no_coincide = contador_no_coincide + 1
					no_coincide_file.write(uri+'\n')
				else:
					contador_coincide = contador_coincide + 1
					coincide_file.write(uri+'\n')

	results_coincide = '\nTOTAL = '+ str(contador_coincide)
	coincide_file.write(results_coincide)
	results_no_coincide = '\nTOTAL = '+str(contador_no_coincide)
	no_coincide_file.write(results_no_coincide)

except IOError:
	print('File does not exist')