# GSM, are you still there

Uses a  cheap and cheerful [RTL SDR](https://www.rtl-sdr.com/about-rtl-sdr/) to keep a beady eye on when this landmark communications network bites the dust.

Be aware of any legislation regards both passive capture, and the processing, of radio signals where you are.

Be a good citizen and always properly anonymise and/or delete any PII https://en.wikipedia.org/wiki/PII stumbled upon doing network research.

IMHO that includes IP addresses as well, but that is another story.

## Dependancies

rtl_sdr

[gr-gsm](https://osmocom.org/projects/gr-gsm/wiki/Installation)

python3-matplotlib

python3-pandas

[mcc-mnc table](https://raw.githubusercontent.com/musalbas/mcc-mnc-table/master/mcc-mnc-table.csv)

## Setup

python3 make-mcc-mnc-db.py ./mcc-mnc-table.csv mcc-mnc.db


## Survey

#
# Get the averge ppm (frequency deviation) for your dongle to help grgsm_scanner etc lock on:
#

```console
rtl_test -p
```

#
# Find candidate stations, and put them in a file for processing, will take a few minutes
#

grgsm_scanner -g 40 -s 2000000 -b GSM900 -p ppm > towers.txt


#
# Using towers found above, create a shell script that will process them, --args are for a networked receiver
#

```console
python3 ./process-scanner-output.py towers.txt ppm --args=rtl_tcp=a.b.c.d:1234 > start.sh
```

## Scan

to start:

```console
sudo bash ./start.sh
```

to stop:

```console
sudo bash ./stop.sh
```

## Results

```console
python3 ./imsi.py ./imsi.csv ./mcc-mnc.db > salted-and-hashed-records.csv

rm imsi.csv

python3 ./visualise.py salted-and-hashed-records.csv
```

![!](./mcccount.png "")

![!](./mnccount.png "")

![!](./msintop20.png "")