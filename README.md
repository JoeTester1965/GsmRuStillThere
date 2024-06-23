# GSM, are you still there

Uses a  cheap and cheerful [RTL SDR](https://www.rtl-sdr.com/about-rtl-sdr/) to keep a beady eye on when this landmark communications network bites the dust.

Be aware of any legislation regards both passive capture, and the processing, of radio signals where you are.

Be a good citizen and always properly anonymise and/or delete any [Personally Identifiable Information](https://en.wikipedia.org/wiki/Personal_data) stumbled upon doing network research.

A post-processing script is provided for that purpose.

## Install dependancies

Tested on Ubuntu 22.04 64bit and Raspberry Pi Debian version: 12 (bookworm) 64bit.

``` console
apt-get install git gnuradio rtl-sdr git cmake libosmocore-dev gr-osmosdr tshark wireshark

pip3 install python-dateutil pandas matplotlib

git clone https://github.com/bkerler/gr-gsm
cd gr-gsm
mkdir build
cd build
cmake ..
mkdir $HOME/.grc_gnuradio/ $HOME/.gnuradio/
make
sudo make install
sudo ldconfig

sudo apt-get install libtool libfftw3-dev librtlsdr-dev
git clone https://github.com/steve-m/kalibrate-rtl.git
cd kalibrate-rtl
./bootstrap
CXXFLAGS='-W -Wall -O3' ./configure
make
sudo make install

```

## Setup (do this in directory you installed GSMRuStillThere)

```console
wget https://s3.amazonaws.com/mcc-mnc.net/mcc-mnc.csv
python3 make-mcc-mnc-db.py mcc-mnc.csv mcc-mnc.db
```

## Survey

Two scans are made, the first to get an accurate RTL error offset and the next the GSM base stations proper. 

This script then creates **start.sh** to allow capture of IMSI data.

```console
bash ./survey.sh
```
Note: A **gain** value of **40** in *survey.sh* worked best for me, you may need to change this. With this value, for me, rx power as indicated by the output file *scan.txt* needed to be greater than **100000** for consistent decoding. You may need to edit **power_threshold** in *survey.sh* to be either larger or smaller to reflect your environment. Alternatively if you are comfortable with bash scripts, run with a small power threshold then edit *start.sh* manually after it has been created by *survey.sh*.

## Scan

This script loops through all found base stations gathering IMSI data from each one for 5 minutes into *imsi.csv*. Root user is needed for tshark hence sudo. 

```console
sudo bash ./start.sh
```

Note for advanced users: If you want to use a networked or specific USB RTL SDR receiver other than the default one edit *start.sh* and add **--args=rtl_tcp=a.b.c.d:1234** etc to the **grgsm_livemon_headless** command lines as appropriate.

To live view signalling in tshark or wireshark, use:

``` console
sudo tshark -i lo -Y gsmtap
sudo wireshark -k -f udp -Y gsmtap -i lo
```

To stop collecting press Control-C then:

```console
sudo bash ./stop.sh
```

## Processing

Run the following to anonymise the IMSI data collected and produce visualisations like the examples below:

```console
bash ./process.sh
```

![!](./mcccount.png "")

![!](./mnccount.png "")

![!](./msintop20.png "")
