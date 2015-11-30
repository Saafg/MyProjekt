# MyProjekt

MyProjekt on "repository" minu programmeerimise kursuse projekti jaoks.

Projekti eesmärk:
Programmeerimise kursuse projektina kirjutatav pythoni programm peaks suutma välja võtta valitud veebilehe html koodist mind huvitava
info ning sooritama saadud info analüüsi. Samuti kirjutama saadud info tekstifaili ning väljastama ekraanile. Täpsemalt on plaan veebilehena 
kasutada "kv.ee" otsingutulemuste lehte, kust võtta välja pakutavaid kortereid puudutava info. 

Projekti töö käigu kirjeldus:
Html koodiga tegelemiseks oli mul tarvis kahte Pythoni moodulit, mida ei leidu Pythoni standard librarys: "requests" ning "BeautifulSoup".
Uue mooduli downloadimiseks leidsin mitmeid variante: 
1)downloadida kodulehelt mooduli package, see unpack-da, minna terminalis vastavasse kausta ning kirjutada python
setup.py install; 
2)installida easy_install package ning seejärel installida mind huvitav package käsuga "easy_install mind_huvtav_package";   
3)installida mind huvitav package käsuga "pip install mind_huvitav package".

Proovisin läbi kõik meetodid, kuid paraku üksi meetod ei toonud soovitud tulemust. Mõtlesin, et probleem võib olla selles, et tegin
installi arvuti "admin" kasutaja alt, kuna tavaliselt kasutuses oleva kasutajaga ei olnud võimalik kasutada installides "sudo" optioni
ning ilma selleta läbi ei saanud. Uurimise käigus jõudsin arusaamani, et probleem on tõepoolest asukohas, kuhu moodul sattus. Avastasin ka,
et installitud mooduleid saab kasutada arvutis oleva Pythoni varasema versiooniga (2.7.4 vms) ehk moodul läks vist varasema versiooni
librarysse. Viimaks leidsin lahenduse kasutades käsku "pip3 install mind_huvitav_package", mis installis mooduli mulle sobivalt 
Python3 librarysse.

Järgnevalt lugesin veebilehe koodi sisse mooduliga requests ning asusin koodist otsima mind huvitavat infot sisaldavaid ridu. Viimase tegevuse
jaoks kasutasin avaldist: "soup.find_all("tr", attrs={"class":"object-type-apartment", "id":True})". Antud avaldis leiab html koodist kõik html
tabeli read ("tr"), mille atribuudid on class=object-type-apartment ja id=True. Atribuudid tuli esitada sõnastikuna. Probleem tekkis kui oli
mõte võtta koodist ühe protsessina välja ridu, mis omavad ühte või teist attribuudi väärtust (lihtne oli määrata, et omaks ühte JA teist
väärtust). Antud probleemi ma lahendatud ei saanudki.   

Leidnud meetodi kv.ee lehelt mind huvitava info kätte saamiseks väljastasin selle ekraanile ning kirjutasin faili kujul:
1) Pakutava korteri aadress
2) Pakutava korteri tubade arv
3) Pakutava korteri pindala ruutmeetrites
4) Pakutava korteri ruutmeetrihind
5) Pakutava korteri hind
