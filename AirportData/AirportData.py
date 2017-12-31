# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:22:22 2017

@author: amar.lad
"""
import csv
import sqlite3

# SQLITE database details
airportdelay = 'airportdelay'
connection = sqlite3.connect('{}.db'.format(airportdelay))
c = connection.cursor()

csvfiles = '1032683730_T_ONTIME_' 
path = 'C:/Users/amar.lad/Downloads/Aviation/'

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS airportdata (YEAR TEXT, MONTH TEXT, DAY_OF_MONTH TEXT, DAY_OF_WEEK TEXT, FL_DATE TEXT, UNIQUE_CARRIER TEXT, AIRLINE_ID TEXT, CARRIER TEXT, ORIGIN_AIRPORT_ID TEXT, ORIGIN_AIRPORT_SEQ_ID TEXT, ORIGIN_CITY_MARKET_ID TEXT, ORIGIN TEXT, ORIGIN_CITY_NAME TEXT, ORIGIN_STATE_ABR TEXT, ORIGIN_STATE_FIPS TEXT, ORIGIN_STATE_NM TEXT, ORIGIN_WAC TEXT, DEST_AIRPORT_ID	TEXT, DEST_AIRPORT_SEQ_ID TEXT,	DEST_CITY_MARKET_ID TEXT, DEST TEXT, DEST_CITY_NAME TEXT, DEST_STATE_ABR TEXT, DEST_STATE_FIPS TEXT, DEST_STATE_NM TEXT, DEST_WAC TEXT, CRS_DEP_TIME TEXT, DEP_TIME TEXT, DEP_DELAY TEXT, DEP_DELAY_NEW TEXT, CRS_ARR_TIME TEXT, ARR_TIME TEXT, ARR_DELAY TEXT, ARR_DELAY_NEW TEXT, CANCELLED TEXT, CANCELLATION_CODE TEXT, DIVERTED TEXT, CRS_ELAPSED_TIME TEXT, ACTUAL_ELAPSED_TIME TEXT, AIR_TIME TEXT, DISTANCE TEXT, CARRIER_DELAY TEXT, WEATHER_DELAY TEXT, NAS_DELAY TEXT, SECURITY_DELAY TEXT, LATE_AIRCRAFT_DELAY TEXT)""")

# SQL insert      
def sql_insert(to_db):
    try:
        c.executemany("INSERT INTO airportdata VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (to_db)) 
        connection.commit()
    except Exception as e:
        print('s0 insertion',str(e))


# main function 
if __name__ == "__main__":
    create_table()
    
    for months in range (1, 13):
        filename = path + csvfiles + str(months) + '.csv'
        with open (filename, 'r') as csvfile:
            # csv.DictReader uses first line in file for column headings by default
            # comma is default delimiter
            dr = csv.DictReader(csvfile) 
            for i in dr:
                to_db = [(i['YEAR'], i['MONTH'] , i['DAY_OF_MONTH'] , i['DAY_OF_WEEK'] , i['FL_DATE'] , i['UNIQUE_CARRIER'] , i['AIRLINE_ID'] , i['CARRIER'] , i['ORIGIN_AIRPORT_ID'] , i['ORIGIN_AIRPORT_SEQ_ID'] , i['ORIGIN_CITY_MARKET_ID'] , i['ORIGIN'] , i['ORIGIN_CITY_NAME'] , i['ORIGIN_STATE_ABR'] , i['ORIGIN_STATE_FIPS'] , i['ORIGIN_STATE_NM'] , i['ORIGIN_WAC'] , i['DEST_AIRPORT_ID'] , i['DEST_AIRPORT_SEQ_ID'] , i['DEST_CITY_MARKET_ID'] , i['DEST'] , i['DEST_CITY_NAME'] , i['DEST_STATE_ABR'] , i['DEST_STATE_FIPS'] , i['DEST_STATE_NM'] , i['DEST_WAC'] , i['CRS_DEP_TIME'] , i['DEP_TIME'] , i['DEP_DELAY'] , i['DEP_DELAY_NEW'] , i['CRS_ARR_TIME'] , i['ARR_TIME'] , i['ARR_DELAY'] , i['ARR_DELAY_NEW'] , i['CANCELLED'] , i['CANCELLATION_CODE'] , i['DIVERTED'] , i['CRS_ELAPSED_TIME'] , i['ACTUAL_ELAPSED_TIME'] , i['AIR_TIME'] , i['DISTANCE'] , i['CARRIER_DELAY'] , i['WEATHER_DELAY'] , i['NAS_DELAY'] , i['SECURITY_DELAY'] , i['LATE_AIRCRAFT_DELAY']) for i in dr]
            sql_insert(to_db)
            print('completed' + str(months))

