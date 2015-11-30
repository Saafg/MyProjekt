__author__ = 'erkiaun'

import requests
from bs4 import BeautifulSoup

url = "http://www.kv.ee/?act=search.simple&company_id=&page=1&orderby=ob&page_size=&deal_type=2&dt_select=2&county=1&parish=&price_min=&price_max=&price_type=1&rooms_min=&rooms_max=&area_min=&area_max=&floor_min=&floor_max=&keyword="
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("tr", attrs={"class":"object-type-apartment", "id":True})

f=(open("kinnisvara.txt", "w"))

toad = []
ruutmeetreid = []

for item in data:
        print(item.contents[3].find_all("h2")[0].text.strip())
        f.write(item.contents[3].find_all("h2")[0].text.strip() + "\n")
        print("Tube: " + item.contents[5].text)
        toad.append(item.contents[5].text)
        f.write("Tube: " + item.contents[5].text + "\n")
        print("Ruutmeetreid: " + item.contents[7].text.strip())
        ruutmeetreid.append(int(item.contents[7].text.strip()))
        f.write("Tube: " + item.contents[7].text.strip() + "\n")
        print("Ruutmeetrihind: " + str(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()))
        f.write("Ruutmeetrihind: " + str(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()) + "\n")
        print("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()))
        f.write("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()) + "\n\n")
        print()

f.close()



