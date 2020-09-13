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
    i = 0

    with open(sys.argv[1], 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            
            set2 = set(line)

            if len(set_especiales.intersection(set2)) > 0:
                print(line)
                line = urllib.parse.quote(line)
            
            launch_url = URL + line
            print(launch_url)
            try:
                req = requests.get(launch_url, verify=False, timeout=5)
                #print(req.status_code)
                time.sleep(1)
            except:
                print("\n") #Catching connection refused by peer exception
                i = i+1

except IOError:
    print('File does not exist')

print("Rejected connections by server: "+str(i)+"\n")
file.close()