import sys
import re
import requests
from datetime import time

# format
if len(sys.argv) != 3:
    print('Format: generator.py file.uri dir_out_time')
    sys.exit()

# constants
URL = 'http://192.168.103.2'

# launch attacks (http requests)
try:
    with open(sys.argv[1], 'r') as file:
        for linea in file:
            launch_url = URL + linea
            req = requests.get(launch_url)

            # save timestamp + uris
            dir_timestamp = open(sys.argv[2], 'a')
            time = time()
            print(time)

            uri_and_time = time + linea
            dir_timestamp.write(uri_and_time)

except IOError:
    print('File does not exist')

file.close
dir_timestamp.close