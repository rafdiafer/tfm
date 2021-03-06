#!/usr/bin/python3.6
import sys
import re
import os.path
import time
import urllib.parse


# Hacer la comparación entre 'results/attacks_'+log_file+'.attacks' con el primer ficher de URIs 'launch_uri.uri'
# Lo que encuentre (las URLs que coincidan), seran las que ha detectado como ataques. Las que no se hayan encontrado
# habrá que mandarlas al directorio de results/clean_....., pues no habrán sido detectadas como ataques.

if len(sys.argv) != 4:
    print('Format: comparer.py file_uri randomnum path_uris')
    sys.exit()

time_log = time.strftime("%Y_%m_%d")
#time_log = "2020_09_04"
randomnum = sys.argv[2]
path_clean = '/run/media/dit/588160b2-d0b0-410c-8e0e-4d2f43ca8bdf/resultadostfm/results/clean_' + time_log + '_' + randomnum + '.clean'
file_uri = sys.argv[1] + '_' + time_log + '_' + randomnum + '.uri'
file_log = '/run/media/dit/588160b2-d0b0-410c-8e0e-4d2f43ca8bdf/resultadostfm/results/attacks_' + time_log + '_' + randomnum + '.attacks'
path_uris = sys.argv[3]
#caracteres_especiales = ";,`+\'"
#set_especiales = set(caracteres_especiales)

counter_accepted_uris = 0
counter_prevent_uris = 0
counter_total_uris = 0

append_or_write = 'a+'
if os.path.isfile(path_clean):
    append_or_write = 'w+'

try:
	with open(file_uri, 'r') as uris:
		for uri in uris:
			counter_total_uris = counter_total_uris + 1

			tam_uri = len(uri)
			if len(uri) < 60:
				N = tam_uri - 1
			else:
				N = 60 # only compares the 100 first chars of the uri

			uri = uri[0:N]
			#uri = uri.rstrip('\n')
			#set2 = set(uri)
			#if len(set_especiales.intersection(set2)) > 0:
				#uri = urllib.parse.quote(uri)

			already_found = False

			with open(file_log, 'r') as logs:
				for log in logs:
	    			#it will only be comparing uris with logs if it has not been found yet
					if already_found is False:
						if log.find(uri) > 0:
							# uri matches attack log, so it has been detected by the fw
							already_found = True
							counter_prevent_uris = counter_prevent_uris + 1

			if already_found is False:
	        	# if it is still not found, it means that traffic has been accepted by the fw
				cleanDir = open(path_clean, append_or_write)
				cleanDir.write(uri + '\n') # only URI + timestamp
				cleanDir.close

				append_or_write = 'a'
				counter_accepted_uris = counter_accepted_uris + 1
except IOError:
	print('File does not exist')

print("\nRESULTS:\n")
totalUrisStr = "Number of launched URIs: "+ str(counter_total_uris) + " | "
print(totalUrisStr)
totalAcceptedStr = "Number of accepted URIs: "+ str(counter_accepted_uris) + " | "
print(totalAcceptedStr)
totalDeniedUris = "Number of detected attacks: "+ str(counter_prevent_uris) + "\n"
print(totalDeniedUris)

finalResults = open('finalResults/finalResults.txt', 'a+')
finalResults.write(path_uris + ':\n')
finalResults.write(totalUrisStr)
finalResults.write(totalAcceptedStr)
finalResults.write(totalDeniedUris + '\n')