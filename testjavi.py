import paramiko
import time

client= paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('192.168.102.1',username='admin',password='ad1847c38')

stdin,stdout,stderr = client.exec_command('expert')
time.sleep(1)
stdin.write('ad1847c38\n')
stdin.flush()
time.sleep(0.1)
stdin.write('\n')
stdin.flush()


for line in stdout.readlines():
    print(line+'\n') 








        
