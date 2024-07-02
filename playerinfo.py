import start
import moves
import useables

lvlmove = -1

def playerstats(player):
  global lvlmove
  player.attack = player.attack + 5
  player.maxhealth = player.maxhealth + 5
  player.defence = player.defence + 1
  player.maxwill = player.maxwill + 1
  print("Stats increased!")
  if player.lvl%2 == 0:
    lvlmove = lvlmove + 1
    print("New move: "+moves.lvlupmove[lvlmove].name)
    player.storedmoves.append(moves.lvlupmove[lvlmove])

def levelup(player):
  x = player.lvl + 1
  scaling = player.lvl
  required = int(((scaling**2)/2)+scaling*50)+50
  if player.lvl <= 30:
    while player.xp >= required:
      if player.lvl >= 30:
        return
      scaling = player.lvl
      required = int(((scaling**2)/2)+scaling*50)+50
      player.xp = player.xp - required
      player.lvl = player.lvl + 1
      print("You leveled up!")
      print("lvl:",x)
      scaling = scaling + 1
      x = x + 1
      playerstats(player)

  return required

class Play:
  def __init__(self, name, attack, defence, health, maxhealth, maxwill, will, xp, lvl, gold, moves, season, food, desc, storedmoves):
    self.name = name
    self.attack = attack
    self.defence = defence
    self.health = health
    self.maxhealth = maxhealth
    self.maxwill = maxwill
    self.will = will
    self.xp = xp
    self.lvl = lvl
    self.gold = gold
    self.moves = moves
    self.season = season
    self.food = food
    self.desc = desc
    self.storedmoves = storedmoves
    
#1 = spring
#2 = summer
#3 = fall
#4 = winter

ellastoredmoves = []
ellamoves = [moves.punch,moves.guard,moves.recover,moves.glaciermelt,moves.refresh]
ellafoods = []
ella = Play(start.ella,0,0,100,100,20,20,0,0,0,ellamoves,start.winter,ellafoods,"Hey it is I!",ellastoredmoves)

