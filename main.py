import math
import random

class valami:
    def __init__(self,name,hp,dmg,luck,):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.luck = luck

    def dobos(kocka):
        szam = 0
        kocka = [random.randint(1,6) for _ in range(1,6)]
        print(kocka)

    def __repr__(self):
        return f"<object.ember name:{self.name}>"

    def kivagy(self):
        print(f"{self.name} vagyok!")
