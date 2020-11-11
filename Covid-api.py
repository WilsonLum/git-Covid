# Import Library
import sys
import os
import requests
from requests.exceptions import HTTPError
import json
import logging
import warnings
from datetime import datetime

import numpy as np, pandas as pd

warnings.filterwarnings("ignore")

#----------------------------------------------------------------
# Create Log folder
#----------------------------------------------------------------
Log_DIR = ("log")
CHECK_FOLDER = os.path.isdir(Log_DIR)

# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.makedirs(Log_DIR)
    print("created folder : ", Log_DIR)

else:
    print(Log_DIR, "folder already exists.")

#----------------------------------------------------------------
# Logging information
#----------------------------------------------------------------
logFileName = Log_DIR + '\covid19.log'
logging.basicConfig(filename=logFileName,filemode='a',level=logging.INFO,format='%(asctime)s :: %(levelname)s :: %(message)s')

#---------------------------------------------------------
# Variable definitions and config file opening
#---------------------------------------------------------

api_path = "https://covid-api.com/api/reports"
config_file = "config.txt"

logging.info("Reading Config file")

f1 = None
try:
    with open(config_file, 'r') as f1:
        myconfig = [line.rstrip('\n') for line in f1]

except Exception as e:

    print("Unable to read at row " + config_file + " Error %s" % (e))
    logging.error("Unable to read at row " + config_file + " Error %s" % (e))

finally:
    if f1 is not None:
        f1.close()

excel_filename = myconfig[0]

#----------------------------------------------------------------
# Read in query parameters excel file
#----------------------------------------------------------------
try:
    query = pd.read_excel(excel_filename)
except Exception as e:
    logging.error(e)
    print(e)

# Convert to date YYYY-MM-MM format
query['date'] =  pd.to_datetime(query['date']).dt.strftime("%Y-%m-%d")

#----------------------------------------------------------------
# Function to get request to the api
#----------------------------------------------------------------
def Get_data(url):
    mydata = []
    try:
        response = requests.get(url)
         # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        logging.error('HTTP error occurred: {http_err}')
        print('HTTP error occurred: {http_err}')  
    except Exception as err:
        logging.error('Other error occurred: {err}') 
        print('Other error occurred: {err}')  
    else:
        mydata = response.json()
        logging.info("Reading url data success")
        print('Success!')
    return mydata

#----------------------------------------------------------------
# Get the api data for each query of Date & Region ISO 
#----------------------------------------------------------------
all_df = pd.DataFrame()
for i in range (0,len(query)):
    date = query['date'][i]
    iso  = query['iso'][i]

    url = api_path+'?date='+date+'&iso='+iso
    mydata = Get_data(url)
    if mydata == []:
        logging.error("Query data not correct") 
        print("Query data not correct")
    else:
        df = pd.DataFrame.from_dict(mydata['data'])
        all_df = all_df.append(df)

#----------------------------------------------------------------
# Get iso data and reformat to desrire output format
#----------------------------------------------------------------
all_df['iso'] = [d.get('iso') for d in all_df.region]
all_df = all_df.rename(columns={"confirmed": "num_confirmed", "deaths": "num_deaths", "recovered": "num_recovered"})
all_df = all_df[['date','iso','num_confirmed','num_deaths','num_recovered']]

#----------------------------------------------------------------
# Save queried data to excel file
#----------------------------------------------------------------
try:
    all_df.to_excel("output.xlsx",index=False)
except IOError:
    logging.info("Cannot open the file")
    print("Cannot open the file")

logging.info("done")
print("done")
