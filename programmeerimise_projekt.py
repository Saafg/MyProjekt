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
ruutmeetrihind = []
hind = []

for item in data:
        print(item.contents[3].find_all("h2")[0].text.strip())
        f.write(item.contents[3].find_all("h2")[0].text.strip() + "\n")
        print("Tube: " + item.contents[5].text)
        toad.append(item.contents[5].text)
        f.write("Tube: " + item.contents[5].text + "\n")
        print("Ruutmeetreid: " + item.contents[7].text.strip())
        ruutmeetreid.append(item.contents[7].text.strip()[0:-3])
        f.write("Tube: " + item.contents[7].text.strip() + "\n")
        print("Ruutmeetrihind: " + str(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()))
        ruutmeetrihind.append(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()[0:-5])
        f.write("Ruutmeetrihind: " + str(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()) + "\n")
        print("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()))
        hind.append(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()[0:-2])
        f.write("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()) + "\n\n")
        print()



tubasid_kokku = 0
tubadega_kvsid = 0
for i in toad:
    if i.isnumeric():
        tubasid_kokku += int(i)
        tubadega_kvsid += 1

ruutmeetreid_kokku = 0
pindalaga_kvsid = 0
for i in ruutmeetreid:
    if i.isnumeric():
        ruutmeetreid_kokku += float(i)
        pindalaga_kvsid += 1

ruutmeetrihind_kokku = 0
ruutmeetrihinnaga_kvsid = 0
for i in ruutmeetrihind:
    if i.isnumeric():
        ruutmeetrihind_kokku += float(i)
        ruutmeetrihinnaga_kvsid += 1

hind_kokku = 0
hinnaga_kvsid = 0
for i in hind:
    if i.isnumeric():
        hind_kokku += float(i)
        hinnaga_kvsid += 1


print("Keskmised:")
print("Tube keskmiselt: " + str(round((tubasid_kokku/tubadega_kvsid),2)))
print("Ruutmeetreid keskmiselt: " + str(round((ruutmeetreid_kokku/pindalaga_kvsid),2)) + " m²")
print("Keskmine ruutmeetrihind: " + str(round(ruutmeetrihind_kokku/ruutmeetrihinnaga_kvsid,2)) + " €/m²")
print("Keskmine hind: " + str(round(hind_kokku/hinnaga_kvsid,2)) + " €")


f.close()