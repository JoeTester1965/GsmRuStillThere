#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
echo 'Not running as root'
exit
fi

pkill -f -9 grgsm_livemon_headless
pkill -f tshark
pkill -f start.sh
