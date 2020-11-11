# Covid19 Data API Extraction

## 1.0 Datasource Description
https://covid-api.com/api/reports/. 

## 2.0 Structure
- Create new python venv
  - pip3 install virtualenv
  - virtualenv covid
  - pip3 install requirements.txt
- Folder structure
  - log    : storing logging info and error message
  
- Files structure
  - run.sh           : Bash script to run the python code
  - requirements.txt : for the python library installation requirements (Need to install this to run)
  - Covid-api.py     : main python file to run and extract data 
  - inout_query.xlsx : excel file for the input Date and ISO query data
  - output.xlsx      : store the results of the query in this excel file
  - config.txt       : location of the input_query.xlsx file
  
## 3.0 Coding Challenge
- Read a config file to get the location of an excel file 
- Read the excel file. The excel contains data with two columns: “date” and “iso”.  “date” is in “YYYY-MM-DD” format. “Iso” is the 3 digit ISO code of the country.
- Make an API request to https://covid-api.com/api/reports/ for each combination of date and iso in the excel
- Produce a table containing the following columns from parameters queried and the results returned: “date” “iso” “num_confirmed” “num_deaths” “num_recovered” 
- Write the table to an excel on disk.
- The script should be production- ready (i.e. proper error handling, logging, read_me.txt and etc.)
- Please include script for unit testing. 
