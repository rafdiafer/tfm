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








# 1.- y 2.- Si tengo que hacer el comando 'fw log .... ' tengo que hacer un ssh y ejecutar el comando antes de el scp para traerme el archivo de logs
# HACER SSH ADMIN@192.168.102.1, LUEGO EXPERT Y CONTESTAR AL EXPERT CON FABRIC, (mandar script solo si no existe) LUEGO EJECUTAR EL SCRIPT SENDLOGS.SH


