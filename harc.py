class Harcos:
  def __init__(self, name, hp, damage):
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
    return f'<object.harcos: {self.nev} (HE:{self.getDamage()}, ÉE:{self.getHp()})>'