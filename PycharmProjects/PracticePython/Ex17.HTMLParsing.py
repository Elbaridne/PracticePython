import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/HTML"


def buildurl():
    lang = ('es', 'en')
    link = "https://{0}.wikipedia.org/wiki/{1}".format(lang[0], input("¿Que deseas buscar?: ").replace(" ", "_"))
    print(link)
    return link


def cleanhtml(raw_html):
    cleantext = re.sub('<[A-Za-z\/][^>]*>', '', raw_html)
    return cleantext


def getrequest(url):
    req = requests.get(url)
    return req.text


def stripurl(request):
    beaut = BeautifulSoup(request, "html.parser")
    encabezado = beaut.find(id="firstHeading")
    print("Wikipedia - Página ----> {0}".format(cleanhtml(str(encabezado))))
    for headline in beaut.find_all(class_="mw-headline"):
        print(cleanhtml(". " + str(headline)))


while (True):
    requrl = getrequest(buildurl())
    stripurl(requrl)
