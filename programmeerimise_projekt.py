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
        x=(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()[0:-2])
        x=x.replace(u"\xa0","")
        hind.append(x)
        f.write("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()) + "\n\n")
        print()



tubasid_kokku = 0
tubadega_kvsid = 0
for i in toad:
    if i != "":
        tubasid_kokku += int(i)
        tubadega_kvsid += 1

ruutmeetreid_kokku = 0
pindalaga_kvsid = 0
alla20 = 0
alla30 = 0
alla40 = 0
alla50 = 0
alla60 = 0
alla70 = 0
alla80 = 0
alla100 = 0
for i in ruutmeetreid:
    if i != "":
        if float(i) < 20:
            alla20 += 1
        if float(i) >= 20 and float(i)<30:
            alla30 += 1
        if float(i) >= 30 and float(i)<40:
            alla40 += 1
        if float(i) >= 40 and float(i)<50:
            alla50 += 1
        if float(i) >= 50 and float(i)<60:
            alla60 += 1
        if float(i) >= 60 and float(i)<70:
            alla70 += 1
        if float(i) >= 70 and float(i)<80:
            alla80 += 1
        if float(i) >= 80 and float(i)<100:
            alla100 += 1
        ruutmeetreid_kokku += float(i)
        pindalaga_kvsid += 1

alla2 = 0
ruutmeetrihind_kokku = 0
ruutmeetrihinnaga_kvsid = 0
for i in ruutmeetrihind:
    if i.isnumeric():
        ruutmeetrihind_kokku += float(i)
        ruutmeetrihinnaga_kvsid += 1

hind_kokku = 0
hinnaga_kvsid = 0
for i in hind:
    if i != "":
        hind_kokku += float(i)
        hinnaga_kvsid += 1


print("Keskmised:")
print("\tTube keskmiselt: " + str(round((tubasid_kokku/tubadega_kvsid),2)))
print("\tRuutmeetreid keskmiselt: " + str(round((ruutmeetreid_kokku/pindalaga_kvsid),2)) + " m²")
print("\tKeskmine ruutmeetrihind: " + str(round(ruutmeetrihind_kokku/ruutmeetrihinnaga_kvsid,2)) + " €/m²")
print("\tKeskmine hind: " + str(round(hind_kokku/hinnaga_kvsid,2)) + " €")

f.write("\tKeskmised:")
f.write("\tTube keskmiselt: " + str(round((tubasid_kokku/tubadega_kvsid),2)))
f.write("\tRuutmeetreid keskmiselt: " + str(round((ruutmeetreid_kokku/pindalaga_kvsid),2)) + " m²")
f.write("\tKeskmine ruutmeetrihind: " + str(round(ruutmeetrihind_kokku/ruutmeetrihinnaga_kvsid,2)) + " €/m²")
f.write("\tKeskmine hind: " + str(round(hind_kokku/hinnaga_kvsid,2)) + " €")

print()
print("Jaotumine vahemikesse: ")
print("\tTubade arvu järgi: ")
print("\t\tÜhetoalisi kv pakkumisi: " + str(toad.count("1")))
print("\t\tKahetoalisi kv pakkumisi: " + str(toad.count("2")))
print("\t\tKolmetoalisi kv pakkumisi: " + str(toad.count("3")))
print("\t\tNeljatoalisi kv pakkumisi: " + str(toad.count("4")))
print("\t\tViie ja enamatoalisi kv pakkumisi: " + str(tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3")+
toad.count("4"))))

print("\tPindala järgi: ")
print("\t\tKv pakkumisi pindalaga kuni 20 m²: " + str(alla20))
print("\t\tKv pakkumisi pindalaga 20 kuni 30 m²: " + str(alla30))
print("\t\tKv pakkumisi pindalaga 30 kuni 40 m²: " + str(alla40))
print("\t\tKv pakkumisi pindalaga 40 kuni 50 m²: " + str(alla50))
print("\t\tKv pakkumisi pindalaga 50 kuni 60 m²: " + str(alla60))
print("\t\tKv pakkumisi pindalaga 60 kuni 70 m²: " + str(alla70))
print("\t\tKv pakkumisi pindalaga 70 kuni 80 m²: " + str(alla80))
print("\t\tKv pakkumisi pindalaga üle 80 m²: " + str(pindalaga_kvsid-(alla20+alla30+alla40+alla50+alla60+alla70+alla80)))

print("\tRuutmeetri hinna järgi: ")
print("\t\tKv pakkumisi hinnaga kuni 2 €/m²: " + str(alla20))
print("\t\tKv pakkumisi pindalaga 20 kuni 30 m²: " + str(alla30))
print("\t\tKv pakkumisi pindalaga 30 kuni 40 m²: " + str(alla40))
print("\t\tKv pakkumisi pindalaga 40 kuni 50 m²: " + str(alla50))
print("\t\tKv pakkumisi pindalaga 50 kuni 60 m²: " + str(alla60))
print("\t\tKv pakkumisi pindalaga 60 kuni 70 m²: " + str(alla70))
print("\t\tKv pakkumisi pindalaga 70 kuni 80 m²: " + str(alla80))
print("\t\tKv pakkumisi pindalaga üle 80 m²: " + str(pindalaga_kvsid-(alla20+alla30+alla40+alla50+alla60+alla70+alla80)))

f.close()