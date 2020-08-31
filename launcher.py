#!/usr/bin/python3.6
import sys
import re
import requests
import time

# format
if len(sys.argv) != 4:
    print('Format: launcher.py file.uri dir_out_time ip_server')
    sys.exit()

# constants
IP_SERVER = sys.argv[3]
URL = 'http://' + IP_SERVER

# launch attacks (http requests)
try:
    print(sys.argv[1])
    dir_timestamp = open(sys.argv[2], 'a')

    with open(sys.argv[1], 'r') as file:
        for linea in file:
            launch_url = URL + linea
            req = requests.get(launch_url)

            # save timestamp + uris
            times = time.strftime("%H:%M:%S")
            print(times)

            uri_and_time = times + linea
            dir_timestamp.write(uri_and_time)
            time.sleep(0.1)
except IOError:
    print('File does not exist')

file.close()
dir_timestamp.close()