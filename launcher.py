#!/usr/bin/python3.6
import sys
import re
import requests
import time
import urllib.parse

# format
if len(sys.argv) != 3:
    print('Format: launcher.py file.uri ip_server')
    sys.exit()

# constants
IP_SERVER = sys.argv[2]
URL = 'http://' + IP_SERVER
date = time.strftime("%d_%m_%y")

# launch attacks (http requests)
print("Launching attacks...\n")
try:
    caracteres_especiales = ";,`+\'"
    set_especiales = set(caracteres_especiales)

    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            
            set2 = set(line)

            if len(set_especiales.intersection(set2)) > 0:
                print(line)
                #line = urllib.parse.quote(line)
            
            print(line)
            launch_url = URL + line
            try:
                req = requests.get(launch_url, verify=false, timeout=2)
                print(req.status_code)
            except:
                print("")

            time.sleep(0.1)
except IOError:
    print('File does not exist')

file.close()