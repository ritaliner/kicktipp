import requests
import time
from bs4 import BeautifulSoup






def get_data():
	html = requests.get(urls).content
	soup = BeautifulSoup(html, "lxml")
	f = open('soup.html', 'wb')
	f.write(soup.prettify().encode('utf8'))
	data = soup.find_all('div', 'mg_name')
	data_positions = soup.find_all('td', 'position right nw d0')


	for position in data_positions:
		print(position)
	
	list_names = [name.string for name in data]

	print(list_names)

    
    
    
urls = 'https://www.kicktipp.at/wm-partypatrioten/gesamtuebersicht?ansicht=platzierungen&'
url = 'https://www.kicktipp.at/wm-partypatrioten/gesamtuebersicht/tipper?ansicht=platzierungen&rankingTeilnehmerId='
user = '22490855'
get_data()
