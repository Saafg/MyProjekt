__author__ = 'erkiaun'

import requests
from bs4 import BeautifulSoup

tehing =  input("Sisesta huvipakkuva tehingu tüüp(müük, üür või kõik): ")
while tehing != "müük" and tehing != "üür" and tehing != "kõik":
    tehing =  input("Sisesta palun korrektine tehingu tüüp(müük, üür või kõik): ")
if tehing == "üür":
    tehing = "2"
if tehing == "müük":
    tehing = "1"
if tehing == "kõik":
    tehing = "20"

toad_min = input("Sisesta minimaalne tubade arv (kui ei soovi täpsustada, vajuta Enter): ")
while toad_min != "" and toad_min.isnumeric() == False:
    toad_min = input("Sisesta palun korrektselt minimaalne tubade arv (kui ei soovi täpsustada, vajuta Enter): ")

toad_max = input("Sisesta maksimaalne tubade arv (kui ei soovi täpsustada, vajuta Enter): ")
while toad_max != "" and toad_max.isnumeric() == False:
    toad_max = input("Sisesta palun korrektselt maksimaalne tubade arv (kui ei soovi täpsustada, vajuta Enter): ")

hind_min = input("Sisesta minimaalne hind (kui ei soovi täpsustada, vajuta Enter): ")
while hind_min != "" and hind_min.isnumeric() == False:
    hind_min = input("Sisesta palun korrektselt minimaalne hind (kui ei soovi täpsustada, vajuta Enter): ")

hind_max = input("Sisesta maksimaalne hind (kui ei soovi täpsustada, vajuta Enter): ")
while hind_max != "" and hind_max.isnumeric() == False:
    hind_max = input("Sisesta palun korrektselt maksimaalne hind (kui ei soovi täpsustada, vajuta Enter): ")

url = "http://www.kv.ee/?act=search.simple&company_id=&page=1&orderby=ob&page_size=100&deal_type=2&dt_select=2&county=1&parish=&price_min=&price_max=&price_type=1&rooms_min=&rooms_max=&area_min=&area_max=&floor_min=&floor_max=&keyword="
url = url.replace(url[url.find("deal_type"):url.find("deal_type")+23],"deal_type="+tehing+"&dt_select="+tehing)
url = url.replace("rooms_min=","rooms_min="+toad_min)
url = url.replace("rooms_max=","rooms_max="+toad_max)
url = url.replace("price_max=","price_max="+hind_max)
url = url.replace("price_min=","price_min="+hind_min)
print(url)
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("tr", attrs={"class":"object-type-apartment", "id":True})

toad = []
ruutmeetreid = []
ruutmeetrihind = []
hind = []
piirkond = []

for item in data:
        print(item.contents[3].find_all("h2")[0].text.strip())
        print("Tube: " + item.contents[5].text)
        toad.append(item.contents[5].text)
        print("Ruutmeetreid: " + item.contents[7].text.strip())
        ruutmeetreid.append(item.contents[7].text.strip()[0:-3])
        print("Ruutmeetrihind: " + str(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()))
        y=(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip())
        y=y.replace(u"\xa0","")
        ruutmeetrihind.append(y[0:-5])
        print("Hind: " + str(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()))
        x=(item.contents[11].find("p", attrs={"class":"object-price-value"}).text.strip()[0:-2])
        x=x.replace(u"\xa0","")
        hind.append(x)
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
        ruutmeetreid_kokku += float(i)
        pindalaga_kvsid += 1


ruutmeetrihind_i_vahemik = 0
ruutmeetrihind_ii_vahemik = 0
ruutmeetrihind_iii_vahemik = 0
ruutmeetrihind_iv_vahemik = 0
ruutmeetrihind_v_vahemik = 0
ruutmeetrihind_vi_vahemik = 0
ruutmeetrihind_vii_vahemik = 0
ruutmeetrihind_viii_vahemik = 0
ruutmeetrihind_iix_vahemik = 0
for i in range(len(ruutmeetrihind)):
    ruutmeetrihind[i] = float(ruutmeetrihind[i])
print(ruutmeetrihind)
ruutmeetrihinnamax = max(ruutmeetrihind)
print(ruutmeetrihinnamax)
ruutmeetrihind_kokku = 0
ruutmeetrihinnaga_kvsid = 0
for i in ruutmeetrihind:
    if i != "0":
        ruutmeetrihind_kokku += float(i)
        ruutmeetrihinnaga_kvsid += 1
        if float(i) > 0 and float(i)<(ruutmeetrihinnamax/12):
            ruutmeetrihind_i_vahemik += 1
        if float(i) >= (ruutmeetrihinnamax/12) and float(i)<((ruutmeetrihinnamax/12)*2):
            ruutmeetrihind_ii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*2) and float(i)<((ruutmeetrihinnamax/12)*3):
            ruutmeetrihind_iii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*3) and float(i)<((ruutmeetrihinnamax/12)*4):
            ruutmeetrihind_iv_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*4) and float(i)<((ruutmeetrihinnamax/12)*5):
            ruutmeetrihind_v_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*5) and float(i)<((ruutmeetrihinnamax/12)*6):
            ruutmeetrihind_vi_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*6) and float(i)<((ruutmeetrihinnamax/12)*7):
            ruutmeetrihind_vii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*7) and float(i)<((ruutmeetrihinnamax/12)*8):
            ruutmeetrihind_viii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/12)*8):
            ruutmeetrihind_iix_vahemik += 1

hind_i_vahemik = 0
hind_ii_vahemik = 0
hind_iii_vahemik = 0
hind_iv_vahemik = 0
hind_v_vahemik = 0
hind_vi_vahemik = 0
hind_vii_vahemik = 0
for i in range(len(hind)):
    hind[i] = float(hind[i])
hinnamax = max(hind)
print(hinnamax)
hind_kokku = 0
hinnaga_kvsid = 0
print(hind)
for i in hind:
    if i != "":
        hind_kokku += float(i)
        hinnaga_kvsid += 1
        if float(i) < (hinnamax/7):
            hind_i_vahemik += 1
        if float(i) >= (hinnamax/7) and float(i) < ((hinnamax/7)*2):
            hind_ii_vahemik += 1
        if float(i) >= ((hinnamax/7)*2) and float(i) < ((hinnamax/7)*3):
            hind_iii_vahemik += 1
        if float(i) >= ((hinnamax/7)*3) and float(i) < ((hinnamax/7)*4):
            hind_iv_vahemik += 1
        if float(i) >= ((hinnamax/7)*4) and float(i) <((hinnamax/7)*5):
            hind_v_vahemik += 1
        if float(i) >= ((hinnamax/7)*5) and float(i) < ((hinnamax/7)*6):
            hind_vi_vahemik += 1
        if float(i) >= ((hinnamax/7)*6):
            hind_vii_vahemik += 1


print("Keskmised:")
print("\tTube keskmiselt: " + str(round((tubasid_kokku/tubadega_kvsid),2)))
print("\tRuutmeetreid keskmiselt: " + str(round((ruutmeetreid_kokku/pindalaga_kvsid),2)) + " m²")
print("\tKeskmine ruutmeetrihind: " + str(round(ruutmeetrihind_kokku/ruutmeetrihinnaga_kvsid,2)) + " €/m²")
print("\tKeskmine hind: " + str(round(hind_kokku/hinnaga_kvsid,2)) + " €")

print()
print("Jaotumine vahemikesse: ")
print("\tTubade arvu alusel: ")
print("\t\tÜhetoalisi kv pakkumisi: " + str(toad.count("1")))
print("\t\tKahetoalisi kv pakkumisi: " + str(toad.count("2")))
print("\t\tKolmetoalisi kv pakkumisi: " + str(toad.count("3")))
print("\t\tNelja ja enamatoalisi kv pakkumisi: " + str(tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3"))))

print("\tPindala alusel: ")
print("\t\tKv pakkumisi pindalaga <20 m²: " + str(alla20))
print("\t\tKv pakkumisi pindalaga >=20 ja <30 m²: " + str(alla30))
print("\t\tKv pakkumisi pindalaga >=30 ja <40 m²: " + str(alla40))
print("\t\tKv pakkumisi pindalaga >=40 ja <50 m²: " + str(alla50))
print("\t\tKv pakkumisi pindalaga >=50 ja <60 m²: " + str(alla60))
print("\t\tKv pakkumisi pindalaga >=60 ja <70 m²: " + str(alla70))
print("\t\tKv pakkumisi pindalaga >=70 ja <80 m²: " + str(alla80))
print("\t\tKv pakkumisi pindalaga >=80 m²: " + str(pindalaga_kvsid-(alla20+alla30+alla40+alla50+alla60+alla70+alla80)))

print("\tRuutmeetri hinna alusel: ")
print("\t\tKv pakkumisi ruutmeetri hinnaga <"+ str(round((ruutmeetrihinnamax/12),2)) + "€/m²: " + str(ruutmeetrihind_i_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round((ruutmeetrihinnamax/12),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*2),2)) +"€/m²: " + str(ruutmeetrihind_ii_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*2),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*3),2)) +"€/m²: " + str(ruutmeetrihind_iii_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*3),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*4),2)) +"€/m²: " + str(ruutmeetrihind_iv_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*4),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*5),2)) +"€/m²: " + str(ruutmeetrihind_v_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*5),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),2)) +"€/m²: " + str(ruutmeetrihind_vi_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*6),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*7),2)) +"€/m²: " + str(ruutmeetrihind_vii_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >=" + str(round(((ruutmeetrihinnamax/12)*7),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*8),2)) +"€/m²: " + str(ruutmeetrihind_viii_vahemik))
print("\t\tKv pakkumisi ruutmeetri hinnaga >="+str(round(((ruutmeetrihinnamax/12)*8),2)) + "€/m²: " + str(ruutmeetrihind_iix_vahemik))

print("\tHinna alusel: ")
print("\t\tKv pakkumisi hinnaga <"+str(round((hinnamax/7),2))   + " €: " + str(hind_i_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round((hinnamax/7),2))   +" ja <"+str(round(((hinnamax/7)*2),2)) +" €: " + str(hind_ii_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*2),2))   +" ja <"+str(round(((hinnamax/7)*3),2)) +" €: " + str(hind_iii_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*3),2))   +" ja <"+str(round(((hinnamax/7)*4),2)) +" €: " + str(hind_iv_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*4),2))   +" ja <"+str(round(((hinnamax/7)*5),2)) +" €: " + str(hind_v_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*5),2))   +" ja <"+str(round(((hinnamax/7)*6),2)) +" €: " + str(hind_vi_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*6),2)) + " €: " + str(hind_vii_vahemik))

# impordi tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk

# see funktsioon käivitatakse nupule klõpsamisel
def arvuta():
    tahvel = Canvas(raam, width=550, height=400, highlightthickness=0, background="Gray91")
    tahvel.place(x=1, y=250)
    frame2=ttk.Frame(raam)
    frame2.place(x=1,y=480,height=300, width=450)
    if soovitudgraafik.get() == "hind":
        sektor_hind_i_vahemik = tahvel.create_arc(225,225,10,10,fill="red", extent = (hind_i_vahemik/hinnaga_kvsid)*360)
        sektor_hind_ii_vahemik = tahvel.create_arc(225,225,10,10,fill = "green", start = (hind_i_vahemik/hinnaga_kvsid)*360, extent = (hind_ii_vahemik/hinnaga_kvsid)*360)
        sektor_hind_iii_vahemik = tahvel.create_arc(225,225,10,10,fill="blue", start = ((hind_i_vahemik+hind_ii_vahemik)/hinnaga_kvsid)*360, extent = (hind_iii_vahemik/hinnaga_kvsid)*360)
        sektor_hind_iv_vahemik = tahvel.create_arc(225,225,10,10,fill="grey", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik)/hinnaga_kvsid)*360, extent = (hind_iv_vahemik/hinnaga_kvsid)*360)
        sektor_hind_v_vahemik = tahvel.create_arc(225,225,10,10,fill="brown", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik)/hinnaga_kvsid)*360, extent = (hind_v_vahemik/hinnaga_kvsid)*360)
        sektor_hind_vi_vahemik = tahvel.create_arc(225,225,10,10,fill="black", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik+hind_v_vahemik)/hinnaga_kvsid)*360, extent = (hind_vi_vahemik/hinnaga_kvsid)*360)
        sektor_hind_vii_vahemik = tahvel.create_arc(225,225,10,10,fill="pink", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik+hind_v_vahemik+hind_vi_vahemik)/hinnaga_kvsid)*360, extent = (hind_vii_vahemik/hinnaga_kvsid)*360)
        label_hind_i_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga <" +str(round((hinnamax/7),2))   +" €: " + str(hind_i_vahemik), font=("Helvetica",15), foreground="red")
        label_hind_i_vahemik.place(x=10, y=480)
        label_hind_ii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >="+str(round((hinnamax/7),2)) +" ja <"+str(round(((hinnamax/7)*2),2))+" €: " + str(hind_ii_vahemik), font=("Helvetica",15), foreground="green")
        label_hind_ii_vahemik.place(x=10, y=500)
        label_hind_iii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*2),2))+" ja <"+str(round(((hinnamax/7)*3),2)) +" €: " + str(hind_iii_vahemik), font=("Helvetica",15), foreground="blue")
        label_hind_iii_vahemik.place(x=10, y=520)
        label_hind_iv_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*3),2))+" ja <"+str(round(((hinnamax/7)*4),2)) +" €: " + str(hind_iv_vahemik), font=("Helvetica",15), foreground="grey")
        label_hind_iv_vahemik.place(x=10, y=540)
        label_hind_v_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*4),2))+" ja <"+str(round(((hinnamax/7)*5),2)) +" €: " + str(hind_v_vahemik), font=("Helvetica",15), foreground="brown")
        label_hind_v_vahemik.place(x=10, y=560)
        label_hind_vi_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*5),2))+" ja <"+str(round(((hinnamax/7)*6),2)) +" €: "+ str(hind_vi_vahemik), font=("Helvetica",15), foreground="black")
        label_hind_vi_vahemik.place(x=10, y=580)
        label_hind_vii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >="+str(round(((hinnamax/7)*6),2)) +" €: " + str(hind_vii_vahemik), font=("Helvetica",15), foreground="pink")
        label_hind_vii_vahemik.place(x=10, y=600)
    if soovitudgraafik.get() == "ruutmeetrihind":
        sektor_ruutmeetrihind_i_vahemik = tahvel.create_arc(225,225,10,10,fill="red", extent = (ruutmeetrihind_i_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_ii_vahemik = tahvel.create_arc(225,225,10,10,fill = "green", start = (ruutmeetrihind_i_vahemik/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_ii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_iii_vahemik = tahvel.create_arc(225,225,10,10,fill="blue", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_iii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_iv_vahemik = tahvel.create_arc(225,225,10,10,fill="grey", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_iv_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_v_vahemik = tahvel.create_arc(225,225,10,10,fill="brown", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_v_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_vi_vahemik = tahvel.create_arc(225,225,10,10,fill="black", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_vi_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_vii_vahemik = tahvel.create_arc(225,225,10,10,fill="pink", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_vii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_viii_vahemik = tahvel.create_arc(225,225,10,10,fill="magenta", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik+ruutmeetrihind_vii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_viii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_iix_vahemik = tahvel.create_arc(225,225,10,10,fill="aliceblue", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik+ruutmeetrihind_vii_vahemik+ruutmeetrihind_viii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = ((ruutmeetrihind_iix_vahemik)/ruutmeetrihinnaga_kvsid)*360)
        label_ruutmeetrihind_i_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga"+str(round((ruutmeetrihinnamax/12),2))+ "€/m²: " + str(ruutmeetrihind_i_vahemik), font=("Helvetica",15), foreground="red")
        label_ruutmeetrihind_i_vahemik.place(x=10, y=480)
        label_ruutmeetrihind_ii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round((ruutmeetrihinnamax/12),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*2),2)) +"€/m²: " + str(ruutmeetrihind_ii_vahemik), font=("Helvetica",15), foreground="green")
        label_ruutmeetrihind_ii_vahemik.place(x=10, y=500)
        label_ruutmeetrihind_iii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*2),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*3),2)) +"€/m²: " + str(ruutmeetrihind_iii_vahemik), font=("Helvetica",15), foreground="blue")
        label_ruutmeetrihind_iii_vahemik.place(x=10, y=520)
        label_ruutmeetrihind_iv_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*3),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*4),2)) +"€/m²: " + str(ruutmeetrihind_iv_vahemik), font=("Helvetica",15), foreground="grey")
        label_ruutmeetrihind_iv_vahemik.place(x=10, y=540)
        label_ruutmeetrihind_v_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*4),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*5),2)) +"€/m²: " + str(ruutmeetrihind_v_vahemik), font=("Helvetica",15), foreground="brown")
        label_ruutmeetrihind_v_vahemik.place(x=10, y=560)
        label_ruutmeetrihind_vi_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*5),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),2)) +"€/m²: " + str(ruutmeetrihind_vi_vahemik), font=("Helvetica",15), foreground="black")
        label_ruutmeetrihind_vi_vahemik.place(x=10, y=580)
        label_ruutmeetrihind_vii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*5),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),2)) +"€/m²: " + str(ruutmeetrihind_vii_vahemik), font=("Helvetica",15), foreground="pink")
        label_ruutmeetrihind_vii_vahemik.place(x=10, y=600)
        label_ruutmeetrihind_viii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*6),2))+" ja "+ str(round(((ruutmeetrihinnamax/12)*7),2)) +"€/m²: " + str(ruutmeetrihind_viii_vahemik), font=("Helvetica",15), foreground="magenta")
        label_ruutmeetrihind_viii_vahemik.place(x=10, y=620)
        label_ruutmeetrihind_iix_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >="+ str(round(((ruutmeetrihinnamax/12)*7),2)) +"€/m²: " + str(ruutmeetrihind_iix_vahemik), font=("Helvetica",15), foreground="aliceblue")
        label_ruutmeetrihind_iix_vahemik.place(x=10, y=640)
    if soovitudgraafik.get() == "pindala":
        sektor_alla20 = tahvel.create_arc(225,225,10,10,fill="red", extent = (alla20/pindalaga_kvsid)*360)
        sektor_alla30 = tahvel.create_arc(225,225,10,10,fill = "green", start = (alla20/pindalaga_kvsid)*360, extent = (alla30/pindalaga_kvsid)*360)
        sektor_alla40 = tahvel.create_arc(225,225,10,10,fill="blue", start = ((alla20+alla30)/pindalaga_kvsid)*360, extent = (alla40/pindalaga_kvsid)*360)
        sektor_alla50 = tahvel.create_arc(225,225,10,10,fill="grey", start = ((alla20+alla30+alla40)/pindalaga_kvsid)*360, extent = (alla50/pindalaga_kvsid)*360)
        sektor_alla60 = tahvel.create_arc(225,225,10,10,fill="brown", start = ((alla20+alla30+alla40+alla50)/pindalaga_kvsid)*360, extent = (alla60/pindalaga_kvsid)*360)
        sektor_alla70 = tahvel.create_arc(225,225,10,10,fill="black", start = ((alla20+alla30+alla40+alla50+alla60)/pindalaga_kvsid)*360, extent = (alla70/pindalaga_kvsid)*360)
        sektor_alla80 = tahvel.create_arc(225,225,10,10,fill="pink", start = ((alla20+alla30+alla40+alla50+alla60+alla70)/pindalaga_kvsid)*360, extent = (alla80/pindalaga_kvsid)*360)
        sektor_yle80 = tahvel.create_arc(225,225,10,10,fill="magenta", start = ((alla20+alla30+alla40+alla50+alla60+alla70+alla80)/pindalaga_kvsid)*360, extent = (pindalaga_kvsid-(alla20+alla30+alla40+alla50+alla60+alla70+alla80)/pindalaga_kvsid)*360)
        labelalla20 = ttk.Label(raam, text="Kv pakkumisi pindalaga <20 m²: " + str(alla20), font=("Helvetica",15), foreground="red")
        labelalla20.place(x=10, y=480)
        labelalla30 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=20 ja <30 m²: " + str(alla30), font=("Helvetica",15), foreground="green")
        labelalla30.place(x=10, y=500)
        labelalla40 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=30 ja <40 m²: " + str(alla40), font=("Helvetica",15), foreground="blue")
        labelalla40.place(x=10, y=520)
        labelalla50 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=40 ja <50 m²: " + str(alla50), font=("Helvetica",15), foreground="grey")
        labelalla50.place(x=10, y=540)
        labelalla60 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=50 ja <60 m²: " + str(alla60), font=("Helvetica",15), foreground="brown")
        labelalla60.place(x=10, y=560)
        labelalla70 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=60 ja <70 m²: " + str(alla70), font=("Helvetica",15), foreground="black")
        labelalla70.place(x=10, y=580)
        labelalla80 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=70 ja <80 m²: " + str(alla80), font=("Helvetica",15), foreground="pink")
        labelalla80.place(x=10, y=600)
        labelyle80 = ttk.Label(raam, text="Kv pakkumisi pindalaga >=80 m²: " + str(pindalaga_kvsid-(alla20+alla30+alla40+alla50+alla60+alla70+alla80)), font=("Helvetica",15), foreground="magenta")
        labelyle80.place(x=10, y=620)
    if soovitudgraafik.get() == "tubade arv":
        sektor1 = tahvel.create_arc(225,225,10,10,fill="red", extent = (toad.count("1")/tubadega_kvsid)*360)
        sektor2 = tahvel.create_arc(225,225,10,10,fill = "green", start = (toad.count("1")/tubadega_kvsid)*360, extent = (toad.count("2")/tubadega_kvsid)*360)
        sektor3 = tahvel.create_arc(225,225,10,10,fill="blue", start = ((toad.count("1")+toad.count("2"))/tubadega_kvsid)*360, extent = (toad.count("3")/tubadega_kvsid)*360)
        sektor4 = tahvel.create_arc(225,225,10,10,fill="grey", start = (((toad.count("1")+(toad.count("2")+(toad.count("3")))))/tubadega_kvsid)*360, extent = (toad.count("4")/tubadega_kvsid)*360)
        sektor_yle4 = tahvel.create_arc(225,225,10,10,fill="brown", start = ((((toad.count("1")+toad.count("2")+toad.count("3")+toad.count("4"))))/tubadega_kvsid)*360, extent = ((tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3")+
toad.count("4")))/tubadega_kvsid)*360)
        label_1 = ttk.Label(raam, text="Ühetoalisi kv pakkumisi: " + str(toad.count("1")), font=("Helvetica",15), foreground="red")
        label_1.place(x=10, y=480)
        label_2 = ttk.Label(raam, text="Kahetoalisi kv pakkumisi: " + str(toad.count("2")), font=("Helvetica",15), foreground="green")
        label_2.place(x=10, y=500)
        label_3 = ttk.Label(raam, text="Kolmetoalisi kv pakkumisi: " + str(toad.count("3")), font=("Helvetica",15), foreground="blue")
        label_3.place(x=10, y=520)
        label_4 = ttk.Label(raam, text="Nelja ja enamatoalisi kv pakkumisi: " + str(tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3"))), font=("Helvetica",15), foreground="grey")
        label_4.place(x=10, y=540)

# loome akna
raam = Tk()
raam.title("Sektordiagramm")
raam.geometry("450x700")

frame=ttk.Frame(raam)
frame.place(x=1,y=1,height=700, width=450)

soovitudgraafik = StringVar()

soovitudgraafik = ttk.Entry(raam, textvariable = soovitudgraafik)
soovitudgraafik.place(x=50, y=71, width=300)

silt_soovitudgraafik = ttk.Label(raam, text=" Sisesta näitaja, mille põhjal soovid sektordiagrammi\n \
moodustada (tubade arv, hind, ruutmeetrihind või pindala):")
silt_soovitudgraafik.place(x=15, y=15)

# loome nupu
nupp = ttk.Button(raam, text="Moodusta sektordiagramm!", command=arvuta)
nupp.place(x=50, y=110, width=300)

# ilmutame akna ekraanile
raam.mainloop()
