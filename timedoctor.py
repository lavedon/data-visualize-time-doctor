import json
import urllib.request
import urllib.error
import numpy
import matplotlib as mp

# Picture of the Enterprise

#                                 ___
#                _____.----------'---`----------._____
#       ___.----'-------------------------------------`----.___
#     ===========================================================
#               `----.________           ________.----'
#                ((___))      `---------'      ((___))
#                 `-.-'         _\_|_/_         `-.-'
#                   |        .-' _____ `-.        |
#                    \______/ _.'( O )`._ \______/
#                           `-.`-.___.-'.-'
#                              `-------'
#

#MY API KEY:
# Access Token: OGMzYzk5NWZmN2FiOWEyZmUzNGFmOWFiMTMxNGM3ODA0ZDZlMDI2ZThmNjI5YmFhYjdhNzYwNGRiNGUwOGI1MA
apiKey = "Y2E4MjJlOTk4NDM4Zjc4YWQ5NjA2MmViNTczZmUzNmFjYTdiMDI4MDNjYzhmNDRhY2M1MDgwYjE0MWNkZTFjNg"
requestURL = "/v1.1/companies/268662/worklogs?access_token=OGMzYzk5NWZmN2FiOWEyZmUzNGFmOWFiMTMxNGM3ODA0ZDZlMDI2ZThmNjI5YmFhYjdhNzYwNGRiNGUwOGI1MA&_format=json&start_date=2017-10-01&end_date=2017-10-31&consolidated=1"
url = "https://webapi.timedoctor.com/v1.1/companies/268662/users/329528"

#############
# Example request for worklog for an entire month
# /v1.1/companies/268662/worklogs?access_token=OGMzYzk5NWZmN2FiOWEyZmUzNGFmOWFiMTMxNGM3ODA0ZDZlMDI2ZThmNjI5YmFhYjdhNzYwNGRiNGUwOGI1MA&_format=json&start_date=2017-10-01&end_date=2017-10-31&consolidated=1
#############


#  Use a calendar library to auto show this month and week


#My  unchanging Time Doctor Constants
user_id = 329528
company_id = 268662

#Time Doctor Api url
timeURL = "https://webapi.timedoctor.com"
myCompleteApiCall = timeURL + requestURL

myData = urllib.request.urlopen(myCompleteApiCall).read().decode('utf-8')
myDataJson = json.loads(myData)
print(myDataJson)
