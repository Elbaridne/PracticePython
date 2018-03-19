import requests
from bs4 import BeautifulSoup
import re

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"

def getrequest(url):
    return requests.get(url).text

def cleanhtml(req):
    cleantext = re.sub('<[A-Za-z\/][^>]*>', '', req)
    return cleantext

def striparticle(raw_request):
    beauty = BeautifulSoup(raw_request, "html.parser")
    heading = beauty.find(class_="hed").getText()
    print(heading)
    paragraph = beauty.find_all('p')
    print("....")
    for a in range(0,len(paragraph)):
        print(paragraph[a].getText())

striparticle(getrequest(url))