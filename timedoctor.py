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
# Access Token: ODFjYjU5OTIwNGM5ZmZlODJiOWMyNjQ2M2Q4MWY5YWNhZjg3YjBhMzVjMjUxNzA0YzJlMjA4OWIzMjdiMjU1MQ
apiKey = "ODFjYjU5OTIwNGM5ZmZlODJiOWMyNjQ2M2Q4MWY5YWNhZjg3YjBhMzVjMjUxNzA0YzJlMjA4OWIzMjdiMjU1MQ"
requestURL = "/v1.1/companies/268662/users/329528/projects?access_token=ODFjYjU5OTIwNGM5ZmZlODJiOWMyNjQ2M2Q4MWY5YWNhZjg3YjBhMzVjMjUxNzA0YzJlMjA4OWIzMjdiMjU1MQ&_format=json"
url = "https://webapi.timedoctor.com/v1.1/companies/268662/users/329528"


#My  unchanging Time Doctor Constants
user_id = 329528
company_id = 268662

#Time Doctor Api url
timeURL = "https://webapi.timedoctor.com"
myCompleteApiCall = timeURL + requestURL

myData = urllib.request.urlopen(myCompleteApiCall).read().decode('utf-8')
myDataJson = json.loads(myData)
print(myDataJson)
