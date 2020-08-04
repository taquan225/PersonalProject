from bs4 import BeautifulSoup
import requests
import json
import urllib.request
url = "http://drexel.edu/events/categories/health_wellness"
response = requests.get(url, eventTimesout = 5)
soup = BeautifulSoup(response.text, "html.parser")
pages = []
link = []
eventTimes = []
date = []
t1me = []
l1nks = []
event = []

#Scrape links, date and time and add those to the unprocessed list
for div in soup.body.find_all('div'):
    if div.get('class'):
        if div['class'][0] == 'eventlistdiv':
            for x in soup.find_all('a'):
                if x.get("href") is not None:
                    pages.append(x['href'])
                    l1nks.append(x.text)
                if x.get("class") and x['class'][0]== "listtext":
                    t1me.append(x.text)
            for y in soup.find_all('td'):
                if y.get("class") and y["class"][0] == "listheadtext":
                    date.append(y.text)

#Format the link and add to the link list
for i in range(48,len(pages)-98):
    x = 'http://events.drexel.edu/'+pages[i]
    link.append(x)

#Scrape the event and add to the event list
for i in range(48,len(pages)-98):
    x = l1nks[i]
    event.append(x)

#Add the time to the time list
for time in t1me:
    if time != '':
        eventTimes.append(tim)

#This list is used to append date that is duplicated
addList = [0,0,3,5,7,12,13,14,16,17,20,23,28,29]
for i in addList:
    date.insert(i, date[i])

#This code is used to export into json format file
output = [{"Event": e, "Link": l, "eventTimes": t, "Date": d} for e, l, t, d in zip(event, link, eventTimes, date)]
with open('Ci1032.json', 'w') as outfile:
    json.dump(output, outfile)