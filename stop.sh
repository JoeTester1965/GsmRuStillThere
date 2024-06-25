#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
echo 'Not running as root'
exit
fi

nohup pkill -f grgsm_livemon_headless &> /dev/null
nohup pkill -f -9 grgsm_livemon_headless &> /dev/null
nohup pkill -f tshark &> /dev/null
nohup pkill -f start.sh &> /dev/null