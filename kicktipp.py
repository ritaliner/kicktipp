import requests
import time
from bs4 import BeautifulSoup



urls = 'https://www.kicktipp.at/wm-partypatrioten/gesamtuebersicht?ansicht=platzierungen&'
list_names = 0
# dic = {}


def get_data():
    # global dic
    rangs_with_names = []
    html = requests.get(urls).content
    soup = BeautifulSoup(html, "lxml")
    f = open('soup.html', 'wb')
    f.write(soup.prettify().encode('utf8'))
    data = soup.find_all('div', 'mg_name')
    positions = soup.find_all('td', 'position right nw d0')
    rang = [name.string for name in positions]
    list_names = [name.string for name in data]
    # print(rang)
    # print(list_names)
    for index in range(min(len(rang),len(list_names))):
        rangs_with_names.append('{}. {}'.format(rang[index], list_names[index]))
    text = ("\n".join(rangs_with_names))
    return text


