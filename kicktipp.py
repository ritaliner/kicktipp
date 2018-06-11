import requests
import time
from bs4 import BeautifulSoup



urls = 'https://www.kicktipp.at/wm-partypatrioten/gesamtuebersicht?ansicht=platzierungen&'
list_names = 0



def get_data():
    html = requests.get(urls).content
    soup = BeautifulSoup(html, "lxml")
    f = open('soup.html', 'wb')
    f.write(soup.prettify().encode('utf8'))
    data = soup.find_all('div', 'mg_name')
    data_positions = soup.find_all('td', 'position right nw d0')

    list_names = [name.string for name in data]
    
    return list_names

list_names = get_data()
print (list_names)
