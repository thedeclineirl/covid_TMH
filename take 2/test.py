# 
# Thomas Higgins
# 
# created:	2022-05-13
# modified:	2022-05-14
#

from urllib.request import urlopen

import pandas as pd 
import json

def listStripper(data,text):
	result = []
	for x in data:
		result.append(x[text])
	return result


url = "https://services1.arcgis.com/eNO7HHeQ3rUcBllm/arcgis/rest/services/CovidStatisticsProfileHPSCIrelandOpenData/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
response = urlopen(url)
data = json.loads(response.read())
data2 = data['features'] # Get the features to get a list of object
# data3 = data2[-1]
# data4 = data3['properties']

data5 = listStripper(data2,'properties')
print(len(data5))
print(data5[-2],data5[-3],data5[-4],data5[-5])


# df = pd.read_json(data,orient ='index')
# df = pd.DataFrame.from_dict(data,orient="index")
# y = json.dumps(data)
# print(y)

# print(data3.keys())
# print(data['type'])
# print(data4)


#########
# print(df.info())


# Drop last 3 zeros from the json date to get the correct date in unix timestamp