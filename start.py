#!/usr/bin/python3.6

import sys
import subprocess
import os
from pathlib import Path
import random

# format
if len(sys.argv) != 5:
    print('Format: start.py path/to/uris/files pass_admin_gw ip_address_server ip_fw\n')
    sys.exit()

os.system("pyfiglet CheckScript")

print("INFORMATION: This script uses four different scripts to throw day-one attacks to a server \
and, using a Checkpoint FW, get logs and stats from it, comparing which ones have been detected \
as attacks and which ones not. \n\n")

uri_file_out = "launch_uri"
pass_admin_gw = sys.argv[2]

print("Let's start!\n")

# dos bucles for para mandar a generator y launcher todos los archivos de uris a lanzar
for path in Path(sys.argv[1]).iterdir():
    if path.is_file():
        #one random number for the resulting files' name, so the dont replace them
        random_number = random.randint(0,9999)
        #print(random_number)
        
        try:
            subprocess.call(['python3', 'generator.py', path, uri_file_out, str(random_number)])
        except:
            print("generator.py error")

        try:
            subprocess.call(['python3', 'launcher.py', uri_file_out, sys.argv[3], str(random_number)])
        except:
            print("launcher.py error")

        try:
            subprocess.call(['python3', 'analyzer.py', pass_admin_gw, sys.argv[4], sys.argv[3], str(random_number)])
        except:
            print("analyzer.py error")

        try:
            subprocess.call(['python3' ,'comparer.py', uri_file_out, str(random_number)])
        except:
            print("comparer.py error")

print("FINISH\n")
