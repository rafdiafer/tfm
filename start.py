#!/usr/bin/python3.6

import sys
import subprocess
import os

# format
if len(sys.argv) != 5:
    print('Format: start.py file_raw_uri.uri pass_admin_gw ip_address_server ip_fw\n')
    sys.exit()

os.system("pyfiglet CheckScript")

print("INFORMATION: This script uses four different scripts to throw day-one attacks to a server \
and, using a Checkpoint FW, get logs and stats from it, comparing which ones have been detected \
as attacks and which ones not. \n\n")

uri_file_out = "launch_uri.uri"
pass_admin_gw = sys.argv[2]

print("Let's start!\n")
try:
    subprocess.call(['python3', 'generator.py', sys.argv[1], uri_file_out])
except:
    print("generator.py error")

try:
    subprocess.call(['python3', 'launcher.py', uri_file_out, sys.argv[3]])
except:
    print("launcher.py error")

try:
    subprocess.call(['python3', 'analyzer.py', pass_admin_gw, sys.argv[4], sys.argv[3]])
except:
    print("analyzer.py error")

try:
    subprocess.call(['python3' ,'comparer.py', uri_file_out])
except:
    print("comparer.py error")

print("FINISH\n")