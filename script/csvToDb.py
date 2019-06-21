#!/usr/bin/python3

import csv
import pymysql

mydb = pymysql.connect(host='127.0.0.1',
    user='root',
    passwd='',
    db='botify')
cursor = mydb.cursor()
data = []
with open('database.csv', encoding="utf8") as csvfile:
    csv_data = csv.reader(csvfile, quotechar='|')
    for row in csv_data:
        data.append(row)
        #cursor.execute('INSERT INTO Towns(Region Code, Region Name, Code Department, Code District, Code town, Town Name, Population, Average Age) VALUES({}, {}, {}, {}, {}, {}, {}, {})'.format(row))

print(data)
#mydb.commit()
#cursor.close()
print("Done")