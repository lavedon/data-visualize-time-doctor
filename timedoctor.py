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

worked = myDataJson.get("worklogs").get("items")

print("This month:")
for i in worked:
    seconds = int(i.get("length"))
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    duration = "%d:%02d:%02d" % (h, m, s)
    print("{}: {}".format(i.get("task_name"), duration))
    
#  @TODO similar print out for projects only
#  @TODO display calendar of total time each day in the month
#  @TODO Average last 5 days
#  @TODO Average last 7 days 
#  @TODO Max total time 'best time' last month
#  @TODO Max total time 'best total time worked' this week
#  @TODO some neat graphs
#  @TODO GUI with PyQt
#  @TODO Efficiency Ratio stuff - Start and End times / Time Doctor Time
#  @TODO More efficiency ratio - so far today - best of the week - best of the month
#  @TODO Best way is to download data at the beginning for this month, last month, last week, today, last 5 days

