#!/usr/bin/python3

import csv
import sqlite3
import sys

from sqlite3 import Error

filename_csv=sys.argv[1]
filename_database=sys.argv[2]

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def main():
    conn = create_connection(filename_database)
    with conn:
        create_table(conn, "CREATE TABLE IF NOT EXISTS mccmnc(mcc int,mccint int,mnc int,mncint int,iso text,country text,countrycode text,network int); ")
        with open(filename_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t MCC: {row[0]},MCC-int: {row[1]},MNC: {row[2]},MNC-int: {row[3]},ISO: {row[4]},Country: {row[5]},Country-Code: {row[6]},Network: {row[7]}')
                    conn.execute('insert into mccmnc values (?,?,?,?,?,?,?,?)', row)
                    line_count += 1
            print(f'Processed {line_count} lines.')
            
if __name__ == '__main__':
    main()
