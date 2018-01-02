# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:40:08 2017

@author: amar.lad
"""

import sqlite3
import datetime

# SQLITE database details
airportdelay = 'Weather'
connection = sqlite3.connect('{}.db'.format(airportdelay))
c = connection.cursor()


# Create database table
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS airportweatherdatetime (metar TEXT, year TEXT, mon TEXT, mday TEXT, ahour TEXT, amin TEXT, tzname TEXT, tempm TEXT, tempi TEXT, dewptm TEXT, dewpti TEXT, hum TEXT, vism TEXT, visi TEXT, conds TEXT, icon TEXT, fog TEXT, rain TEXT, snow TEXT, hail TEXT, thunder TEXT, tornado TEXT, city TEXT, adatetime TIMESTAMP)""")
    c.execute("""CREATE TABLE IF NOT EXISTS airportdatadatetime (YEAR TEXT, MONTH TEXT, DAY_OF_MONTH TEXT, DAY_OF_WEEK TEXT, FL_DATE TEXT, UNIQUE_CARRIER TEXT, AIRLINE_ID TEXT, CARRIER TEXT, ORIGIN_AIRPORT_ID TEXT, ORIGIN_AIRPORT_SEQ_ID TEXT, ORIGIN_CITY_MARKET_ID TEXT, ORIGIN TEXT, ORIGIN_CITY_NAME TEXT, ORIGIN_STATE_ABR TEXT, ORIGIN_STATE_FIPS TEXT, ORIGIN_STATE_NM TEXT, ORIGIN_WAC TEXT, DEST_AIRPORT_ID	TEXT, DEST_AIRPORT_SEQ_ID TEXT,	DEST_CITY_MARKET_ID TEXT, DEST TEXT, DEST_CITY_NAME TEXT, DEST_STATE_ABR TEXT, DEST_STATE_FIPS TEXT, DEST_STATE_NM TEXT, DEST_WAC TEXT, CRS_DEP_TIME TEXT, DEP_TIME TEXT, DEP_DELAY TEXT, DEP_DELAY_NEW TEXT, CRS_ARR_TIME TEXT, ARR_TIME TEXT, ARR_DELAY TEXT, ARR_DELAY_NEW TEXT, CANCELLED TEXT, CANCELLATION_CODE TEXT, DIVERTED TEXT, CRS_ELAPSED_TIME TEXT, ACTUAL_ELAPSED_TIME TEXT, AIR_TIME TEXT, DISTANCE TEXT, CARRIER_DELAY TEXT, WEATHER_DELAY TEXT, NAS_DELAY TEXT, SECURITY_DELAY TEXT, LATE_AIRCRAFT_DELAY TEXT, ADATETIME TIMESTAMP)""")

# SQL insert      
def sql_insert1(to_db):
    try:
        c.execute("INSERT INTO airportweatherdatetime VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (to_db)) 
        connection.commit()
    except Exception as e:
        print('s0 insertion',str(e))
  
# SQL insert      
def sql_insert2(to_db):
    try:
        c.executemany("INSERT INTO airportdatadatetime VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (to_db)) 
        connection.commit()
    except Exception as e:
        print('s0 insertion',str(e))
                
# main function 
if __name__ == "__main__":
    create_table()
    
    sql = 'select * from airportweather'
    c.execute(sql)
    records = c.fetchall()
    cnt = 0
    for record in records:
        to_db = record
        city = to_db[0][7:10]
        to_db = to_db + (city,)
        adatetime = datetime.datetime(int(to_db[1]), int(to_db[2]), int(to_db[3]), int(to_db[4]), 0, 0)
        to_db = to_db + (adatetime,)
        try:
            cnt += 1
            sql_insert1(to_db)            
        except:
            print('error:' + str(cnt))
    print('completed' + str(cnt))
    
    sql = 'select * from airportdata'
    c.execute(sql)
    records = c.fetchall()
    cnt = 0
    to_indb = []
    for record in records:
        to_db = record
        dtime = to_db[27]
        dday = to_db[2]
        if dtime == '':
            dtime = '0000'
        if dtime == '2400':
            dtime = '2359'
        dtime = dtime[0:2] + '00'    
        ddelay = to_db[28]
        if ddelay == '':
            ddelay = '0'

        
        adate = datetime.datetime(int(to_db[0]), int(to_db[1]), int(dday), 0, 0, 0).date()
        atime = datetime.datetime.strptime(dtime, '%H%M').time()
        adatetime = datetime.datetime.combine(adate, atime)
        adatetime = adatetime - datetime.timedelta(minutes=int(float(ddelay)))
        to_db = to_db + (adatetime,)
        to_indb.append(to_db)
    try:
        cnt += 1
        sql_insert2(to_indb)            
    except:
        print('error:' + str(cnt))
    print('completed' + str(cnt))
        
connection.close()
    
    