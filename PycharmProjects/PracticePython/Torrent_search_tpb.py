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
    if "No hits" in pag_req:
        print("No hits")
    else:
        soup = BeautifulSoup(pag_req,"html.parser")
        hrefs = soup.find_all('a', href=True)
        for ref in hrefs:
            pass
        print(hrefs)





check_search(search_builder("Mario mola"))
check_search(search_builder("Adobe Photoshop"))
