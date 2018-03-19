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
    with open('{0}.txt'.format(heading), 'w') as f:
        f.write(heading)
        f.write("hellou deja el chou")

    paragraph = beauty.find_all('p')

    with open('{0}.txt'.format(heading), 'w') as f:
        for a in range(0, len(paragraph)):
            f.write(paragraph[a].getText() + '\n')


striparticle(getrequest(url))
