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
        create_table(conn, "CREATE TABLE IF NOT EXISTS mccmnc(mcc int,mnc int,country text, operator text); ")
        with open(filename_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    conn.execute("INSERT INTO mccmnc (mcc, mnc, country, operator) VALUES (?, ?, ?, ?)", (row[0],row[1],row[4],row[6]))
                    line_count += 1
            
if __name__ == '__main__':
    main()
