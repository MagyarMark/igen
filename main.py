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

while True:
    if keyboard.is_pressed("enter"):
        print(f" ")
        print(f"                                             41.")
        print(f"szöveg")
        break