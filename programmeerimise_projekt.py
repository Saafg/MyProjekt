__author__ = 'erkiaun'

#Impordin vajalikud moodulid
import requests
from bs4 import BeautifulSoup


#Kasutan kv.ee url-i ja imporditud mooduleid, et luua listid, mis sisaldavad maakondade nimesid ja maakondade id-sid (list_maakonna_nimi ja list_maakonna_id).
url = "http://www.kv.ee/?act=search.simple&company_id=&page=1&orderby=ob&page_size=100&deal_type=1&dt_select=1&county=0&parish=&price_min=&price_max=&price_type=1&rooms_min=&rooms_max=&area_min=&area_max=&floor_min=&floor_max=&keyword="

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("select", attrs={"id":"county"})

list_maakonna_id = []

for item in data:
    list_maakonna_nimi = (item.text).split()

list_maakonna_nimi[0] = ""

for item in data:
    data2 = item.find_all("option")

for item in data2:
    list_maakonna_id.append(item.get("value"))


#Listid valdade või linnade nimedega ja neile vastavate id-dega.
list_valla_nimi = ["",'Aegviidu vald', 'Anija vald', 'Harku vald', 'Jõelähtme vald', 'Keila', 'Keila vald', 'Kernu vald', 'Kiili vald', 'Kose vald', 'Kuusalu vald', 'Loksa', 'Maardu', 'Nissi vald', 'Padise vald', 'Paldiski', 'Raasiku vald', 'Rae vald', 'Saku vald', 'Saue', 'Saue vald', 'Tallinn', 'Vasalemma vald', 'Viimsi vald', 'Emmaste vald', 'Hiiu vald', 'Käina vald', 'Pühalepa vald', 'Alajõe vald', 'Aseri vald', 'Avinurme vald', 'Iisaku vald', 'Illuka vald', 'Jõhvi vald', 'Kiviõli', 'Kohtla-Järve', 'Kohtla-Nõmme vald', 'Kohtla vald', 'Lohusuu vald', 'Lüganuse vald', 'Mäetaguse vald', 'Narva', 'Narva-Jõesuu', 'Sillamäe', 'Sonda vald', 'Toila vald', 'Tudulinna vald', 'Vaivara vald', 'Jõgeva', 'Jõgeva vald', 'Kasepää vald', 'Mustvee', 'Pajusi vald', 'Palamuse vald', 'Pala vald', 'Puurmani vald', 'Põltsamaa', 'Põltsamaa vald', 'Saare vald', 'Tabivere vald', 'Torma vald', 'Albu vald', 'Ambla vald', 'Imavere vald', 'Järva-Jaani vald', 'Kareda vald', 'Koeru vald', 'Koigi vald', 'Paide', 'Paide vald', 'Roosna-Alliku vald', 'Türi vald', 'Väätsa vald', 'Haapsalu', 'Hanila vald', 'Kullamaa vald', 'Lihula vald', 'Lääne-Nigula vald', 'Martna vald', 'Noarootsi vald', 'Nõva vald', 'Ridala vald', 'Vormsi vald', 'Haljala vald', 'Kadrina vald', 'Kunda', 'Laekvere vald', 'Rakke vald', 'Rakvere', 'Rakvere vald', 'Rägavere vald', 'Sõmeru vald', 'Tamsalu vald', 'Tapa vald', 'Vihula vald', 'Vinni vald', 'Viru-Nigula vald', 'Väike-Maarja vald', 'Are vald', 'Audru vald', 'Halinga vald', 'Häädemeeste vald', 'Kihnu vald', 'Koonga vald', 'Paikuse vald', 'Pärnu', 'Saarde vald', 'Sauga vald', 'Sindi', 'Surju vald', 'Tahkuranna vald', 'Tootsi vald', 'Tori vald', 'Tõstamaa vald', 'Varbla vald', 'Vändra vald', 'Vändra vald (alev)', 'Juuru vald', 'Järvakandi vald', 'Kaiu vald', 'Kehtna vald', 'Kohila alevi vald', 'Kohila vald', 'Käru vald', 'Märjamaa vald', 'Raikküla vald', 'Rapla vald', 'Vigala vald', 'Kihelkonna vald', 'Kuressaare', 'Laimjala vald', 'Leisi vald', 'Lääne-Saare vald', 'Muhu vald', 'Mustjala vald', 'Orissaare vald', 'Pihtla vald', 'Pöide vald', 'Ruhnu vald', 'Salme vald', 'Torgu vald', 'Valjala vald', 'Alatskivi vald', 'Elva', 'Haaslava vald', 'Kallaste', 'Kambja vald', 'Konguta vald', 'Laeva vald', 'Luunja vald', 'Meeksi vald', 'Mäksa vald', 'Nõo vald', 'Peipsiääre vald', 'Piirissaare vald', 'Puhja vald', 'Rannu vald', 'Rõngu vald', 'Tartu', 'Tartu vald', 'Tähtvere vald', 'Vara vald', 'Võnnu vald', 'Ülenurme vald', 'Helme vald', 'Hummuli vald', 'Karula vald', 'Otepää vald', 'Palupera vald', 'Puka vald', 'Põdrala vald', 'Sangaste vald', 'Taheva vald', 'Tõlliste vald', 'Tõrva', 'Valga', 'Õru vald', 'Abja vald', 'Halliste vald', 'Karksi vald', 'Kolga-Jaani vald', 'Kõo vald', 'Kõpu vald', 'Mõisaküla', 'Suure-Jaani vald', 'Tarvastu vald', 'Viljandi', 'Viljandi vald', 'Võhma', 'Antsla vald', 'Haanja vald', 'Lasva vald', 'Meremäe vald', 'Misso vald', 'Mõniste vald', 'Rõuge vald', 'Sõmerpalu vald', 'Urvaste vald', 'Varstu vald', 'Vastseliina vald', 'Võru', 'Võru vald']
list_valla_id = ["0",'1', '2', '3', '4', '416', '5', '6', '7', '8', '9', '417', '418', '12', '13', '419', '14', '15', '16', '420', '17', '421', '18', '19', '20', '614', '22', '23', '24', '25', '26', '27', '28', '29', '424', '425', '31', '30', '32', '33', '35', '426', '427', '429', '36', '37', '38', '39', '430', '40', '46', '431', '41', '43', '42', '44', '432', '45', '47', '48', '49', '50', '51', '52', '53', '55', '56', '57', '433', '60', '61', '62', '63', '435', '64', '65', '66', '615', '67', '68', '69', '71', '74', '76', '77', '437', '78', '79', '438', '80', '81', '83', '84', '608', '85', '86', '87', '89', '103', '104', '105', '106', '108', '109', '111', '444', '112', '113', '445', '114', '115', '117', '118', '119', '120', '121', '122', '123', '124', '125', '126', '128', '127', '129', '131', '133', '134', '135', '137', '447', '140', '141', '618', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '448', '153', '449', '154', '155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '450', '166', '167', '168', '169', '170', '171', '172', '173', '177', '174', '175', '176', '178', '179', '180', '452', '453', '181', '182', '183', '184', '185', '186', '187', '455', '192', '193', '457', '616', '458', '196', '197', '198', '199', '200', '201', '202', '203', '204', '205', '206', '460', '207']

#Inputid otsingukriteeriumite sätestamiseks. Kohustuslik on sisestada kinnisvara tüüp ja tehingu tüüp. Ülejäänud võib vastamata jätta
#vajutades Enterit.
maakond = input("Sisesta maakond otsitava kv jaoks (kui ei soovi täpsustada, vajuta Enter): ")
while maakond not in list_maakonna_nimi:
    maakond = input("Proovi sisestada maakonna nimi uuesti (kujul Harjumaa, Ida-Virumaa, Jõgevamaa, Järvamaa, Läänemaa, Lääne-Virumaa, Põlvamaa, Pärnumaa või Raplamaa): ")

vald = input("Sisesta vald või linn otsitava kv jaoks (kui ei soovi täpsustada, vajuta Enter): ")
while vald not in list_valla_nimi:
    vald = input("Vabandust, kuid sellise kirjapiliga vald või asula puudub listist. Proovi uuesti või kui ei soovi täpsustada, vajuta Enter!): ")


kv_tyyp = input("Sisesta otsitava kinnisvara tüüp (korter või maja): ")
while kv_tyyp != "korter" and kv_tyyp != "maja":
    kv_tyyp = input("Sisesta korrektselt otsitava kinnisvara tüüp (korter või maja): ")

tehing =  input("Sisesta huvipakkuva tehingu tüüp (müük, üür või kõik): ")
while tehing != "müük" and tehing != "üür" and tehing != "kõik":
    tehing =  input("Sisesta palun korrektselt tehingu tüüp(müük, üür või kõik): ")
if tehing == "müük":
    if kv_tyyp == "korter":
        tehing = "1"
    if kv_tyyp == "maja":
        tehing = "3"
if tehing == "üür":
    if kv_tyyp == "korter":
        tehing = "2"
    if kv_tyyp == "maja":
        tehing = "4"
if tehing == "kõik":
    if kv_tyyp == "korter":
        tehing = "20"
    if kv_tyyp == "maja":
        tehing = "21"

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


#Url-i modifitseerimine vastavalt saadud input-dele.
url = url.replace(url[url.find("county="):url.find("&parish=")],"county="+list_maakonna_id[list_maakonna_nimi.index(maakond)])
url = url.replace(url[url.find("parish="):url.find("&price_min=")],"parish="+list_valla_id[list_valla_nimi.index(vald)])
url = url.replace(url[url.find("deal_type"):url.find("deal_type")+23],"deal_type="+tehing+"&dt_select="+tehing)
url = url.replace("rooms_min=","rooms_min="+toad_min)
url = url.replace("rooms_max=","rooms_max="+toad_max)
url = url.replace("price_max=","price_max="+hind_max)
url = url.replace("price_min=","price_min="+hind_min)

#Imporditud moodulite rakendamine, sobivaks modifitseeritud url-i peal. Vastavalt sellele, kas soovitakse kortereid või maju, otsin
#html tabeli ridu, mille atribuut class on vastavalt "object-type-apartment" või "object-type-house". Tabeli real peab olema olemas
#atribuut "id".

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

if kv_tyyp == "korter":
    data = soup.find_all("tr", attrs={"class":"object-type-apartment", "id":True})
else:
    data = soup.find_all("tr", attrs={"class":"object-type-house", "id":True})

#Loon tühjad listid, kuhu hakkan neile järgnevas tsüklis koguma korterite vastavaid andmeid.
toad = []
ruutmeetreid = []
ruutmeetrihind = []
hind = []
piirkond = []

for item in data:
        print()
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

#Kuna igal kv pakkumisel peab olema märgitud hind, siis kasutan tühja hinna listi selleks, et tekitada veateade puhuks kui ükski
#kv pakkumine ei vasta sisestatud otsingukriteeriumitele.
if len(hind) == 0:
    raise Exception("Sisestatud kriteeriumitele ei vasta ükski kinnisvara pakkumine!")

#Märgitud tubade arvuga kv-de ülelugemine, et arvutada keskmist tubade arvu kv kohta.
tubasid_kokku = 0
tubadega_kvsid = 0
for i in toad:
    if i != "":
        tubasid_kokku += int(i)
        tubadega_kvsid += 1

#Märgitud pindalaga kv-de ülelugemine, et arvutada keskmist pindala kv kohta. Samuti loon maksimaalse pindalaga kv-st sõltuvalt
#seitse võrdset vahemikku ning loen üle, kui palju kv pakkumisi igasse vahemikku jääb.
ruutmeetreid_kokku = 0
pindalaga_kvsid = 0
pindala_i_vahemik = 0
pindala_ii_vahemik = 0
pindala_iii_vahemik = 0
pindala_iv_vahemik = 0
pindala_v_vahemik = 0
pindala_vi_vahemik = 0
pindala_vii_vahemik = 0
pindalamax = 0
for i in range(len(ruutmeetreid)):
    if ruutmeetreid[i] != "":
        ruutmeetreid[i] = float(ruutmeetreid[i])
        if ruutmeetreid[i] > pindalamax:
            pindalamax = ruutmeetreid[i]
for i in ruutmeetreid:
    if i != "":
        if float(i) < (pindalamax/7):
            pindala_i_vahemik += 1
        if float(i) >= (pindalamax/7) and float(i)<((pindalamax/7)*2):
            pindala_ii_vahemik += 1
        if float(i) >= ((pindalamax/7)*2) and float(i)<((pindalamax/7)*3):
            pindala_iii_vahemik += 1
        if float(i) >= ((pindalamax/7)*3) and float(i)<((pindalamax/7)*4):
            pindala_iv_vahemik += 1
        if float(i) >= ((pindalamax/7)*4) and float(i)<((pindalamax/7)*5):
            pindala_v_vahemik += 1
        if float(i) >= ((pindalamax/7)*5) and float(i)<((pindalamax/7)*6):
            pindala_vi_vahemik += 1
        if float(i) >= ((pindalamax/7)*6):
            pindala_vii_vahemik += 1
        ruutmeetreid_kokku += float(i)
        pindalaga_kvsid += 1


#Märgitud ruutmeetrihinnaga kv-de ülelugemine, et arvutada keskmist ruutmeetrihinda kv kohta. Samuti loon maksimaalse ruutmeetrihinnaga
#kv-st sõltuvalt üheksa võrdset vahemikku ning loen üle, kui palju kv pakkumisi igasse vahemikku jääb.
ruutmeetrihind_i_vahemik = 0
ruutmeetrihind_ii_vahemik = 0
ruutmeetrihind_iii_vahemik = 0
ruutmeetrihind_iv_vahemik = 0
ruutmeetrihind_v_vahemik = 0
ruutmeetrihind_vi_vahemik = 0
ruutmeetrihind_vii_vahemik = 0
ruutmeetrihind_viii_vahemik = 0
ruutmeetrihind_ix_vahemik = 0
ruutmeetrihinnamax = 0
for i in range(len(ruutmeetrihind)):
    if ruutmeetrihind[i] != "":
        ruutmeetrihind[i] = float(ruutmeetrihind[i])
        if ruutmeetrihind[i] > ruutmeetrihinnamax:
            ruutmeetrihinnamax = ruutmeetrihind[i]
ruutmeetrihind_kokku = 0
ruutmeetrihinnaga_kvsid = 0
for i in ruutmeetrihind:
    if i != 0 and i != "":
        ruutmeetrihind_kokku += float(i)
        ruutmeetrihinnaga_kvsid += 1
        if float(i) > 0 and float(i)<(ruutmeetrihinnamax/8):
            ruutmeetrihind_i_vahemik += 1
        if float(i) >= (ruutmeetrihinnamax/8) and float(i)<((ruutmeetrihinnamax/8)*2):
            ruutmeetrihind_ii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*2) and float(i)<((ruutmeetrihinnamax/8)*3):
            ruutmeetrihind_iii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*3) and float(i)<((ruutmeetrihinnamax/8)*4):
            ruutmeetrihind_iv_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*4) and float(i)<((ruutmeetrihinnamax/8)*5):
            ruutmeetrihind_v_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*5) and float(i)<((ruutmeetrihinnamax/8)*6):
            ruutmeetrihind_vi_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*6) and float(i)<((ruutmeetrihinnamax/8)*7):
            ruutmeetrihind_vii_vahemik += 1
        if float(i) >= ((ruutmeetrihinnamax/8)*7):
            ruutmeetrihind_ix_vahemik += 1

#Märgitud hinnaga kv-de ülelugemine, et arvutada keskmist hinda kv kohta. Samuti loon maksimaalse hinnaga kv-st sõltuvalt
#seitse võrdset vahemikku ning loen üle, kui palju kv pakkumisi igasse vahemikku jääb.
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
hind_kokku = 0
hinnaga_kvsid = 0
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

#Väljastan ekraanile arvutatud keskmised kv-dega seotud aruvuliste näitajate kohta.
print("Keskmised:")
print("\tTube keskmiselt: " + str(round((tubasid_kokku/tubadega_kvsid),0)))
print("\tRuutmeetreid keskmiselt: " + str(round((ruutmeetreid_kokku/pindalaga_kvsid),0)) + " m²")
print("\tKeskmine ruutmeetrihind: " + str(round(ruutmeetrihind_kokku/ruutmeetrihinnaga_kvsid,0)) + " €/m²")
print("\tKeskmine hind: " + str(round(hind_kokku/hinnaga_kvsid,0)) + " €")

#Väljastan ekraanile kv-de jaotuse vastavalt tubade arvule.
print()
print("Jaotumine vahemikesse: ")
print("\tTubade arvu alusel: ")
print("\t\tÜhetoalisi kv pakkumisi: " + str(toad.count("1")))
print("\t\tKahetoalisi kv pakkumisi: " + str(toad.count("2")))
print("\t\tKolmetoalisi kv pakkumisi: " + str(toad.count("3")))
print("\t\tNelja ja enamatoalisi kv pakkumisi: " + str(tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3"))))

#Väljastan erkaanile kv-de jaotumise maksimaalse pindala alusel loodud 7-sse võrdsesse vahemikku.
print("\tPindala alusel: ")
print("\t\tKv pakkumisi pindalaga <"+ str(round((pindalamax/7),0)) + "m²: " + str(pindala_i_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round((pindalamax/7),0))+" ja <"+str(round(((pindalamax/7)*2),0))+" m²: " + str(pindala_ii_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round(((pindalamax/7)*2),0))+" ja <"+str(round(((pindalamax/7)*3),0))+" m²: " + str(pindala_iii_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round(((pindalamax/7)*3),0))+" ja <"+str(round(((pindalamax/7)*4),0))+" m²: " + str(pindala_iv_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round(((pindalamax/7)*4),0))+" ja <"+str(round(((pindalamax/7)*5),0))+" m²: " + str(pindala_v_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round(((pindalamax/7)*5),0))+" ja <"+str(round(((pindalamax/7)*6),0))+" m²: " + str(pindala_vi_vahemik))
print("\t\tKv pakkumisi pindalaga >="+str(round(((pindalamax/7)*6),0)) +" m²: " + str(pindala_vii_vahemik))

#Väljastan ekraanile kv-de jaotumise maksimaalse ruutmeetrihinna alusel loodud 8-sse võrdsesse vahemikku.
print("\tRuutmeetri hinna alusel: ")
print("\t\tKv pakkumisi ruutmeetrihinnaga <"+ str(round((ruutmeetrihinnamax/12),0)) + "€/m²: " + str(ruutmeetrihind_i_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round((ruutmeetrihinnamax/12),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*2),0)) +"€/m²: " + str(ruutmeetrihind_ii_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*2),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*3),0)) +"€/m²: " + str(ruutmeetrihind_iii_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*3),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*4),0)) +"€/m²: " + str(ruutmeetrihind_iv_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*4),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*5),0)) +"€/m²: " + str(ruutmeetrihind_v_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*5),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),0)) +"€/m²: " + str(ruutmeetrihind_vi_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*6),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*7),0)) +"€/m²: " + str(ruutmeetrihind_vii_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >=" + str(round(((ruutmeetrihinnamax/12)*7),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*8),0)) +"€/m²: " + str(ruutmeetrihind_viii_vahemik))
print("\t\tKv pakkumisi ruutmeetrihinnaga >="+str(round(((ruutmeetrihinnamax/12)*8),0)) + "€/m²: " + str(ruutmeetrihind_ix_vahemik))

#Väljastan erkraanile kv-de jaotumise maksimaalse hinna alusel loodud 7-sse võrdsesse vahemikku.
print("\tHinna alusel: ")
print("\t\tKv pakkumisi hinnaga <"+str(round((hinnamax/7),0))   + " €: " + str(hind_i_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round((hinnamax/7),0))   +" ja <"+str(round(((hinnamax/7)*2),0)) +" €: " + str(hind_ii_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*2),0))   +" ja <"+str(round(((hinnamax/7)*3),0)) +" €: " + str(hind_iii_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*3),0))   +" ja <"+str(round(((hinnamax/7)*4),0)) +" €: " + str(hind_iv_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*4),0))   +" ja <"+str(round(((hinnamax/7)*5),0)) +" €: " + str(hind_v_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*5),0))   +" ja <"+str(round(((hinnamax/7)*6),0)) +" €: " + str(hind_vi_vahemik))
print("\t\tKv pakkumisi hinnaga >="+str(round(((hinnamax/7)*6),0)) + " €: " + str(hind_vii_vahemik))

#Impordin tk vidinad ja konstandid
from tkinter import *
from tkinter import ttk

#See funktsioon käivitatakse nupule klõpsamisel
def arvuta():
    tahvel = Canvas(raam, width=550, height=400, highlightthickness=0, background="Gray91")
    tahvel.place(x=1, y=250)
    frame2=ttk.Frame(raam)
    frame2.place(x=1,y=480,height=300, width=450)
    #Loon tkinteri aknasse sektordiagrammi kv-de jaotumise kohta loodud hinnavahemikesse. Samuti väljastan antud info kirjalikult.
    if soovitudgraafik.get() == "hind":
        sektor_hind_i_vahemik = tahvel.create_arc(225,225,10,10,fill="red", extent = (hind_i_vahemik/hinnaga_kvsid)*360)
        sektor_hind_ii_vahemik = tahvel.create_arc(225,225,10,10,fill = "green", start = (hind_i_vahemik/hinnaga_kvsid)*360, extent = (hind_ii_vahemik/hinnaga_kvsid)*360)
        sektor_hind_iii_vahemik = tahvel.create_arc(225,225,10,10,fill="blue", start = ((hind_i_vahemik+hind_ii_vahemik)/hinnaga_kvsid)*360, extent = (hind_iii_vahemik/hinnaga_kvsid)*360)
        sektor_hind_iv_vahemik = tahvel.create_arc(225,225,10,10,fill="grey", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik)/hinnaga_kvsid)*360, extent = (hind_iv_vahemik/hinnaga_kvsid)*360)
        sektor_hind_v_vahemik = tahvel.create_arc(225,225,10,10,fill="brown", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik)/hinnaga_kvsid)*360, extent = (hind_v_vahemik/hinnaga_kvsid)*360)
        sektor_hind_vi_vahemik = tahvel.create_arc(225,225,10,10,fill="black", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik+hind_v_vahemik)/hinnaga_kvsid)*360, extent = (hind_vi_vahemik/hinnaga_kvsid)*360)
        sektor_hind_vii_vahemik = tahvel.create_arc(225,225,10,10,fill="pink", start = ((hind_i_vahemik+hind_ii_vahemik+hind_iii_vahemik+hind_iv_vahemik+hind_v_vahemik+hind_vi_vahemik)/hinnaga_kvsid)*360, extent = (hind_vii_vahemik/hinnaga_kvsid)*359.9999)
        label_hind_i_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga <" +str(round((hinnamax/7),0))   +" €: " + str(hind_i_vahemik), font=("Helvetica",15), foreground="red")
        label_hind_i_vahemik.place(x=10, y=480)
        label_hind_ii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >="+str(round((hinnamax/7),0)) +" ja <"+str(round(((hinnamax/7)*2),0))+" €: " + str(hind_ii_vahemik), font=("Helvetica",15), foreground="green")
        label_hind_ii_vahemik.place(x=10, y=500)
        label_hind_iii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*2),0))+" ja <"+str(round(((hinnamax/7)*3),0)) +" €: " + str(hind_iii_vahemik), font=("Helvetica",15), foreground="blue")
        label_hind_iii_vahemik.place(x=10, y=520)
        label_hind_iv_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*3),0))+" ja <"+str(round(((hinnamax/7)*4),0)) +" €: " + str(hind_iv_vahemik), font=("Helvetica",15), foreground="grey")
        label_hind_iv_vahemik.place(x=10, y=540)
        label_hind_v_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*4),0))+" ja <"+str(round(((hinnamax/7)*5),0)) +" €: " + str(hind_v_vahemik), font=("Helvetica",15), foreground="brown")
        label_hind_v_vahemik.place(x=10, y=560)
        label_hind_vi_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >=" +str(round(((hinnamax/7)*5),0))+" ja <"+str(round(((hinnamax/7)*6),0)) +" €: "+ str(hind_vi_vahemik), font=("Helvetica",15), foreground="black")
        label_hind_vi_vahemik.place(x=10, y=580)
        label_hind_vii_vahemik = ttk.Label(raam, text="Kv pakkumisi hinnaga >="+str(round(((hinnamax/7)*6),0)) +" €: " + str(hind_vii_vahemik), font=("Helvetica",15), foreground="pink")
        label_hind_vii_vahemik.place(x=10, y=600)
    #Loon tkinteri aknasse sektordiagrammi kv-de jaotumise kohta loodud ruutmeetrihinnavahemikesse. Samuti väljastan antud info kirjalikult.
    if soovitudgraafik.get() == "ruutmeetrihind":
        sektor_ruutmeetrihind_i_vahemik = tahvel.create_arc(225,225,10,10,fill="red", extent = (ruutmeetrihind_i_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_ii_vahemik = tahvel.create_arc(225,225,10,10,fill = "green", start = (ruutmeetrihind_i_vahemik/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_ii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_iii_vahemik = tahvel.create_arc(225,225,10,10,fill="blue", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_iii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_iv_vahemik = tahvel.create_arc(225,225,10,10,fill="grey", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_iv_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_v_vahemik = tahvel.create_arc(225,225,10,10,fill="brown", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_v_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_vi_vahemik = tahvel.create_arc(225,225,10,10,fill="black", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_vi_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_vii_vahemik = tahvel.create_arc(225,225,10,10,fill="pink", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_vii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_viii_vahemik = tahvel.create_arc(225,225,10,10,fill="magenta", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik+ruutmeetrihind_vii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = (ruutmeetrihind_viii_vahemik/ruutmeetrihinnaga_kvsid)*360)
        sektor_ruutmeetrihind_ix_vahemik = tahvel.create_arc(225,225,10,10,fill="aliceblue", start = ((ruutmeetrihind_i_vahemik+ruutmeetrihind_ii_vahemik+ruutmeetrihind_iii_vahemik+ruutmeetrihind_iv_vahemik+ruutmeetrihind_v_vahemik+ruutmeetrihind_vi_vahemik+ruutmeetrihind_vii_vahemik+ruutmeetrihind_viii_vahemik)/ruutmeetrihinnaga_kvsid)*360, extent = ((ruutmeetrihind_ix_vahemik)/ruutmeetrihinnaga_kvsid)*359.9999)
        label_ruutmeetrihind_i_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga"+str(round((ruutmeetrihinnamax/12),0))+ "€/m²: " + str(ruutmeetrihind_i_vahemik), font=("Helvetica",15), foreground="red")
        label_ruutmeetrihind_i_vahemik.place(x=10, y=480)
        label_ruutmeetrihind_ii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round((ruutmeetrihinnamax/12),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*2),0)) +"€/m²: " + str(ruutmeetrihind_ii_vahemik), font=("Helvetica",15), foreground="green")
        label_ruutmeetrihind_ii_vahemik.place(x=10, y=500)
        label_ruutmeetrihind_iii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*2),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*3),0)) +"€/m²: " + str(ruutmeetrihind_iii_vahemik), font=("Helvetica",15), foreground="blue")
        label_ruutmeetrihind_iii_vahemik.place(x=10, y=520)
        label_ruutmeetrihind_iv_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*3),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*4),0)) +"€/m²: " + str(ruutmeetrihind_iv_vahemik), font=("Helvetica",15), foreground="grey")
        label_ruutmeetrihind_iv_vahemik.place(x=10, y=540)
        label_ruutmeetrihind_v_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*4),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*5),0)) +"€/m²: " + str(ruutmeetrihind_v_vahemik), font=("Helvetica",15), foreground="brown")
        label_ruutmeetrihind_v_vahemik.place(x=10, y=560)
        label_ruutmeetrihind_vi_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*5),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),0)) +"€/m²: " + str(ruutmeetrihind_vi_vahemik), font=("Helvetica",15), foreground="black")
        label_ruutmeetrihind_vi_vahemik.place(x=10, y=580)
        label_ruutmeetrihind_vii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*5),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*6),0)) +"€/m²: " + str(ruutmeetrihind_vii_vahemik), font=("Helvetica",15), foreground="pink")
        label_ruutmeetrihind_vii_vahemik.place(x=10, y=600)
        label_ruutmeetrihind_viii_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >=" +str(round(((ruutmeetrihinnamax/12)*6),0))+" ja "+ str(round(((ruutmeetrihinnamax/12)*7),0)) +"€/m²: " + str(ruutmeetrihind_viii_vahemik), font=("Helvetica",15), foreground="magenta")
        label_ruutmeetrihind_viii_vahemik.place(x=10, y=620)
        label_ruutmeetrihind_ix_vahemik = ttk.Label(raam, text="Kv pakkumisi ruutmeetri hinnaga >="+ str(round(((ruutmeetrihinnamax/12)*7),0)) +"€/m²: " + str(ruutmeetrihind_ix_vahemik), font=("Helvetica",15), foreground="aliceblue")
        label_ruutmeetrihind_ix_vahemik.place(x=10, y=640)
    #Loon tkinteri aknasse sektordiagrammi kv-de jaotumise kohta loodud pindalavahemikesse. Samuti väljastan antud info kirjalikult.
    if soovitudgraafik.get() == "pindala":
        sektor_pindala_i_vahemik = tahvel.create_arc(225,225,10,10,fill="red", extent = (pindala_i_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_ii_vahemik = tahvel.create_arc(225,225,10,10,fill = "green", start = (pindala_i_vahemik/pindalaga_kvsid)*360, extent = (pindala_ii_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_iii_vahemik = tahvel.create_arc(225,225,10,10,fill="blue", start = ((pindala_i_vahemik+pindala_ii_vahemik)/pindalaga_kvsid)*360, extent = (pindala_iii_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_iv_vahemik = tahvel.create_arc(225,225,10,10,fill="grey", start = ((pindala_i_vahemik+pindala_ii_vahemik+pindala_iii_vahemik)/pindalaga_kvsid)*360, extent = (pindala_iv_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_v_vahemik = tahvel.create_arc(225,225,10,10,fill="brown", start = ((pindala_i_vahemik+pindala_ii_vahemik+pindala_iii_vahemik+pindala_iv_vahemik)/pindalaga_kvsid)*360, extent = (pindala_v_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_vi_vahemik = tahvel.create_arc(225,225,10,10,fill="black", start = ((pindala_i_vahemik+pindala_ii_vahemik+pindala_iii_vahemik+pindala_iv_vahemik+pindala_v_vahemik)/pindalaga_kvsid)*360, extent = (pindala_vi_vahemik/pindalaga_kvsid)*360)
        sektor_pindala_vii_vahemik = tahvel.create_arc(225,225,10,10,fill="pink", start = ((pindala_i_vahemik+pindala_ii_vahemik+pindala_iii_vahemik+pindala_iv_vahemik+pindala_v_vahemik+pindala_vi_vahemik)/pindalaga_kvsid)*360, extent = (pindala_vii_vahemik/pindalaga_kvsid)*359.9999)
        label_pindala_i_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga <"+str(round((pindalamax/7),0))+ " m²: " + str(pindala_i_vahemik), font=("Helvetica",15), foreground="red")
        label_pindala_i_vahemik.place(x=10, y=480)
        label_pindala_ii_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >=" +str(round((pindalamax/7),0))+" ja "+ str(round(((pindalamax/7)*2),0)) +"€/m²: " + str(pindala_ii_vahemik), font=("Helvetica",15), foreground="green")
        label_pindala_ii_vahemik.place(x=10, y=500)
        label_pindala_iii_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >=" +str(round(((pindalamax/7)*2),0))+" ja "+ str(round(((pindalamax/7)*3),0)) +"€/m²: " + str(pindala_iii_vahemik), font=("Helvetica",15), foreground="blue")
        label_pindala_iii_vahemik.place(x=10, y=520)
        label_pindala_iv_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >=" +str(round(((pindalamax/7)*3),0))+" ja "+ str(round(((pindalamax/7)*4),0)) +"€/m²: " + str(pindala_iv_vahemik), font=("Helvetica",15), foreground="grey")
        label_pindala_iv_vahemik.place(x=10, y=540)
        label_pindala_v_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >=" +str(round(((pindalamax/7)*4),0))+" ja "+ str(round(((pindalamax/7)*5),0)) +"€/m²: " + str(pindala_v_vahemik), font=("Helvetica",15), foreground="brown")
        label_pindala_v_vahemik.place(x=10, y=560)
        label_pindala_vi_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >=" +str(round(((pindalamax/7)*5),0))+" ja "+ str(round(((pindalamax/7)*6),0)) +"€/m²: " + str(pindala_vi_vahemik), font=("Helvetica",15), foreground="black")
        label_pindala_vi_vahemik.place(x=10, y=580)
        label_pindala_vii_vahemik = ttk.Label(raam, text="Kv pakkumisi pindalaga >="+ str(round(((pindalamax/12)*7),0)) +"€/m²: " + str(pindala_vii_vahemik), font=("Helvetica",15), foreground="pink")
        label_pindala_vii_vahemik.place(x=10, y=600)
    #Loon tkinteri aknasse sektordiagrammi kv-de jaotumise kohta vastavalt tubade arvule. Samuti väljastan antud info kirjalikult.
    if soovitudgraafik.get() == "tubade arv":
        sektor1 = tahvel.create_arc(225,225,10,10,fill="red", extent = (toad.count("1")/tubadega_kvsid)*359.9999)
        sektor2 = tahvel.create_arc(225,225,10,10,fill = "green", start = (toad.count("1")/tubadega_kvsid)*360, extent = (toad.count("2")/tubadega_kvsid)*359.9999)
        sektor3 = tahvel.create_arc(225,225,10,10,fill="blue", start = ((toad.count("1")+toad.count("2"))/tubadega_kvsid)*360, extent = (toad.count("3")/tubadega_kvsid)*359.9999)
        sektor4 = tahvel.create_arc(225,225,10,10,fill="grey", start = (((toad.count("1")+(toad.count("2")+(toad.count("3")))))/tubadega_kvsid)*360, extent = (toad.count("4")/tubadega_kvsid)*359.9999)
        sektor_yle4 = tahvel.create_arc(225,225,10,10,fill="brown", start = ((((toad.count("1")+toad.count("2")+toad.count("3")+toad.count("4"))))/tubadega_kvsid)*360, extent = ((tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3")+toad.count("4")))/tubadega_kvsid)*359.9999)
        label_1 = ttk.Label(raam, text="Ühetoalisi kv pakkumisi: " + str(toad.count("1")), font=("Helvetica",15), foreground="red")
        label_1.place(x=10, y=480)
        label_2 = ttk.Label(raam, text="Kahetoalisi kv pakkumisi: " + str(toad.count("2")), font=("Helvetica",15), foreground="green")
        label_2.place(x=10, y=500)
        label_3 = ttk.Label(raam, text="Kolmetoalisi kv pakkumisi: " + str(toad.count("3")), font=("Helvetica",15), foreground="blue")
        label_3.place(x=10, y=520)
        label_4 = ttk.Label(raam, text="Nelja ja enamatoalisi kv pakkumisi: " + str(tubadega_kvsid-(toad.count("1")+toad.count("2")+toad.count("3"))), font=("Helvetica",15), foreground="grey")
        label_4.place(x=10, y=540)

#Loon tkinteri akna
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

#Loon nupu
nupp = ttk.Button(raam, text="Moodusta sektordiagramm!", command=arvuta)
nupp.place(x=50, y=110, width=300)

#Ilmutan akna ekraanile
raam.mainloop()
