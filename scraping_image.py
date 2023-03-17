import requests
from bs4 import BeautifulSoup

page_url = 'https://www.arita-marukei.com/?mode=srh&cid=&keyword='
img_url_base = 'https://www.arita-marukei.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.text)
urls = []
contents = soup.find('ul', class_='row-list row-list--middle')


a_elements = contents.find_all('a')
for a_element in a_elements:
    # print('herf:{}'.format(a_element.get('href')))
    urls.append(img_url_base + a_element.get('href'))

print(urls)
