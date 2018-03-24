import subprocess , os , sys
import requests
from bs4 import BeautifulSoup

def search_builder(nam):
    # "pyrite es el mejor" https://thepiratebay.cr/search/pyrite%20es%20el%20mejor/0/7/
    tpb = "https://thepiratebay.cr/search/"
    nam = nam.replace(" ", "%20")
    return tpb+nam+"/0/7/"

def check_search(built_url):
    pag_req_raw = requests.get(url=built_url)
    pag_req = pag_req_raw.text
    magnets = []
    rawtitles = []
    if "No hits" in pag_req:
        print("No hits")
    else:
        soup = BeautifulSoup(pag_req,"html.parser")
        hrefs = soup.find_all('a', href=True)
        titles = soup.find_all(class_="detName")
        for href in hrefs:
            hrf = str(href.get('href'))
            if hrf.startswith("magnet"):
                magnets.append(hrf)

        for tit in titles:
            rawtitles.append(tit.getText())


        for i in range(3):
            print("{0}\n {1}\n".format(rawtitles.pop(),magnets.pop()))






def open_magnet(mgn):
    ssoo = sys.platform
    if ssoo.startswith('win32'):
        os.startfile(mgn)
    if ssoo.startswith('linux'):
        subprocess.Popen(['xdg-open', mgn],stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#TODO String formating for SXXEYY s: season e:episode and HD/720...
def top3magnet(busqueda):
    if busqueda is '':
        print("Busqueda vacía")
    else:
        url = search_builder(busqueda)
        check_search(url)



if __name__ == '__main__':
    top3magnet("Game of Thrones")
