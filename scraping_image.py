import requests
from bs4 import BeautifulSoup


page_url_base = 'https://www.arita-marukei.com/?mode=cate&cbid=2482976&csid=0'
page_num = 52
img_url_base = 'https://www.arita-marukei.com/'
urls = []
for page in range(page_num):
    if (page == 0):
        r = requests.get(page_url_base)
    else:
        r = requests.get(page_url_base + '&page=' + str(page))
    soup = BeautifulSoup(r.text)
    contents = soup.find('ul', class_='row-list row-list--middle')
    a_elements = contents.find_all('a')
    for a_element in a_elements:
        # print('herf:{}'.format(a_element.get('href')))
        urls.append(img_url_base + a_element.get('href'))

print(urls)
