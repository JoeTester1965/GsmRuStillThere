# GSM, are you still there

Uses a  cheap and cheerful [RTL SDR](https://www.rtl-sdr.com/about-rtl-sdr/) to keep a beady eye on when this landmark communications network bites the dust.

Be aware of any legislation regards both passive capture, and the processing, of radio signals where you are.

Be a good citizen and always properly anonymise and/or delete any [Personally Identifiable Information](https://en.wikipedia.org/wiki/Personal_data) stumbled upon doing network research.

IMHO that includes IP addresses as well, but that is another story.

## Dependancies

[rtl_sdr](https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/)

[gr-gsm](https://osmocom.org/projects/gr-gsm/wiki/Installation)

[mcc-mnc table](https://raw.githubusercontent.com/musalbas/mcc-mnc-table/master/mcc-mnc-table.csv)

[python3-matplotlib](https://matplotlib.org/stable/faq/installing_faq.html)

[python3-pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

## Setup

```console
python3 make-mcc-mnc-db.py mcc-mnc-table.csv mcc-mnc.db
```


## Survey

Get the averge ppm (frequency deviation) for your dongle to help the scripts below (i.e. replace {your ppm} below with the numeric value you get here). Using 0 should work most of the time if your RTL dongle is a decent one.

```console
rtl_test -p
```
Alternatively use [kalibrate-rtl](http://314256.blogspot.com/2015/03/how-to-use-kal-software-to-workout-ppm.html) to find the ppm.

Find downlinks and put them in a file for processing, will take a few minutes:

```console
grgsm_scanner -g 40 -s 2000000 -b GSM900 -p {your ppm} > towers.txt
```

Using downlinks found above, create a shell script that will process them. --args are optional and for a networked receiver.

```console
python3 ./process-scanner-output.py towers.txt {your ppm} --args=rtl_tcp=a.b.c.d:1234 > start.sh
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
python3 imsi.py imsi.csv mcc-mnc.db > salted-and-hashed-records.csv

rm imsi.csv

python3 ./visualise.py salted-and-hashed-records.csv
```

![!](./mcccount.png "")

![!](./mnccount.png "")

![!](./msintop20.png "")
