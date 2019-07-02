#!/usr/bin/python3
import csv
import pymysql

data = []

mydb = pymysql.connect(host='127.0.0.1',
    user='root',
    passwd='',
    db='botify')
cursor = mydb.cursor()

with open('database.csv', encoding="utf8") as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csv_data:
        data.append(row)
        #cursor.execute('INSERT INTO Towns(Region Code, Region Name, Code Department, Code District, Code town, Town Name, Population, Average Age) VALUES({}, {}, {}, {}, {}, {}, {}, {})'.format(row))

cursor.execute("CREATE TABLE towns({} INT, {} VARCHAR(255), {} VARCHAR(255), {} INT, {} INT, {} VARCHAR(255), {} float, {} float)".format(data[0][0].replace(" ", "_"), data[0][1].replace(" ", "_"), data[0][2].replace(" ", "_"), data[0][3].replace(" ", "_"), data[0][4].replace(" ", "_"), data[0][5].replace(" ", "_"), data[0][6], data[0][7].replace(" ", "_")))
data.remove(data[0])
data.remove(data[0])

i=0
while i < len(data):
    cursor.execute('INSERT INTO Towns(Region_Code, Region_Name, Code_Department, Code_District, Code_town, Town_Name, Population, Average_Age) VALUES({}, "{}", "{}", {}, {}, "{}", {}, {})'.format(data[i][0].replace("'", ""), data[i][1], data[i][2], data[i][3].replace("'", ""), data[i][4].replace("'", ""), data[i][5], int(data[i][6].replace(",", " ")), data[i][7].replace("'", "")))
    i+=1

mydb.commit()
cursor.close()
print("Done")