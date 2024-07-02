import start
class Food:
  def __init__(self, name, attackup, defenceup, healthup, willup, bestseason, desc):
    self.name = name
    self.attackup = attackup
    self.defenceup = defenceup
    self.healthup = healthup
    self.willup = willup
    self.bestseason = bestseason
    self.desc = desc

potato = Food(start.food1, 0, 0, 10, 0, start.fall,"Just a potato...")
ice = Food(start.food2, 0, 3, 0, 0, start.winter,"Increases defence by 3!")
crumbl = Food(start.food3, 10, 0, 5, 0, start.fall, "Heals 5 hp and increases attack by 10.") 