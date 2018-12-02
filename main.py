import requests
import wget
import urllib.request
import datetime

url = "http://kartbites.com/"
apiKey = "A.f4ed48a6e9aa9c0726ed7833973b1d2d"
finalURL = "http://www.webpagetest.org/runtest.php?url="+url+"&k="+apiKey+"&f=JSON"
print("Final URL is ",finalURL)
res = requests.get(finalURL)
json = res.json()
csvURL = json['data']['summaryCSV']
print("CSV URL is",csvURL)
print("JSON ",str(json))
with open("testresponse.json","a") as file:
    file.write("\n\n--New entry {}-- \n\n".format(datetime.datetime.now()))
    file.write(str(json))