#!/bin/bash

if [[ $(/usr/bin/id -u) -ne 0 ]]; then
echo 'Not running as root'
exit
fi

pkill -f runme.sh
pkill -f grgsm_livemon_headless
pkill -f tshark.sh