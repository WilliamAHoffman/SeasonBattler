import start
import enemies
import playerinfo
import battle
import random
import useables
import moves

recovers = 0

def enemymoveselect(enemy,player):
  choice = 10
  while choice not in range(1,6):
    start.clear()
    z = len(enemy.moves)-1
    print("Learn a move:")
    print("")
    while z >= 0:
      print("["+str(z+1)+"]",enemy.moves[z].name+":",enemy.moves[z].desc)
      print("")
      z = z - 1
    try:
      choice = int(input(""))
    except:
      start.clear()
      print(start.red+"Unclear command!"+start.white)
      print("--------------")
      input(">")
      start.clear()
  player.storedmoves.append(enemy.moves[choice-1])

def pickmoves(player):
  b = 0
  z = len(player.moves)-1
  print("Equiped moves:")
  print("")
  while z >= 0:
    print("["+str(z+1)+"]",player.moves[z].name+":",player.moves[z].desc)
    print("")
    z = z - 1
  print("")
  print("Stored moves:")
  print("")
  print("[0] Back")
  print("")
  while b < len(player.storedmoves):
    print("["+str(b+1)+"]",player.storedmoves[b].name+":",player.storedmoves[b].desc)
    print("")
    b = b + 1
  try:
    y = int(input("Equip move: "))-1
    if y == -1:
      return
    print(player.storedmoves[y].name)
  except:
    start.clear()
    print(start.red+"Unclear command!"+start.white)
    print("--------------")
    input(">")
    return
  if y in range(0,len(player.storedmoves)):
    try:
      q = int(input("Replace with: "))-1
      if q in range(0,5):
        print(player.moves[q].name)
        tempmove = player.storedmoves[y]
        player.storedmoves[y] = player.moves[q]
        player.moves[q] = tempmove
        print("Done!")
        input(">")
        return
    except:
      start.clear()
      print(start.red+"Unclear command!"+start.white)
      print("--------------")
      input(">")
      return
  start.clear()
  print(start.red+"Unclear command!"+start.white)
  print("--------------")
  input(">")
  return
    
def explore(location,player):
  print("You begin to look around the", location+".")
  input(">")
  chance = random.randint(1,100)
  if location == start.local1:
    if chance >= 75:
      battle.battle(playerinfo.ella,enemies.enemygraveyard1,True,[],0) 
    elif chance >= 50:
      battle.battle(playerinfo.ella,enemies.enemygraveyard2,True,[],useables.crumbl)
    elif chance >= 25:
      battle.battle(playerinfo.ella,enemies.enemygraveyard3,True,[],0)
    elif chance >= 0:
      battle.battle(playerinfo.ella,enemies.enemygraveyard4,True,[],0)
  return
    
def menu(player,location):
  start.clear()
  playerinfo.levelup(player)
  while 1 == 1:
    global recovers
    print("What will you do next",player.name+"?")
    start.write("[1] Change Moves",speed=0.02)
    start.write("[2] Check Bag",speed=0.02)
    start.write("[3] Continue",speed=0.02)
    start.write("[4] Look Around",speed=0.02)
    start.write("[5] Rest ("+str(recovers)+")",speed=0.02)
    print("Location: "+location)
    if player.lvl < 30:
      start.write(str(player.xp)+" / "+str(playerinfo.levelup(player))+" xp",speed=0.02)
    else:
      start.write(str(player.xp)+" xp",speed=0.02)
    start.write("Lvl: "+str(player.lvl),speed=0.02)
    start.write("Gold: "+str(player.gold),speed=0.02)
    print("Defence:",str(player.defence))
    print("Attack:",str(player.attack))
    print("Health:")
    battle.bar(player.maxhealth,player.health)
    print("Will:")
    battle.bar(player.maxwill,player.will)

    y = input(">")
    if y == "1":
      start.clear()
      pickmoves(player)
      start.clear()
    elif y == "2":
      start.clear()
      food(player)
      start.clear()
    elif y == "3":
      start.clear()
      return
    elif y == "4":
      start.clear()
      explore(location,player)
      start.clear()
    elif y == "5":
      start.clear()
      print("You sit and rest for a short while.")
      playerinfo.ella.health = playerinfo.ella.maxhealth
      playerinfo.ella.will = playerinfo.ella.maxwill
      recovers = recovers + 1
      input(">")
      print("Health and will restored!")
      input(">")
      start.clear()
    else:
      start.clear()
      print(start.red+"Unclear command!"+start.white)
      print("--------------")

def food(player):
  b = 0
  print("You check your bag.")
  print("You have:")
  while b < len(player.food):
    print(player.food[b].name+":",player.food[b].desc)
    b = b + 1
  input(">")
  return

#----------------------------------------------------------------------

def cutscene1():
  start.write("You wake up in a small empty well.",speed=0.02)
  start.write("As you get up you hear the crunching of decaying Autumn leaves spread about the hard well floor.",speed=0.02)
  input(">")
  start.write(start.unknown+": Why do you keep coming back here.",speed=0.02)
  input(">")
  start.write(start.ella+": I'm not entirely sure.",speed=0.02)
  start.write(start.ella+": Who are you?",speed=0.02)
  input(">")
  start.write(start.unknown+": I should be asking you the same thing.",speed=0.02)
  start.write(start.markus+": My name is Markus. I'm just the grave keeper here.",speed=0.02)
  input(">")
  start.write(start.ella+": My name is Ella.",speed=0.02)
  input(">")
  start.write(start.markus+": Nice to meet you. You might wanna get out of that well.",speed=0.02)
  input(">")
  start.write(start.ella+": I'm well aware.",speed=0.02)
  input(">")
  start.write("As you get up you hear an "+start.ename1+" from behind!",speed=0.02)
  input(">")
  win = battle.battle(playerinfo.ella,enemies.enemy1,False,[],useables.potato)
  return win

def cutscene2(win):
  start.write("You quickly get out of the well.",speed=0.02)
  if win == True:
    start.write(start.markus+": Holy crap are you ok!",speed=0.02)
    input(">")
    start.write(start.ella+": I'm fine just a few bites.",speed=0.02)
    start.write(start.ella+": This isn't poisonous right?.",speed=0.02)
    input(">")
    start.write(start.markus+": You should be fine.",speed=0.02)
    start.write(start.markus+": That was some impressive fighting.",speed=0.02)
    start.write(start.markus+": I'll heal you right now.",speed=0.02)
  else:
    start.write(start.markus+": That was pretty embarrasing...",speed=0.02)
    start.write(start.markus+": you'll be fine though.",speed=0.02)
  input(">")
  start.write(start.markus+" used "+start.move14+"!",speed=0.02)
  start.write("Health restored!",speed=0.02)
  start.write("Will restored!",speed=0.02)
  input(">")
  playerinfo.ella.health = playerinfo.ella.maxhealth
  playerinfo.ella.will = playerinfo.ella.maxwill
  start.write(start.ella+": I think I just learned something from that snake.",speed=0.02)
  start.write(start.ella+" learned "+start.move3+"!",speed=0.02)
  input(">")
  playerinfo.ella.storedmoves.append(moves.bite)
  start.write(start.markus+": You've changed somehow...",speed=0.02)
  start.write(start.markus+": Im gonna head to the my abode please come speak with me.",speed=0.02)
  input(">")
  start.write(start.markus+": Take this before I go.",speed=0.02)
  start.write(start.markus+" gives you a small blue gem. you can feel something within.",speed=0.02)
  start.write(start.ella+" learned "+start.move24+"!",speed=0.02)
  input(">")
  playerinfo.ella.storedmoves.append(moves.refresh2)

def cutscene3(location):
  start.write("You start heading for the grave tenders home. It sits on the outskirts of the graveyard.",speed=0.02)
  start.write("You try to remember why you were in the well in the first place.",speed=0.02)
  start.write("Suddenly you get attack by a "+start.ename3+"!",speed=0.02)
  input(">")
  win = False
  while win == False:
    win = battle.battle(playerinfo.ella,enemies.enemy3,False,[],0)
    menu(playerinfo.ella,location)
  start.write("You where able to survive the attack.",speed=0.02)
  input(">")
  start.write("You continue for a short while before reaching the cabin that "+start.markus+" was talking about. You open the door but its pitch black inside.",speed=0.02)

def cutscene4():
  print("heheheha")