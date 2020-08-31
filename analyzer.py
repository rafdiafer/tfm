#!/usr/bin/python3.6
import sys
import re
from datetime import datetime
import paramiko
from paramiko.channel import Channel
import time

# format
if len(sys.argv) != 3:
    print('Format: analyzer.py pass_admin_gw ip_fw')
    sys.exit()

IP = str(sys.argv[2])
USER_SEC_GW = 'admin'
PASS_SEC_GW = str(sys.argv[1])

# 1.- y 2.- Si tengo que hacer el comando 'fw log .... ' tengo que hacer un ssh y ejecutar el comando antes de el scp para traerme el archivo de logs
# HACER SSH ADMIN@192.168.102.1, LUEGO EXPERT Y CONTESTAR AL EXPERT CON FABRIC, (mandar script solo si no existe) LUEGO EJECUTAR EL SCRIPT SENDLOGS.SH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(IP,username=USER_SEC_GW,password=PASS_SEC_GW)

channel:Channel = ssh.invoke_shell()
channel_data = str()

while True:
   if channel.recv_ready():
       time.sleep(2)
       channel_data += str(channel.recv(999))
   else:
       continue

   channel.send("expert\n")
   channel.send(PASS_SEC_GW + "\n")
   time.sleep(2)
   channel_data += str(channel.recv(999))

   channel.send("./sendLogs.sh\n")
   time.sleep(2)
   channel_data += str(channel.recv(999))
   time.sleep(20)
   break

for command in channel_data.split('\\r\\n'):
    print (command)

# 3.-   
try:
    acceptedTraffic = False
    deniedTraffic = False
    time_log = time.strftime("%Y_%m_%d")

    with open(time_log, 'r') as file:
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
