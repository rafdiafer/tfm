#import subprocess
import pexpect

#p = subprocess.Popen("ssh admin@192.168.102.1 'expert'", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
#p.stdin.write("ad1847c38")

mypassword = 'ad1847c38'

child = pexpect.spawn("ssh admin@192.168.102.1 'expert'")
child.expect("This system is for authorized use only.\r\n\radmin@192.168.102.1's password: ")
child.sendline(mypassword)
child.expect("\r\nEnter expert password:")
child.sendline(mypassword)
child.command('./sendLogs.sh')