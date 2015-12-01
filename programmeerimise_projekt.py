__author__ = 'erkiaun'

import requests
from bs4 import BeautifulSoup

url = "http://www.kv.ee/?act=search.simple&company_id=&page=1&orderby=ob&page_size=&deal_type=2&dt_select=2&county=1&parish=&price_min=&price_max=&price_type=1&rooms_min=&rooms_max=&area_min=&area_max=&floor_min=&floor_max=&keyword="
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
        ruutmeetrihind.append(item.contents[11].find("span", attrs={"class":"object-m2-price"}).text.strip()[0:-5])
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


alla5 = 0
alla6 = 0
alla7 = 0
alla8 = 0
alla9 = 0
alla10 = 0
alla11 = 0
alla12 = 0
yle12 = 0
ruutmeetrihind_kokku = 0
ruutmeetrihinnaga_kvsid = 0
for i in ruutmeetrihind:
    if i != "0":
        ruutmeetrihind_kokku += float(i)
        ruutmeetrihinnaga_kvsid += 1
        if float(i) > 0 and float(i)<5:
            alla5 += 1
        if float(i) >= 5 and float(i)<6:
            alla6 += 1
        if float(i) >= 6 and float(i)<7:
            alla7 += 1
        if float(i) >= 7 and float(i)<8:
            alla8 += 1
        if float(i) >= 8 and float(i)<9:
            alla9 += 1
        if float(i) >= 9 and float(i)<10:
            alla10 += 1
        if float(i) >= 10 and float(i)<11:
            alla11 += 1
        if float(i) >= 11 and float(i)<12:
            alla12 += 1
        if float(i) >= 12:
            yle12 += 1

alla200 = 0
alla300 = 0
alla400 = 0
alla500 = 0
alla600 = 0
alla700 = 0
yle700 = 0
hind_kokku = 0
hinnaga_kvsid = 0
for i in hind:
    if i != "":
        hind_kokku += float(i)
        hinnaga_kvsid += 1
        if float(i) < 200:
            alla200 += 1
        if float(i) >= 200 and float(i) < 300:
            alla300 += 1
        if float(i) >= 300 and float(i) < 400:
            alla400 += 1
        if float(i) >= 400 and float(i) < 500:
            alla500 += 1
        if float(i) >= 500 and float(i) <600:
            alla600 += 1
        if float(i) >= 600 and float(i) < 700:
            alla700 += 1
        if float(i) >= 700:
            yle700 += 1


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
print("\t\tKv pakkumisi ruutmeetri hinnaga < 5 €/m²: " + str(alla5))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 5 ja <6 €/m²: " + str(alla6))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 6 ja <7 €/m²: " + str(alla7))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 7 ja <8 €/m²: " + str(alla8))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 8 ja <9 €/m²: " + str(alla9))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 9 ja <10 €/m²: " + str(alla10))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 10 ja <11 €/m²: " + str(alla11))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 11 ja <12 €/m²: " + str(alla12))
print("\t\tKv pakkumisi ruutmeetri hinnaga >= 12 €/m²: " + str(yle12))

print("\tHinna alusel: ")
print("\t\tKv pakkumisi hinnaga < 200 €: " + str(alla200))
print("\t\tKv pakkumisi hinnaga >=200 ja <300 €: " + str(alla300))
print("\t\tKv pakkumisi hinnaga >=300 ja <400 €: " + str(alla400))
print("\t\tKv pakkumisi hinnaga >=400 ja <500 €: " + str(alla500))
print("\t\tKv pakkumisi hinnaga >=500 ja <600 €: " + str(alla600))
print("\t\tKv pakkumisi hinnaga >=600 ja <700 €: " + str(alla700))
print("\t\tKv pakkumisi hinnaga >=700 €: " + str(yle700))

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
        sektor_alla200 = tahvel.create_arc(225,225,10,10,fill="red", extent = (alla200/hinnaga_kvsid)*360)
        sektor_alla300 = tahvel.create_arc(225,225,10,10,fill = "green", start = (alla200/hinnaga_kvsid)*360, extent = (alla300/hinnaga_kvsid)*360)
        sektor_alla400 = tahvel.create_arc(225,225,10,10,fill="blue", start = ((alla200+alla300)/hinnaga_kvsid)*360, extent = (alla400/hinnaga_kvsid)*360)
        sektor_alla500 = tahvel.create_arc(225,225,10,10,fill="grey", start = ((alla200+alla300+alla400)/hinnaga_kvsid)*360, extent = (alla500/hinnaga_kvsid)*360)
        sektor_alla600 = tahvel.create_arc(225,225,10,10,fill="brown", start = ((alla200+alla300+alla400+alla500)/hinnaga_kvsid)*360, extent = (alla600/hinnaga_kvsid)*360)
        sektor_alla700 = tahvel.create_arc(225,225,10,10,fill="black", start = ((alla200+alla300+alla400+alla500+alla600)/hinnaga_kvsid)*360, extent = (alla700/hinnaga_kvsid)*360)
        sektor_yle700 = tahvel.create_arc(225,225,10,10,fill="pink", start = ((alla200+alla300+alla400+alla500+alla600+alla700)/hinnaga_kvsid)*360, extent = (yle700/hinnaga_kvsid)*360)
        labelalla200 = ttk.Label(raam, text="Kv pakkumisi hinnaga < 200 €: " + str(alla200), font=("Helvetica",15), foreground="red")
        labelalla200.place(x=10, y=480)
        labelalla300 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=200 ja <300 €: " + str(alla300), font=("Helvetica",15), foreground="green")
        labelalla300.place(x=10, y=500)
        labelalla400 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=300 ja <400 €: " + str(alla400), font=("Helvetica",15), foreground="blue")
        labelalla400.place(x=10, y=520)
        labelalla500 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=400 ja <500 €: " + str(alla500), font=("Helvetica",15), foreground="grey")
        labelalla500.place(x=10, y=540)
        labelalla600 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=500 ja <600 €: " + str(alla600), font=("Helvetica",15), foreground="brown")
        labelalla600.place(x=10, y=560)
        labelalla700 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=600 ja <700 €: " + str(alla700), font=("Helvetica",15), foreground="black")
        labelalla700.place(x=10, y=580)
        labelyle700 = ttk.Label(raam, text="Kv pakkumisi hinnaga >=700: " + str(yle700), font=("Helvetica",15), foreground="pink")
        labelyle700.place(x=10, y=600)
    if soovitudgraafik.get() == "ruutmeetrihind":
        sektor_alla5 = tahvel.create_arc(225,225,10,10,fill="red", extent = (alla5/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla6 = tahvel.create_arc(225,225,10,10,fill = "green", start = (alla5/ruutmeetrihinnaga_kvsid)*360, extent = (alla6/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla7 = tahvel.create_arc(225,225,10,10,fill="blue", start = ((alla5+alla6)/ruutmeetrihinnaga_kvsid)*360, extent = (alla7/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla8 = tahvel.create_arc(225,225,10,10,fill="grey", start = ((alla5+alla6+alla7)/ruutmeetrihinnaga_kvsid)*360, extent = (alla8/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla9 = tahvel.create_arc(225,225,10,10,fill="brown", start = ((alla5+alla6+alla7+alla8)/ruutmeetrihinnaga_kvsid)*360, extent = (alla9/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla10 = tahvel.create_arc(225,225,10,10,fill="black", start = ((alla5+alla6+alla7+alla8+alla9)/ruutmeetrihinnaga_kvsid)*360, extent = (alla10/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla11 = tahvel.create_arc(225,225,10,10,fill="pink", start = ((alla5+alla6+alla7+alla8+alla9+alla10)/ruutmeetrihinnaga_kvsid)*360, extent = (alla11/ruutmeetrihinnaga_kvsid)*360)
        sektor_alla12 = tahvel.create_arc(225,225,10,10,fill="magenta", start = ((alla5+alla6+alla7+alla8+alla9+alla10+alla11)/ruutmeetrihinnaga_kvsid)*360, extent = (alla12/ruutmeetrihinnaga_kvsid)*360)
        sektor_yle12 = tahvel.create_arc(225,225,10,10,fill="aliceblue", start = ((alla5+alla6+alla7+alla8+alla9+alla10+alla11+alla12)/ruutmeetrihinnaga_kvsid)*360, extent = ((yle12)/ruutmeetrihinnaga_kvsid)*360)
        labelalla5 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga < 5 €/m²: " + str(alla5), font=("Helvetica",15), foreground="red")
        labelalla5.place(x=10, y=480)
        labelalla6 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 5 ja <6 €/m²: " + str(alla6), font=("Helvetica",15), foreground="green")
        labelalla6.place(x=10, y=500)
        labelalla7 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 6 ja <7 €/m²: " + str(alla7), font=("Helvetica",15), foreground="blue")
        labelalla7.place(x=10, y=520)
        labelalla8 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 7 ja <8 €/m²: " + str(alla8), font=("Helvetica",15), foreground="grey")
        labelalla8.place(x=10, y=540)
        labelalla9 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 8 ja <9 €/m²: " + str(alla9), font=("Helvetica",15), foreground="brown")
        labelalla9.place(x=10, y=560)
        labelalla10 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 9 ja <10 €/m²: " + str(alla10), font=("Helvetica",15), foreground="black")
        labelalla10.place(x=10, y=580)
        labelalla11 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 10 ja <11 €/m²: " + str(alla11), font=("Helvetica",15), foreground="pink")
        labelalla11.place(x=10, y=600)
        labelalla12 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 11 ja <12 €/m²: " + str(alla12), font=("Helvetica",15), foreground="magenta")
        labelalla12.place(x=10, y=620)
        labelyle12 = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >= 12 €/m²: " + str(yle12), font=("Helvetica",15), foreground="aliceblue")
        labelyle12.place(x=10, y=640)
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
