import requests
from bs4 import BeautifulSoup
import os


def download_image(url, file_path):
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(r.content)


if __name__ == '__main__':
    page_url_base = 'https://www.arita-marukei.com/?mode=cate&cbid=2482976&csid=0'
    page_num = 52
    img_url_base = 'https://www.arita-marukei.com/'
    urls = []

    # 有田焼一覧からそれぞれのリンクを取得
    for page in range(1, page_num + 1):
        if (page == 1):
            r = requests.get(page_url_base)
        else:
            r = requests.get(page_url_base + '&page=' + str(page))
        soup = BeautifulSoup(r.text)
        contents = soup.find('ul', class_='row-list row-list--middle')
        a_elements = contents.find_all('a')
        for a_element in a_elements:
            # print('herf:{}'.format(a_element.get('href')))
            urls.append(img_url_base + a_element.get('href'))
        print('page:{}={}'.format(page, len(a_elements)))
    os.makedirs('images_sara', exist_ok=True)
    # 取得したリンクから画像を取得
    for i, url in enumerate(urls):
        print('{}/{}'.format(i, len(urls)))
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        contents = soup.find('ul', class_='product__gallery')
        img_elements = contents.find_all('img')
        img_urls = []
        for j, img_elements in enumerate(img_elements):
            img_url = img_elements.get('src')
            file_name = '{}_{}.png'.format(i, j)
            image_path = 'images_sara/{}'.format(file_name)
            download_image(url=img_url, file_path=image_path)
        # print(*img_urls, sep='\n')
        # for j, img_url in enumerate(img_urls):
        #     file_name = '{}_{}.png'.format(i, j)
        #     image_path = 'images_sara/{}'.format(file_name)
        #     download_image(url=img_url, file_path=image_path)
