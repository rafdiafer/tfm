#!/usr/bin/python3.6
import sys
import re

# format
if len(sys.argv) != 3:
    print ('Format: generator.py file-raw.uri file-out.uri')
    sys.exit()

print("Preparing URI files to launch them...")
try:
    file_uri = open(sys.argv[1], 'r')
except IOError:
    print ('File does not exist')

string_uri = file_uri.read()
re.sub('.*[\ ]', '', string_uri)

file_out = open(sys.argv[2], 'w')
file_out.write(string_uri)

file_uri.close()
file_out.close()