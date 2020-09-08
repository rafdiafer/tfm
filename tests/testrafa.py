import sys
import re
import time

file_log = "log_prueba.txt"


try:
	with open(file_log, 'r') as file:
		for line in file:
			numero = 0
			lineArray = line.split(';')
			print("Número 0 URI + TIMESTAMP: "+lineArray[0])
			print("Número 17 RULE NAME: "+lineArray[17])
			print("Número 8 SOURCE IP: "+lineArray[8])
			print("Número 9 DESTINATION: "+lineArray[9])
			print("\n------------------------------------------------------------------\n")
			for i in lineArray:
				print("Número "+str(numero)+" : "+i)
				numero = numero +1

			print("\n..................................................................\n")

except IOError:
	print('File does not exist')








        
