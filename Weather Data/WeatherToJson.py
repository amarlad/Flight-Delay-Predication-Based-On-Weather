# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:22:22 2017

@author: amar.lad
"""
import csv
import datetime
import os
import requests
import sqlite3

# add your API key (from wunderground) here
api_key = "xxxxxxxxxxxxxxxxxxx"
station_ids = ["DFW","SFO","IAH","NYC", ] 

# enter the first and last day required here
start_date = datetime.date(2017,1,1)
end_date = datetime.date(2017,12,29)

# SQLITE database details
weather = 'Weather'
connection = sqlite3.connect('{}.db'.format(weather))
c = connection.cursor()

# Create database table
def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS airportweather (metar TEXT, year TEXT, mon TEXT, mday TEXT, ahour TEXT, amin TEXT, tzname TEXT, tempm TEXT, tempi TEXT, dewptm TEXT, dewpti TEXT, hum TEXT, vism TEXT, visi TEXT, conds TEXT, icon TEXT, fog TEXT, rain TEXT, snow TEXT, hail TEXT, thunder TEXT, tornado TEXT)""")

# SQL insert      
def sql_insert(metar, year, mon, mday, ahour, amin, tzname, tempm, tempi, dewptm, dewpti, hum, vism, visi, conds, icon, fog, rain, snow, hail, thunder, tornado):
    try:
        c.execute("INSERT INTO airportweather VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (metar, year, mon, mday, ahour, amin, tzname, tempm, tempi, dewptm, dewpti, hum, vism, visi, conds, icon, fog, rain, snow, hail, thunder, tornado)) 
        connection.commit()
    except Exception as e:
        print('s0 insertion',str(e))
        

# main function 
if __name__ == "__main__":
    create_table()
    
    for station_id in station_ids:
        filename =  station_id + 'weatherdata.csv' 
        print("Fetching data for station ID: %s" % station_id)
        try:
            with open(filename, 'w', newline='') as csvfile:  
                writer = csv.writer(csvfile)
                headers = ['metar', 'year', 'mon', 'mday', 'hour', 'min', 'tzname', 'tempm', 'tempi', 'dewptm', 'dewpti', 'hum', 'vism', 'visi', 'conds', 'icon', 'fog', 'rain', 'snow', 'hail', 'thunder', 'tornado']
                writer.writerow(headers)
                
                date = start_date
                while date <= end_date:
                    
                    # format the date as YYYYMMDD
                    date_string = date.strftime('%Y%m%d')
                    
                    # build the url
                    url = ("http://api.wunderground.com/api/%s/history_%s/q/%s.json" %
                    						  (api_key, date_string, station_id))
                    
                    # make the request and parse json
                    data = requests.get(url).json()
                    
                    # build your row
                    for history in data['history']['observations']:
                        row = []
                        row.append(str(history["metar"]))
                        row.append(str(history['date']["year"]))
                        row.append(str(history['date']["mon"]))
                        row.append(str(history['date']["mday"]))
                        row.append(str(history['date']["hour"]))
                        row.append(str(history['date']["min"]))
                        row.append(str(history['date']["tzname"]))
                        row.append(str(history['tempm']))
                        row.append(str(history['tempi'])) 
                        row.append(str(history['dewptm'])) 
                        row.append(str(history['dewpti'])) 
                        row.append(str(history['hum'])) 
                        row.append(str(history['vism'])) 
                        row.append(str(history['visi'])) 
                        row.append(str(history['conds'])) 
                        row.append(str(history['icon'])) 
                        row.append(str(history['fog'])) 
                        row.append(str(history['rain'])) 
                        row.append(str(history['snow'])) 
                        row.append(str(history['hail'])) 
                        row.append(str(history['thunder'])) 
                        row.append(str(history['tornado'])) 
                        writer.writerow(row)
  
                      
                        metar   = history["metar"]
                        year    = history["date"]["year"]
                        mon     = history["date"]["mon"]
                        mday    = history["date"]["mday"]
                        ahour   = history["date"]["hour"]
                        amin    = history["date"]["min"]
                        tzname  = history["date"]["tzname"]
                        tempm   = history["tempm"] 
                        tempi   = history["tempi"] 
                        dewptm  = history["dewptm"]  
                        dewpti  = history["dewpti"] 
                        hum     = history["hum"] 
                        vism    = history["vism"] 
                        visi    = history["visi"] 
                        conds   = history["conds"] 
                        icon    = history["icon"] 
                        fog     = history["fog"] 
                        rain    = history["rain"] 
                        snow    = history["snow"] 
                        hail    = history["hail"] 
                        thunder = history["thunder"] 
                        tornado = history["tornado"] 
                        sql_insert(metar, year, mon, mday, ahour, amin, tzname, tempm, tempi, dewptm, dewpti, hum, vism, visi, conds, icon, fog, rain, snow, hail, thunder, tornado)
                    
                        # increment the day by one
                    date += datetime.timedelta(days=1)
                    
        except Exception:
    	# tidy up
            os.remove(csvfile)

c.close()
print ("Done!")
