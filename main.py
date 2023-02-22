import math
import random
import keyboard

class valami:
    def __init__(self,name,hp,damage,):
        self.name = name
        self.hp = hp
        self.damage = damage

    def getHp(self):
        return self.hp
    
    def getDamage(self):
        return self.damage

    def sebzodik(self, damage):
        self.hp -= damage
    def harcol(self, harcos):
        self.sebzodik(harcos.getDamage())
        harcos.sebzodik(self.getDamage())
        if self.getHp()<1 or harcos.getHp()<1:
         return True
        return False

    def __repr__(self):
        return f'<object.harcos: {self.name} (HE:{self.getDamage()}, ÉE:{self.getHp()})>'


print(f"                                            1.")
print(f"Belöknek a lenti alagútba, és rád zárják az ajtót, kizárva ezzel a nyiláson át beszúrödö termeszetes világgosságot, innentől kezdve kizárólag a falra rögzített fáklyáktól remélhetsz valamennyi fényt. Ahogy szemed hozzászokik a homályhoz, látod, hogy az alagút észak felé indul. Nagyot sóhajtasz a dolog igazságtalansága felett, majd elindulsz  abba az irányba. Lapozz a 41-re")
print(f" ")
print(f"ahhoz, hogy tovább menj nyomd meg az ENTER-t")

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             41.")
        print(f"Az alagút, bár folyamatosan jobbra-balra kanyarog, nagyjából mégis tartja az északi irányt, végül élesen oldalra kanyarodik, és ekkor majdnem belefutsz egy fekete köpenybe öltözött alakba. Tört tart a kezébe, az arcán ülő tekintet rettegésről árulkodik! Rájössz hogy nem te vagy az egyetlen, akit most próbára tesznek és hogy mindketten ugyanazon Szobor után kutattok. A fickó rád veti magát nyilvánvaló hogy mielőbb végezni akar veled. Harcolnod kell!")
        print(f"Tolvaj Ügyesség 7     Életerő 6")
        h1 = valami(f"Kalandor", random.randint(2,12), random.randint(2,12))
        h2 = valami(f"Tolvaj",7,6)
        kor = 1

        while not h1.harcol(h2):
            print(f"{kor}. kör")
            print(h1)
            print(h2)
            kor += 1

        if h1.getHp()<1 and h2.getHp()<1:
            print("Mindketten vesztettek")
        elif h1.getHp()<1:
            print(f"Nyertes: {h2}")
        else:
            print(f"Nyertes: {h1}")
        print(f" ")
        print(f"Ha győztál és tovább akarsz menni a 85. mezőre akkor nyomd meg a SPACE-t")
        break
    
while True:    
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             85.")
        print(f"A Tolvajnál mindössze 3 aranytallért és egy háromszög alakú penészes gyümölcsöt találsz. Még soha nem láttál ehez hasonlót de gyanítod hogy ez lehet a Xentos a hosszú élet gyümölcse. Ha nem lenne ilyen borzalmas állapotba gond nélkül megkockáztatnád hogy belekóstólj így azomban úgy döntesz hogy itt hagyod és folytatod az utad észak felé. Hammarosan egy útelágazáshoz érsz, Ha továbrais északnak tartasz lapozz a 108-ra. Ha a nyugati irányba leágazó új parton mennél tovább lapozz a 147-re.")
        print(f" ")
        print(f"Ha 108-ra akarsz menni nyomd meg az ENTER-t")
        break
while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             108.")
        print(f"Északi irányba követed az átjárót. Hamarosan elérsz egy keleti elágazáshoz. Hogyha egyenesen mész tovább lapozz a 146-ra Ha letérsz jobbra lapozz a 79-re.")
        print(f" ")
        print(f"Ha a 146-ra akarsz menni nyomd meg a SPACE-t")
        break
while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             146.")
        print(f"Hamarosan egy ajtóhoz érsz ami a nyugati falból nyílik. Ahogy végig húzod a kezed rajta a kezed a kilincset keresve egy keresztet sikerül kitapintatod rajta amit nem túl mélyen véstek bele. Ha kiakarod nyitni az ajtós lapozz sz 51-re. Ha folytatnád az utad észak felé lapozz a 80-ra")
        print(f" ")
        print(f"ha az 51-re akarsz lépni nyomd meg az ENTER-t")
        break
while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             51.")
        print(f"Egy kis helyiségbe nyitsz be, mely az első ránézésre nem tartalmaz semmi mást, csak nagy halom tőrmeléket a padlón. Ahogy beljebb lépsz, kellemetlen szag csapja meg az orrodat, és egy éles, magas és - amennyire meg tudod állapítani - dühődt visítás kezd egyre erősödni. Végül egy rikoltás kiséretében két hatalmas Denevér ereszti el a plafont a szoba két sarkában, és feléd kezdenek repülni. Ahogy ösztönösen lebuksz, sekrült észrevenned a lények vicsorgó agyarait, melyek készek szétcincálni a torkodat.Ha gyorsan kihátrálsz, majd becsapod magad mögött a bejárati ajtót, lapozz a 80-ra.Hogyha megveted a lábad és megküzdesz ezekkel a szörnyű teremtményekkel, lapozz a 140-re.")
        print(f"ha a 140-re akarsz lépni nyomd meg az SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             140.")
        print(f"Felkészülsz az ütközetre miközben a két denevér zuhanórepülésbe közelít feléd. Hogyan is remélheted hogy kardoddal képes leszel felvenni velük a harcot? Meg kell próblnod a szoba egy másik részébe csalogatnod őket Hogyha pajzsod a levegőbe hajítanád talán azt hinnék hogy ez egy másik áldozat. Bármit is teszel egyesével kell megküzdened velük.")
        print(f"Elsődenevér: (Ügyesség 5 életerő 7) Második denevér: (ügyesség 6 életerő 6)")
        h1 = valami(f"Kalandor", random.randint(2,12), random.randint(2,12))
        h2 = valami(f"Denevér 1",5,7)
        kor = 1

        while not h1.harcol(h2):
            print(f"{kor}. kör")
            print(h1)
            print(h2)
            kor += 1

        if h1.getHp()<1 and h2.getHp()<1:
            print("Mindketten vesztettek")
        elif h1.getHp()<1:
            print(f"Nyertes: {h2}")
        else:
            print(f"Nyertes: {h1}")
        print(f" ")
        h3 = valami(f"Kalandor", random.randint(2,12), random.randint(2,12))
        h4 = valami(f"Denevér 2",6,6)
        kor = 1

        while not h3.harcol(h4):
            print(f"{kor}. kör")
            print(h3)
            print(h4)
            kor += 1

        if h3.getHp()<1 and h4.getHp()<1:
            print("Mindketten vesztettek")
        elif h3.getHp()<1:
            print(f"Nyertes: {h4}")
        else:
            print(f"Nyertes: {h3}")
        print(f"Ha nyersz lapozz a 160 ra. Ha akarsz az első kör után 80-ra lapozva az ajtón át elmenekülhetsz északfelé.")
        print(f"ahhoz, hogy a 160-ra lapozz nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             160.")
        print(f"Lenézel ellenfeleid elernyedt tetemeire. Holtukban még ocsmányabbak, mert a vicsorgás gonosz pofájukra fagyott. A törmelékek között első ránézésre nem sok érdekes dolgot találsz. Ha alaposabban is át akarod vizsgálni, lapozz a 37-re. Ha inkább távoznál, és észak felé folytatnád az utad, lapozz a 80-ra.")
        print(f"Ha a 37-re akarsz menni nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             37.")
        print(f"A törmelékek közt kutatva belerúgsz valami fémes dologba. Miután eltakarítottad a környékéről a szemetet, egy masszív csapóajtó körvonalai rajzolódnak ki előtted a padlóban. Nem tudod megállapítani, hogy túl rozsdás-e ahhoz, hogy fel lehessen nyitni, te mindenesetre megpróbálod. Tedd próbára szerencséd! Ha szerencsés vagy, lapozz a 199-re. Hogyha nincs szerencséd, lapozz a 130-ra.")
        print(f"Ha a 199-re akarsz lapozni akkor nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             199.")
        print(f"A csapóajtó eléggé megszorult, végül azon ban sikerül kinyitnod. Alatta egy kis üreget találsz abban peddig három tárgyat egy gyürüt, egy kis fiolányi folyadékot és egy összehajtogathatogatott köpenyt. Ha fel akarod próbálni a gyürüt, lapozz a 119-re. Hogyha fel szeretnéd venni a  köpenyt, lapozz a 12-re Amennyiben felhajtanad a folyadékot, lapozz a 71-re. Ha mindezeket a hasznos tár gyakat a követsző utazónak hagynád hátra. Bezárnád a csapóajtót és az ajton kilépve észak felé távoznál lapozz a 80-ra")
        print(f"Ha a 80-ra akarsz menni nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             80.")
        print(f"Észak felé haladsz. Megszenvedsz az úttal, hisz eléggé hepehupás. Hamarosan elérsz egy elágazáshoz. A nyugat felé tovább induló szakasz még rosszabb állapotúnak tűnik, mint az, ahol most jársz, ezért úgy döntesz továbbra is tartod az irányt. Lapozza 89-re")
        print(f"Ha a 89-re akarsz menni nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             89.")
        print(f"A járat meredeken emelkedik, te pedig gyorsan fáradni kezdesz. Figyelmed ellankad, és nem veszed észre a padlóban lévő meglazult kődarabot. Megbotlasz és elesel. közben pajzsod a fal egyik repedésébe ékelődik. Miközben próbálod kiszabadítani, elferdül. Sérült pajzsod miatt a soron követ kez csatákban 2-vel csökkentened kell majd Támadóerődet, Morogva mész tovább, mig végül egy újabb elágazáshoz nem érsz. Hogyha a nyugati ágon folytatnád az utad. lapozz a 95-ru. Ha egyenesen mész tovább, lapozz a 127-re.")
        print(f"Ha 127-re akarsz menni nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             127.")
        print(f"A járat fokozatosan kiszélesedik, és hamarosan egy sziklapárkányra érsz, ami kelet- nyugati irányban fut végig egy magas sziklafal közepén. Tiszta szerencse, hogy nem siettél nagyon, különben most egyenesen a szakadékba zuhantál volna. Hasra fekszel a párkányon és letekintesz a szélén. Messze alattad egy kis hidat látsz, ami sebesen folyó patak felett ível át. Elhátrálsz a széléről. Felnézel, de semmit nem látsz, csak a sötétséget. Nem látod, hogyan tudnál leereszkedni a völgy fenekére, a perem pedig nem messze semmivé keskenyedik mindkét oldalon. Ha nálad van a Lebegés Köpenye lapozz a 23-ra. Ha nincs, lapozz a 62-re.")
        print(f"Ha a 62-re akarsz menni nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             62.")
        print(f"Rájössz, hogy nincs rá mód, hogy lejuss innen, így visszatérsz az elágazáshoz. Lapozza 95-re.")
        print(f"Ha a 95-re akarsz menni nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                             95.")
        print(f"Nyugati irányba mész, le egy lejtős járaton míg el nem érsz egy újabb elágazást. Úgy gondolod, a déli út visszafelé vezetne, igy észak felé indulsz, Lapozz a 153-ra.")
        print(f"Ha a 153-ra akarsz menni nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            153.")
        print(f"A járat szélesedni kezd, repedések és hasadékok jelennek meg a falakon. Zörgő hang szűrődik ki valahonnan, és az egyik lyukból két különös teremtmény ugrik elő. Az egyértelműen látszik, hogy az alvilág lakói, mivel bőrük teljesen fehér, vad szemeik pedig rózsaszínüek. Fejüktől a farkukig hosszú, veszedelmes tüskék borítják hátukat,melyek járás közben jobbra-balra inganak. A lények hátat fordítanak neked, és már kezdesz megörülni, hogy megijedtek tőled és elmenekülnek. Mekkorát tévedtél! Ezek mérges Sündisznók, és épp arra készülnek. hogy halálos tüskéket beléd Köpjék. Egymás után küzdj meg velük.")
        print(f"Első sündisznó: Ügyesség 7 ÉLETRŐ 5")
        print(f"Második sündisznó: ÜGYESSEG 8 ÉLETERŐ 5")
        h1 = valami(f"Kalandor", random.randint(2,12), random.randint(2,12))
        h2 = valami(f"Sündisznó 1",7,5)
        kor = 1

        while not h1.harcol(h2):
            print(f"{kor}. kör")
            print(h1)
            print(h2)
            kor += 1

        if h1.getHp()<1 and h2.getHp()<1:
            print("Mindketten vesztettek")
        elif h1.getHp()<1:
            print(f"Nyertes: {h2}")
        else:
            print(f"Nyertes: {h1}")
        print(f" ")
        h3 = valami(f"Kalandor", random.randint(2,12), random.randint(2,12))
        h4 = valami(f"Sündisznó 2",8,5)
        kor = 1

        while not h3.harcol(h4):
            print(f"{kor}. kör")
            print(h3)
            print(h4)
            kor += 1

        if h3.getHp()<1 and h4.getHp()<1:
            print("Mindketten vesztettek")
        elif h3.getHp()<1:
            print(f"Nyertes: {h4}")
        else:
            print(f"Nyertes: {h3}")
        print(f"Mivel a tüskék nagyon mérgezőek, valahányszor beléd áll valamelyik, a szokásos 2 helyett 3 ÉLETERŐ pontot kell levonnod magadtól. Lapozz a 42-re.")
        print(f"Ha a 42-re akarsz menni akkor nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            42.")
        print(f"A járat tovább szélesedik, végül egy hatalmas barlangüregben találod magad. Mindkét oldaladnál sztalagmitok és sztalaktitok meredeznek. Néhányuk hatalmas kőoszloppá nőtt össze az idők folyamán, melyek mögött kimondhatatlan borzalmak lapulhatnak. Érzed, hogy a barlangban folyamatosan mozog a levegő, és rájössz, hogy ennek oka egy gyors folyású, igen veszedelmesnek tűnő folyó. Feltekintve szemeid követik a cseppkőoszlopok vonalait, egészen addig, míg el nem tűnnek a plafont elrejtő végtelen sötétségben. Valahol a folyó mentén egy kis, nem túl bizalomgerjesztő híd körvonalát sikerül kivenni. Lapozz a 27-re.")
        print(f"ha a 27-re akarsz menni nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            27.")
        print(f"Egy hatalmas völgy lábánál állsz, melyet egy gyors folyású folyó vájt ki. Próbálsz valami megoldást találni az átkelésre, de csak egy kicsi, eléggé rozoga és korhadt hidat látsz. Ahogy megközelíted, látod. amint két óriási termesz eszi a fát. Hófehér testükön igen nyugtalanítóan hat két vérvörös szemük. A lények bármelyike bármikor beléd marhatna. Ha sietsz talán még sikerül átkelned rajta azelőtt, hogy végleg összeroskadna. A másik lehetőséged, hogy megpróbálsz átúszni a sebes folyón. Ha az első megoldást választod, lapozz a 40-re. Ha úgy gondolod, elég jó úszó vagy. ezzel próbálkoznál, lapozz a 2-re.")
        print(f"ha a 40-re akarsz menni nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            40.")
        print(f"Miközben a termeszektől nyüzsgő építményen haladsz, az baljósan recseg-ropog a talpad alatt. Minden egyes lépéssel újabb darabjai esnek bele a vízbe. Végül már csak egyetlen kötél marad épen, ami az utolsó deszkadarabot tartja. Tedd próbára SZERENCSÉD! Ha szerencsés vagy, lapozz a 60-ra. Ha nem, lapozz a 75-re.")
        print(f"ha a 60-ra akarsz menni nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            60.")
        print(f"A híd épp elég ideig marad épen ahhoz. hogy átérj a túloldalra. Ahogy lelépsz róla, Összeomlik. Lapozz a 76-ra")
        print(f"Ha tovább akarsz menni a 76-ra nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            76.")
        print(f"Homokos parton találod magad, melynek félhold alakja van. Az előtted lévő sziklafal egy kis alkóvot alkot, és három ajtót foglal magában. Ezek közül választhatsz majd, mikor eljön a távozás ideje, előtte azonban még el kell döntened, át akarod-e kutatni a folyópartot ékkövek vagy aranyérmék után. Hogyha az északi ajtón át távoznál, lapozz a 87-re. Ha a nyugatin lépnél be, lapozz a 6-ra. Ha a keletivel próbálnál szerencsét, lapozz a 111-re. Ha előbb átkutatnád a partot, lapozz az 53-ra.")
        print(f"Ha tovább akarsz menni az 53-ra akkor nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            53.")
        print(f"A part teljesen kihaltnak tűnik, te pedig eléggé óvatlanul járkálsz, így a homokban bujkáló apró, bíbor rák minden gond nélkül csíp bele a lábadba. Vesztesz 2 ÉLETERŐ pontot. A három ajtó bármelyikén át távozhatsz. Ha az északi ajtón át távoznál, lapozz a 87-re. Ha a nyugatin lépnél be, lapozza 6-ra. Ha a keletivel próbálnál szerencsét, lapozz a 111-re")
        print(f"Ha tovább akarsz menni a 6-ra akkor nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            6.")
        print(f"Az ajtó egy nyugat felé haladó alagútba nyílik. Követed, amíg egy elágazáshoz nem érsz. Ha észak felé akarsz fordulni, lapozz a 172-re. Ha nem akarsz letérni ebből a járatból, lapozz a 168-ra.")
        print(f"Ha tovább akarsz menni a 172-re akkor nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            172.")
        print(f"A folyosó gyorsan szélesedik, végül egy kisebb szoba méreteit őlti magára. Nam messze tőled ismét összeszűkül, és újra egyszerű járatként folytatja életét. A padló közepén egy sekély aknát látsz, Ha gyorsan átgázolsz rajta, hogy a túloldalon folytathasd az utad, lapozz a 163-ra. Ha bele akarsz ugrani, lapozz a 185-re. Ha Visszatérnél az élőző alágazáshoz, és ott nyugati irányba mennél tovább, lapozza 168-ra.")
        print(f"ha tovább akarsz menni a 163-ra akkor nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            163.")
        print(f" Követed az alagutat, mely szinte azonnal egy újabb szobába torkollik. Ennek a padlója jóval lentebb áll, mint a bejárat, ahol most állsz, padlóját és kör alakú falát pedig elég magasan kőlapok borítják. Ezekre különös, egymásba fonódó mintákat festettek, melyek mintha valamilyen mágikus vagy misztikus jelentőséggel rendelkeznének. A helyiség színültig van telve kristálytiszta vízzel, és mivel eléggé mocskos vagy, meg meleged is van, nem tudsz ellenállni a kísértésnek. Levetkőzöl, és miután a biztonság kedvéért a fa ajtófélfába állítod a kardodat, elmerülsz a vízben. Miután percekig boldogan pancsolsz idelenn, és teljesen felfrissülsz, megfordulsz, hogy kimássz. Ekkor veszed észre a víz alatt lévő másik kijáratot. Lemerülsz, hogy alaposabban is szemügyre vedd. A kilincset nem tudod lenyomni, ami azért szerencse, mert ha leeresztenéd a vizet, akkor elég bajos lenne kijutnod a medencéből. Nem találsz itt semmi más érdekeset, igy felöltözöl és távozol. Visszatérsz a vermes ajtóhoz. Ha most le akarsz itt ugrani, lapozz a 185-re. Ha inkább visszatérnél a korábban látott elágazáshoz és nyugat felé folytatnád az utad, lapozz a 168-ra.")
        print(f"Ha tovább akarsz menni a 185-re akkor nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            185.")
        print(f"Leugrasz a verembe, miután meggyőződtél róla, hogy ki fogsz tudni belőle mászni, ha ez szükségesnek bizonyulna. Mikor Körbenézel agy alacsony bejáratra bukkansz az egyik kinyuló szikladarad alatt. Szinte négykézlábra kell leereszkedned, hogy be tudi kukkantani rajta. Ha alaposabban is szét akarsz odaben nézni, úgy lapozz a 178-ra Ha inkább visszatérnél a szobába, lapozz 172-re válasz valami mást.")
        print(f"Ha tovább akarsz menni a 178-ra akkor nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            178.")
        print(f"Az alagút egyra alacsonyabb és szűkebbé válik, így nehéz nem észrevenni az itt heverő kis, kék folyadikan tartalmazó üvegcsét vege Lapozz  34-re.")
        print(f"Ha tovább akarsz menni a 34-re akkor nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            34.")
        print(f"A fiola erős mentaillatot áraszt magából. Ha meg akarod inni, lapozz a 102-re. Ha inkább hagyod, ahol van. lapozz a 169-re.")
        print(f"Ha tovább akarsz menni a 102-re akkor nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            102.")
        print(f"Miután felhajtod az üvegecsében lévő italt, megdöbbenve tapasztalod, mennyivel jobban érzed most magad. Az üvegben a Szerencse Italának egy adagja volt. Növeld meg 1-el Kezdeti szerencsédet, majd állítsd vissza jelenlegi pontjaidat erre az új értékre. Folytatod a kúszást észak felé. Lapozz a 169-re")
        print(f"Ha tovább akarsz menni a 169-re nyomd meg az ENTER-t")
        break

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                            169.")
        print(f"A folyosó végén egy kicsíny ajtót  találsz Ahogy figyelsz, különös, csobogó hangot hallasz átszűrődni rajta. Érintésedre különösen  hűvösnek tűnik az anyaga. Ha ki akarod nyitni, lapozz a 164-re. Ha inkább hagyod, ahol van, lapozz vissza a 172-re és válassz valami mást")
        print(f"Ha tovább akarsz menni a 164-re nyomd meg a SPACE-t")
        break

while True:
    if keyboard.is_pressed("space"):
        print(f" ")
        print(f"                                            164.")
        print(f"Ahogy lenyomod a kilincset, az ajtó kicsapódik, mintha valami hatalmas súly nyomná ki a túloldalon. Azonnal rájössz, hogy nagy hibát vétettél, mikor vizsugarak kezdenek el kispriccelni az apró réseken. Kétségbeesetten próbálod újra bezárni a kitörni készülő víztömeget ám hamar rájössz, hogy erre semmi esélyed, igy más választásod nem lévén menekülni próbálsz. Az ajtó kicsapódik, a szűk járatban pedig esélyed sincs rá, hogy túléld a dolgot. A víz teljes tömege rád zúdul, te pedig azon nyomban megfulladsz. Kalandod itt véget ér.")
        break