#!/usr/bin/python3.6

import sys
import os
from pathlib import Path

i = 0
j = 0

results = open('resultados.txt','w+')

for path in Path(sys.argv[1]).iterdir():
	if path.is_file():
		with open(path, 'r') as file:
			for line in file:
				i = i + 1
				print(i)

		numeroUris = i - j
		results.write(str(path) + ': ' + str(numeroUris) + '\n')
		j = i

results.write('TOTAL: ' + str(i))