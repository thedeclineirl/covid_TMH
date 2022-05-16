# 
# Thomas Higgins
# 
# created:	2022-05-13
# modified:	2022-05-14
#

from urllib.request import urlopen

import pandas as pd 
import json


##################################
###	Functions
##################################

def listStripper(data,text):
	result = []
	for x in data:
		result.append(x[text])
	return result

# Returns a list of Dictionary objects from the JSON retrieved from the given url
def getJsonAsListofDict(url):
	data = json.loads(urlopen(url).read())['features'] # Get the features to get a list of object
	return(listStripper(data,'properties')) 

##################################
###	Variables
##################################
url = "https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/CovidStatisticsProfileHPSCIrelandOpenData/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"



##################################
###	Sandbox
##################################

data = getJsonAsListofDict(url)

data4 = data.pop()
# print(data4.keys())
data5 = data4.keys()
for a in data4:
	print(a.key())
	print(a.value())


##################################
###	NOTES
##################################

# Drop last 3 zeros from the json date to get the correct date in unix timestamp format

