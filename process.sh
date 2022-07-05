#!/bin/bash

python3 imsi.py imsi.csv mcc-mnc.db > salted-and-hashed-records.csv

rm -f imsi.csv

python3 ./visualise.py salted-and-hashed-records.csv
