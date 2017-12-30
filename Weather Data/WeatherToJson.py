# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:27:47 2017

@author: amar.lad
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 09:22:22 2017

@author: amar.lad
"""

import json
import datetime
import os
import requests

# add your API key (from wunderground) here
api_key = "xxxxxxxxxxxxxxxxx"

station_ids = ["LAX", ] 

for station_id in station_ids:
    filename =  station_id + 'weatherdata.txt' 
    print("Fetching data for station ID: %s" % station_id)
    try:
      	with open(filename, 'w') as outfile:  
			# enter the first and last day required here
            start_date = datetime.date(2017,1,1)
            end_date = datetime.date(2017,12,29)
            
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
                json.dump(data, outfile)
                # increment the day by one
                date += datetime.timedelta(days=1)
    except Exception:
	# tidy up
        os.remove(outfile)

print ("Done!")
