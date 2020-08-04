from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, re, string, json
import urllib.request

#option = browser.find_element_by_xpath("//select/option[@value='2020-03-01']")
def urlMaker(date):
    link = 'http://libcal.library.drexel.edu/rooms_acc.php?gid=3656&d=' + str(date) + '&cap=0'
    return link

def openWeb(link):
    website = webdriver.Firefox()
    website.get(link)
    return website

def fill(fieldID, whatToFill, website):
    fname = website.find_element_by_id(fieldID)
    fname.send_keys(whatToFill)

def click(buttonID, website):
    numOfPeople = website.find_element_by_id(buttonID)
    numOfPeople.click()
    
def addTimeslot(text, website):
    tail = int(text[3:])
    head = 'sch'
    for i in range(6):
        code = head + str(tail + i)
        website.find_element_by_id(code).click()

url = urlMaker('2020-03-21')
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

#id scraper
l1st = []
for product_div in soup.find_all('div', {'class': 'checkbox'}):
    product_tag = product_div.find('label')
    product_id = product_tag.attrs['for']
    l1st.append(product_id)

#for 0000-1700 day (17+4)
idNeeded = l1st[-42]

#for 0000-0000 day (24+11)
#idNeeded = l1st[-70]

#for 1000-2000 day (20+7)
#idNeeded = l1st[-54]

a = openWeb(url)
addTimeslot(idNeeded, a)
fill('fname','Quan', a)
fill('lname','Ta', a)
fill('email','qmt26@drexel.edu', a)
click('rb142141', a)
#click('s-lc-rm-ac-but', a)
              