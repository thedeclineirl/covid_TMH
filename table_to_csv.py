# Github:       thedeclineirl
# Name:         Thomas Higgins
# Created:      2020-10-06
# Editted:
# ############################## #

# imports
from datetime import datetime

# Declare Variables
import_name = 'in/new.csv'
export_name = 'out/'+datetime.now().strftime("%Y-%m-%d--%H-%M-%S")+'.csv'



### import 
def import_data(import_name):
    return [line.strip() for line in open(import_name, 'r')]
    

data = import_data(import_name)

def process_data(data):
    cells=[]
    county=[]
    results=[]

    for line in data:
        cell = line.split(',')    
        cells.append(cell)

    # get counties from the first row
    x = cells.pop(0)
    for y in x:
        county.append(y)
    # drop the word date from the counties list
    county.pop(0)

    ### clean-up

    while len(cells)>0:
        row = cells.pop(0)
        date = row.pop(0)
        a=0
        while a<len(row): 
            result = [date,row[a],county[a]]
            results.append(result)
            a+=1
    return results

results = process_data(data)

### export
def export_csv(results,export_name):
    headers = 'Date,Case,County'
    outfile = open(export_name,'a')
    outfile.write(headers+'\n')
    for datum in results:
        for item in datum:
            outfile.write(str(item)+', ')
        outfile.write('\n')

export_csv(results,export_name)

print('Complete')

