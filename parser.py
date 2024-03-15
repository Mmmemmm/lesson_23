import requests
from bs4 import BeautifulSoup

url='https://dedmorozural.ru/'
responce=requests.get(url)
print(responce.status_code)
#print(responce.text)

soup=BeautifulSoup(responce.text,'html.parser')
print(soup.title)

print(soup)
print(soup.a.string)

print(soup.a.get('href'))

images_tags=soup.find_all('img')
for tag in images_tags:
    print(tag)

    a_tags=soup.find_all('a')
    for a_tag in a_tags:
        print(a_tag)

big_body_div=soup.find_all('div',class_='modulebody1')

print(big_body_div)