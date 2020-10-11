# Github:       thedeclineirl
# Name:         Thomas Higgins
# Created:      2020-10-05
# Editted:      2020-10-06
# ############################## #

# imports
from datetime import datetime

DEBUG = True

# Declare Variables

import_name = 'data\IE_by_county.csv'#'in\converted.csv'
export_name = 'out\county_inserts.sql'

if DEBUG:
    country = 'Ireland'
    county = 'Mayo'
    date = '2020-03-17'
    cases = 5
    de_cases = 0

export_header = 'INSERT INTO Daily_Cases (Country,County,FullDate,Cases) VALUES '

### import 
def import_data(import_name):
    return [line.strip() for line in open(import_name, 'r')]


def fix_data(data):
    data.pop(0) # drop headers from csv
    results = []
    for line in data:
        x = line.split(',')
        tofix = x[0].split('/')
        date = '{2}-{1}-{0}'.format(tofix[0],tofix[1],tofix[2])
        county = x[2].strip()
        cases = x[1].strip()
        if cases == 'N/A':
            cases = 0
            # print(cases)
        # cases = cases.strip('≤')

        result = '\'Ireland\',\'{0}\',\'{1}\',{2}'.format(county,date,cases)
        results.append(result)
    return results

def export_sql_insert(data,headers, export_name):
    outfile = open(export_name,'a')
    # outfile.write(headers+' ')
    x=0
    for line in data:
        if x ==0:
            outfile.write(headers+' ')
        # line = country, county, date, new cases,
        outfile.write('('+line+')')
        if x<999:
            outfile.write(',\n')
            x+=1
        else:
            outfile.write(';\n')
            x=0
    outfile.write(';\n\n')



data = import_data(import_name)
cleaned = fix_data(data)
# print(cleaned)
export_sql_insert(cleaned,export_header,export_name)
print('Completed')

# INSERT INTO Daily_Cases (Country,County,FullDate,New_Cases) VALUES ('Ireland','Carlow','2020-09-30',5);
### ToDo
    # 
    # Convert Date to YYYY-MM-DD from DD/MM/YYYY
    # Get data in correct order

# def convert_date(data):
#     for line in data:


# for line in data 

# def export_to_sql(results,export_name):
#     headers = 'Date,Case,County'
#     outfile = open(export_name,'a')
#     outfile.write(headers+'\n')
#     for datum in results:
#         for item in datum:
#             outfile.write(str(item)+', ')
#         outfile.write('\n')

      