# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:40:08 2017

@author: amar.lad
"""

import sqlite3

# SQLITE database details
airportdelay = 'airportdelay'
connection1 = sqlite3.connect('{}.db'.format(airportdelay))
c1 = connection1.cursor()


# SQLITE database details
weather = 'Weather'
connection2 = sqlite3.connect('{}.db'.format(weather))
c2 = connection2.cursor()


# Create database table
def create_table():
    c1.execute("""CREATE TABLE IF NOT EXISTS airportweather (metar TEXT, year TEXT, mon TEXT, mday TEXT, ahour TEXT, amin TEXT, tzname TEXT, tempm TEXT, tempi TEXT, dewptm TEXT, dewpti TEXT, hum TEXT, vism TEXT, visi TEXT, conds TEXT, icon TEXT, fog TEXT, rain TEXT, snow TEXT, hail TEXT, thunder TEXT, tornado TEXT)""")

# SQL insert      
def sql_insert(to_db):
    try:
        c1.execute("INSERT INTO airportweather VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (to_db)) 
        connection1.commit()
    except Exception as e:
        print('s0 insertion',str(e))
        
# main function 
if __name__ == "__main__":
    create_table()
    
    sql = 'select * from airportweather'
    c2.execute(sql)
    records = c2.fetchall()
    cnt = 0
    for record in records:
        to_db = record
        try:
            cnt += 1
            sql_insert(to_db)            
        except:
            print('error:' + str(cnt))
    print('completed' + str(cnt))
            
            
            

