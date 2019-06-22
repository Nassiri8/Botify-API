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
    csv_data = csv.reader(csvfile, quotechar='|')
    for row in csv_data:
        print(row)
        #data.append(row)
        #cursor.execute('INSERT INTO Towns(Region Code, Region Name, Code Department, Code District, Code town, Town Name, Population, Average Age) VALUES({}, {}, {}, {}, {}, {}, {}, {})'.format(row))

#cursor.execute("CREATE TABLE towns(id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, {} INT, {} VARCHAR(255), {} INT, {} INT, {} INT, {} VARCHAR(255), {} float, {} float)".format(data[1][0], data[1][1], data[1][2], data[1][3], data[1][4], data[1][5], data[1][6], data[1][7]))
#data.remove(data[0])
#data.remove(data[0])
#while i < len(data):
    #data[i][6].replace('"', '')
    #cursor.execute('INSERT INTO Towns(region_code, region_name, dept_code, distr_code, code, name, population, average_age) VALUES({}, "{}", {}, {}, {}, "{}", {}, {})'.format(int(data[i][0]), data[i][1], int(data[i][2]), int(data[i][3]), int(data[i][4]), data[i][5], float(data[i][6]), float(data[i][7])))
    #i+=1

print("Done")