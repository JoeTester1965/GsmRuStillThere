#!/bin/bash
rm -f scan.txt
rm -f ppm.txt
rm -f start.sh
gain="40"
power_threshold="200000"
kal -g $gain -s 900 > scan.txt
channel_to_get_ppm=`more scan.txt | grep chan: | head -n 1 | cut -c 12-15 | xargs`
kal -g $gain -c $channel_to_get_ppm > ppm.txt
ppm=`tail -n 1 ppm.txt | cut -c 25- | sed 's/.\{4\}$//'`
echo $ppm
kal -g $gain -s 900 -e $ppm > scan.txt
python3 ./process-scanner-output.py scan.txt $ppm $power_threshold > start.sh