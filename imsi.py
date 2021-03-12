import sys
import csv
import sqlite3
import hashlib
import uuid
from dateutil.parser import parse
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

filename_csv=sys.argv[1]
filename_database=sys.argv[2]

def main():
    salt = uuid.uuid4().hex.encode('utf-8')
    conn = create_connection(filename_database)
    with conn:
        with open(filename_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    try:
                        timestamp = row[1]
                        mcc = row[0][0:3]
                        mnc = row[0][3:5]  
                        msin = hashlib.sha256(row[0][5:].encode('utf-8') + salt).hexdigest()[-10:]
                        datetime = parse(timestamp)
                        cursor = conn.cursor()
                        cursor.execute('select distinct country,network from mccmnc where mcc=? and mnc=?', (mcc, mnc))
                        records=cursor.fetchall()
                        if len(records) > 0:
                            country=records[0][0]
                            network=records[0][1]
                            print(f'{datetime},{msin},{mcc},{mnc},{country},{network}')
                        line_count += 1
                    except:
                        pass
            
if __name__ == '__main__':
    main()
