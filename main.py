import math
import random
import keyboard

class valami:
    def __init__(self,name,hp,dmg,luck,):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.luck = luck

    def dobos(kocka):
        szam = 0
        kocka = [random.randint(1,6) for _ in range(1,6)]
        return print(kocka)

    def __repr__(self):
        return f"<object.ember name:{self.name}>"

    def kivagy(self):
        print(f"{self.name} vagyok!")


print(f"                                            1.")
print(f"Belöknek a lenti alagútba, és rád zárják az ajtót, kizárva ezzel a nyiláson át beszúrödö termeszetes világgosságot, innentől kezdve kizárólag a falra rögzített fáklyáktól remélhetsz valamennyi fényt. Ahogy szemed hozzászokik a homályhoz, látod, hogy az alagút észak felé indul. Nagyot sóhajtasz a dolog igazságtalansága felett, majd elindulsz  abba az irányba. Lapozz a 41-re")
print(f"ahhoz, hogy tovább menj nyomd meg az ENTER-t")

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             41.")
        print(f"Az alagút, bár folyamatosan jobbra-balra kanyarog, nagyjából mégis tartja az északi irányt, végül élesen oldalra kanyarodik, és ekkor majdnem belefutsz egy fekete köpenybe öltözött alakba. Tört tart a kezébe, az arcán ülő tekintet rettegésről árulkodik! Rájössz hogy nem te vagy az egyetlen, akit most próbára tesznek és hogy mindketten ugyanazon Szobor után kutattok. A fickó rád veti magát nyilvánvaló hogy mielőbb végezni akar veled. Harcolnod kell!")
        print(f"Tolvaj Ügyesség 7     Életerő 6")
        break