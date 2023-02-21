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
        h1 = valami(f"Martin", random.randint(1,6), random.randint(1,6))
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
        print(f"")
        break
