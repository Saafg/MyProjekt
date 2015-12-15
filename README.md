# MyProjekt

MyProjekt on "repository" minu programmeerimise kursuse projekti jaoks.

Projekti eesmärk:
Programmeerimise kursuse projektina kirjutatav pythoni programm peaks suutma välja võtta valitud veebilehe html koodist mind huvitava
info, sooritama saadud info analüüsi ning väljastama need ekraanile. Täpsemalt on plaan veebilehena 
kasutada "kv.ee" otsingutulemuste lehte, kust võtta välja pakutavaid kortereid puudutava info. 

Projekti töö käigu kirjeldus:
Html koodiga tegelemiseks oli mul tarvis kahte Pythoni moodulit, mida ei leidu Pythoni standard librarys: "requests" ning "BeautifulSoup4".
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
1) Pakutava kinnisvara aadress
2) Pakutava kinnisvara tubade arv
3) Pakutava kinnisvara pindala ruutmeetrites
4) Pakutava kinnisvara ruutmeetrihind
5) Pakutava kinnisvara hind

Järgnes kõikide korterite näitajate põhjal listide moodustamine ning kasutades saadud liste arvutasin arvulistele näitajatele keskmised ning väljastasin need ekraanile. 

Järgnevalt mõtlesin igale arvulisele näitajale (tubade arv, pindala, ruutmeetrihind, hind) välja mingid vahemikud ning lugesin kokku palju kortereid jääb loodud vahemikesse. Tulemused
väljastasin ekraanile.

Kasutades tkinterit lõin akna, mis avaneb programmi käivitamisel ning kuhu saab sisestada ühe korteritega seotud arvulise näitaja, vastusena tekib sektordiagramm mis kajastab korterite
jaotumist selle näitaja jaoks mõeldud vahemikesse.

Kirjutasin programmile juurde koodi, mis võimaldab "input"-i kasutades sisestada otsingukriteeriumeid nagu nt. otsitava kinnisvara  minimaalne ja maksimaalne tubade arv, minimaalne ja
maksimaalne hind ning tehingu tüüp - kas müük, üür või mõlemad. Kuna kinnisvara müügi ja ostu puhul on kõikumised hinnas ning ruutmeetrihinnas suured, siis tegin nende näitajate puhul
sektordiagrammi loomisel kasutatavad vahemikud sõltuvaks otsingutulemustes kajastuvate pakkumiste maksimaalsest hinnast ning ruutmeetrihinnast.

Kirjutasin programmile juurde koodi, mis võimaldab "input"-i kasutades sisestada otsitava kinnisvara paiknemise maakonda ning täpsustada valda või linna. Maakondadega läks lihtsalt, kuna
maakonnad ja nele vastavad "id"-d, mida url-i sisestada olid kv.ee lähtekoodis olemas. Valdadega oli keerulisem, kuna nendega seotud infot lähtekoodis polnud. Kui aga inspekteerida
valdade loetelu listi, siis sinna ilmus valdade info, kui maakonna listist valida ära maakond. Mõtlesin, et valdadega seotud info võiks saada kätte POST request
meetodiga, saates serverisse andmed soovitud maakonna kohta. Edu antud meetodi õppimine mulle ei toonud ning kuna valdadega seotud infot lähtekoodi ei teki, siis mõtlesin, et võibolla
antud meetod ei saagi mulle edu tuua ning hakkasin otsima teisi lahendusi. Sai selgeks, et süsteemi nimi on AJAX (Asynchronous JavaScript and XML) - javascript teeb päringuid lehte uuesti
laadimata. Network tab'i jälgides sai selgeks, kuhu url-i valdadega seotud päring läheb. Antud url-l oligi sõnastik, milles oli valdadega seonduv info. Kahjuks ei olnud see sõnastik 
päris selline, et seda oleks saanud kohe Pythoniga kasutada, vaid seda tuli enne veidi korrastada. Sellest tulenevalt ei saanud programmi sisse kirjutada tsüklit, mis kõik need url-id
läbi käiks ning koguks kokku valdadega seonduva info, vaid kogusin valdadega seonduva info eraldi protseduurina ning copy-sin saadud listid oma programmi.  

Korrastasin koodi. Kirjutasin koodijuppidele juurde kommentaarid. Samuti kõrvaldasin trükivigu ning ette tulevaid erroreid. Näiteks ei teinud programm varem tulpdiagrammi, kui otsingule
tuli vaid üks vaste. Samuti tuli error, kui otsingule ei tulnud ühtegi vastet - selleks puhuks ma tegin nüüd "raise Exception"-i koos asjakohase vea selgitusega. 

Projekt on valmis!
