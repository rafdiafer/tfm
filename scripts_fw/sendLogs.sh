FECHA=$(date +%Y_%m_%d)
fw log $FWDIR/log/fw.log >> $FWDIR/log/exportLogs/${FECHA}.log
scp $FWDIR/log/exportLogs/${FECHA}.log dit@192.168.102.3:/home/dit/tfm/logs/${FECHA}.log
rm $FWDIR/log/exportLogs/${FECHA}.log