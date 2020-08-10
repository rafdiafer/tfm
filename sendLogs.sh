fw log $FWDIR/log/fw.log > $FWDIR/log/exportedLogs/$(date +%Y_%m_%d).log
scp Rafa@192.168.102.2 -i 