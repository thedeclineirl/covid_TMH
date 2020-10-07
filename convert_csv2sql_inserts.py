# Github:       thedeclineirl
# Name:         Thomas Higgins
# Created:      2020-10-05
# Editted:      2020-10-06
# ############################## #

# imports
from datetime import datetime

# Declare Variables
# import_name = 'in/new.csv'
# export_name = 'out/'+datetime.now().strftime("%Y-%m-%d--%H-%M-%S")+'.csv'



### import 
def import_data(import_name):
    return [line.strip() for line in open(import_name, 'r')]
    
data = import_data(import_name)

for line in data 

def export_to_sql(results,export_name):
    headers = 'Date,Case,County'
    outfile = open(export_name,'a')
    outfile.write(headers+'\n')
    for datum in results:
        for item in datum:
            outfile.write(str(item)+', ')
        outfile.write('\n')


    # 'INSERT INTO' + Database_Name + '
    #        (TableName
    #        ,ChangeTracking_VersionNumber
    #        ,ETLStatus
    #        ,StartTime
    #        ,EndTime
    #        ,RecordCount)
    #  VALUES
    #        (@TableName
    #        ,NULL
    #        ,'Running'
    #        ,getdate()
    #        ,NULL
    #        ,NULL)

           