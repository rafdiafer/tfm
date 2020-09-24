#!/usr/bin/python3.6
import sys
import re
import time

# format
if len(sys.argv) != 4:
    print ('Format: generator.py file-raw.uri file-out.uri randomnum')
    sys.exit()

print("Preparing URI files to launch them...")

time_log = time.strftime("%Y_%m_%d")
randomnum = sys.argv[3]
path_uris_file = str(sys.argv[2]) + '_'+ time_log + '_' + randomnum + '.uri'

file_out = open(path_uris_file, 'a')

try:
	with open(sys.argv[1], 'r') as file:
		for line in file:
			new_line = line.split('/', 1)
			if len(new_line) == 2:
				file_out.write('/' + str(new_line[1]))
except IOError:
    print ('File does not exist')

file_out.close()