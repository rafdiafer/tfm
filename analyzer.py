#!/usr/bin/python3.6
import sys
import re
from datetime import datetime
import paramiko
from paramiko.channel import Channel
import time
import os.path

# format
if len(sys.argv) != 4:
    print('Format: analyzer.py pass_admin_gw ip_fw ip_server')
    sys.exit()

IP = str(sys.argv[2])
IP_SERVER = str(sys.argv[3])
USER_SEC_GW = 'admin'
PASS_SEC_GW = str(sys.argv[1])

# Using Paramiko module SSH client to login to fw's expert mode and get the fw logs file
print("Taking log files from the firewall...\n")
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
    print("Just wait a minute while preparing the log file...\n")
    time.sleep(60)
    break

#for command in channel_data.split('\\r\\n'):
    #print (command)

# Now that we have the log file in local, we analyze the logs
time_log = time.strftime("%Y_%m_%d")
#time_log = "2020_09_04"
print(time_log)
file_log = "logs/" + time_log + '.log'
print(file_log)
contador_lineas_vacias = 1

path_attacks_file = 'results/attacks_'+time_log+'.attacks'
path_attacks_info_file = 'results/attacksInfo_'+time_log+'.attacks'
append_or_write_1 = 'a'
append_or_write_2 = 'a'

# indexes for printing in files
indexURI = 0
indexSeverity = 0
indexAttackInfo = 0
indexProtectionName = 0
indexMalwareRule = 0

if os.path.isfile(path_attacks_file):
    append_or_write_1 = 'w'
if os.path.isfile(path_attacks_info_file):
    append_or_write_2 = 'w'

print("Analyzing logs...\n")
try:
    with open(file_log, 'r') as file:
        for line in file:
            lineArray = line.split(';')

            # it can happen to be pair and be a Date, so we need to skip this one
            if lineArray[0].find("Date: ") < 0:
                # We only take IPS prevent logs
                if lineArray[0].find('prevent') > 0:
                    print("Dropped traffic | IPS blade")

                    # to find which is the index where the information can be found
                    i = 0
                    for item in lineArray:
                        if item.find("resource") > 0:
                            indexURI = i
                        if item.find("Attack Info") > 0:
                            indexAttackInfo = i
                        if item.find("Protection Name") > 0:
                            indexProtectionName = i
                        if item.find("Severity") > 0:
                            indexSeverity = i
                        if item.find("malware_rule_id") > 0:
                            indexMalwareRule = i
                        i = i + 1

                    lineArray[indexURI] = lineArray[indexURI].replace(' resource: ', '')
                    lineArray[indexMalwareRule] = lineArray[indexMalwareRule].replace('malware_rule_id', 'Malware rule ID')

                    # writing only urls in this file
                    attacksUris = open('results/attacks_'+time_log+'.attacks', append_or_write_1)
                    attacksUris.write(lineArray[indexURI]+'\n') # only URI
                    attacksUris.close

                    # writing urls and their info in this file
                    attacksInfo = open('results/attacksInfo_'+time_log+'.attacks', append_or_write_2)
                    attacksInfo.write(" URL: "+lineArray[indexURI] +'\n')
                    attacksInfo.write(lineArray[indexAttackInfo] +'\n') # Attack info
                    attacksInfo.write(lineArray[indexProtectionName] +'\n') # Protection name
                    attacksInfo.write(lineArray[indexSeverity] +'\n') # Severity
                    attacksInfo.write(lineArray[indexMalwareRule] + '\n\n') # Malware rule ID
                    attacksInfo.close

                    # next iteration of the loop, we need to 'append' in the files, not to 'write', so the other info won't be lost
                    append_or_write_1 = 'a'
                    append_or_write_2 = 'a'

except IOError:
    print('File does not exist')