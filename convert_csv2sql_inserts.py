# Github:       thedeclineirl
# Name:         Thomas Higgins
# Created:      2020-10-05
# Editted:      2020-10-06
# ############################## #

# imports
from datetime import datetime

DEBUG = True

# Declare Variables
# export_name = 'out/'+datetime.now().strftime("%Y-%m-%d--%H-%M-%S")+'.csv'

import_name='in\converted.csv'

if DEBUG:
    country = 'Ireland'
    county = 'Mayo'
    date = '2020-03-17'
    cases = 5
    de_cases = 0

export_header = 'INSERT INTO Daily_Cases (Country,County,FullDate,New_Cases) VALUES '

### import 
def import_data(import_name):
    return [line.strip() for line in open(import_name, 'r')]
    
data = import_data(import_name)
data.pop(0) # drop headers from csv






# INSERT INTO Daily_Cases (Country,County,FullDate,New_Cases) VALUES ('Ireland','Carlow','2020-09-30',5);
### ToDo
    # 
    # Convert Date to YYYY-MM-DD from DD/MM/YYYY
    # Get data in correct order

def convert_date(data):
    for line in data:


def export_sql_insert(data, export_name):
    outfile = open(export_name,'a')
    outfile.write(headers+'\n')
    for line in data:
        # line = country, country, date, new cases,
        outfile.write('('+line[0]+','+line[1]+','+line[2]+','+line[3]+');'+'\n')





# for line in data 

# def export_to_sql(results,export_name):
#     headers = 'Date,Case,County'
#     outfile = open(export_name,'a')
#     outfile.write(headers+'\n')
#     for datum in results:
#         for item in datum:
#             outfile.write(str(item)+', ')
#         outfile.write('\n')

      