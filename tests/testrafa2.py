import paramiko
from paramiko.channel import Channel
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.102.1',username='admin',password='ad1847c38')

channel:Channel = ssh.invoke_shell()
channel_data = str()

while True:
   if channel.recv_ready():
       time.sleep(2)
       channel_data += str(channel.recv(999))
   else:
       continue

   channel.send("expert\n")
   channel.send("ad1847c38\n")
   time.sleep(2)
   channel_data += str(channel.recv(999))

   channel.send("ls\n")
   time.sleep(2)
   channel_data += str(channel.recv(999))
   break

for command in channel_data.split('\\r\\n'):
    print (command)
