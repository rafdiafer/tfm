import sys
import re
from datetime import datetime

# format
if len(sys.argv) != 5:
    print('Format: generator.py file.log pass_admin_gw')
    sys.exit()

DIR_LOG = '$FWDIR/log/'
IP = '192.168.103.2'
USER_SEC_GW = 'admin'
PASS_SEC_GW = sys.arg[2]

# 1.- y 2.- Si tengo que hacer el comando 'fw log .... ' tengo que hacer un ssh y ejecutar el comando antes de el scp para traerme el archivo de logs

# 3.-
try:
    acceptedTraffic = False
    deniedTraffic = False

    with open(sys.argv[1], 'r') as file:
        for line in file:
            lineArray = line.split(';')

            if lineArray[0].find('accept'):
                acceptedTraffic = True
            elif lineArray[0].find('deny'):
                deniedTraffic = True

            if acceptedTraffic == True:
                cleanDir = open('results/clean.clean', 'a')
                cleanDir.write(lineArray[0]) # only URI + timestamp
                cleanDir.close
            elif deniedTraffic == True:
                attacksUris = open('results/attacks.attacks', 'a')
                attacksUris.write(lineArray[0]) # only URI + timestamp
                attacksUris.close

                attacksInfo = open('results/attacksInfo.attacks', 'a')
                attacksInfo.write(lineArray[0]) # URI + timestamp
                attacksInfo.write(lineArray[17]) # rule name
                attacksInfo.write(lineArray[8]) # source ip
                attacksInfo.write(lineArray[9] + '\n') # destination
                attacksInfo.close

except IOError:
    print('File does not exist')

# tengo que coger los logs del firewall:
#   1.- meterme en el checkpoint y volcar 'fw log $FWDIR/log/nombredelarchivo.log' en un archivo
#   2.- traerme con scp el archivo
#   3.- analizar qué log es clean y cual attack, separarlos en dos archivos distintos, con su url y un pequeño resumen (regla, timestamp...)
