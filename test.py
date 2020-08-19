import subprocess

p = subprocess.Popen("ssh admin@192.168.102.1 'expert'", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p.stdin.write("ad1847c38")