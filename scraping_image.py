import requests
from bs4 import BeautifulSoup

page_url = 'https://www.arita-marukei.com/?mode=srh&cid=&keyword='
img_url_base = 'https://www.arita-marukei.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.text)

contents = soup.find('ul', class_='row-list row-list--middle')


contents_a = contents.a

print('herf:{}'.format(contents_a.get('href')))

