# TFM: CheckScript

This script (start.py) uses four different scripts to throw zero day attacks to a server and, using a Checkpoint FW, getting logs and stats from it, comparing which ones have been detected as attacks and which ones not.

To execute start.py script:

``` python3 start.py file_raw_uri.uri pass_admin_gw ip_address_server ip_fw```

### Generator.py
It prepares the URIs to be launched to the Apache server, returning a launch_uri.uri file.

### Launcher.py
It launches the URIs to the Apache server using the Requests module.

### Analyzer.py
It uses the Paramiko module to enter the firewall and bypass the ssh connection and expert mode password to execute one script that will send the logs from the fw to us. For more info about that script, see "sendLogs.sh". 

Then, the logs file is analyzed and the ones that have been detected will be written in two different files: Attacks_${DATE}.attacks (with only URIs) and AttacksInfo_${DATE}.attacks (with URIs and more info).

### Comparer.py
It compares all the URIs that have been launched with the Attacks_${DATE}.attacks file, so the ones that have not been detected are written in the Clean_${DATE}.clean file. Then, it shows the number of detected and accepted URIs.

### sendLogs.sh
It's a shell script that has already been sent to the firewall. It makes log files readable ("fw log" command), creates a file with the readable logs, sends it to our system (using "scp") and deletes the file. 

The scp command execution is possible without introducing any password because ssh keys are being used.
