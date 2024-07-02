
import start
import random
import playerinfo

def startbattle(player,enemy):
  global enemyattack,enemydefence,enemyhealth,enemyseason,playerattack,playerdefence,playerseason,word
  enemyattack = enemy.attack
  enemydefence = enemy.defence
  enemyhealth = enemy.health
  enemyseason = enemy.season
 
  playerattack = player.attack
  playerdefence = player.defence
  playerseason = player.season

  word = -1
  return

def seasonchange(season,attacker,moves,y):
  try:
    if season == start.winter:
      s = 4
    elif season == start.fall:
      s = 3
    elif season == start.spring:
      s = 1
    elif season == start.summer:
      s = 2
    if attacker == 1:
      s = s + moves[y].advanceseasonu
      if moves[y].directchange == True:
        s = moves[y].advanceseasonu
    else:
      s = s + moves[y].advanceseasonv
      if moves[y].directchange == True:
        s = moves[y].advanceseasonv
    if s <= 0:
      s = s + 4
    if s >= 5:
      s = s - 4
    if s == 1:
      season = start.spring
    elif s == 2:
      season = start.summer
    elif s == 3:
      season = start.fall
    elif s == 4:
      season = start.winter
    print("Season change!")
  except:
    season = start.unbound
  return season

def words(enemy):
  lenword = len(enemy.words)
  if word < lenword:
    if enemy.words[word] != 0:
      start.write(str(enemy.words[word]),speed=0.01)
      input(">")
      start.clear()
  return

def result(name,name2,y,moves,defhealth,defender,curdefence,attseason,defseason,attackvalue,health,maxhealth,defattack):
  start.write(name+" used "+moves[y].name+"!",speed=0)
  x = 1
  if moves[y].bestseason == attseason:
    print("It's the best season!")
    x = 1.2
  speed = moves[y].speed
  while speed > 0:
    if moves[y].userattack != 0:  
      #print(defhealth,defender,curdefence,attseason,defseason,attackvalue,health,maxhealth,defattack)
      damage = int(moves[y].userattack*(1+attackvalue/100))
      #print("initial:",damage)#temp
      effect = season(attseason,defseason)
      #print("season effect:",effect)#temp
      damage = int(damage * ((100+effect)/100))
      #print("attack bonus:",damage)#temp
      damage = int(variance(damage))
      #print("variance:",damage)#temp
      if moves[y].peirce == False:
        damage = damage - defender
      #print("defence:",damage)#temp
      if damage <= 0:
        damage = 1
      defhealth = defhealth - int(damage*x)
      start.write("It dealt "+str(int(damage*x))+" damage!",speed=0.01)
    if moves[y].userdefence != 0:
      curdefence = curdefence + int(moves[y].userdefence*x)
      if curdefence > 0:
        print(name,"defence increased by",int(moves[y].userdefence*x))
      else:
        print(name,"defence decreased by",int(moves[y].userdefence*x*-1))
    if moves[y].heal != 0:
      health = health + int(moves[y].heal*x)
      if moves[y].heal > 0:
        print(name,"healed",int(moves[y].heal*x),"Hp")
      else:
        print(name,"sacrificed",int(moves[y].heal*x*-1),"Hp")
      if health > maxhealth:
        health = maxhealth
    if moves[y].victimdefencechange != 0:
      defender = defender - int(moves[y].victimdefencechange*x)
      if moves[y].victimdefencechange < 0:
        print(name2,"defence increased by",int(moves[y].victimdefencechange*x*-1)) 
      else:
        print(name2,"defence decreased by",int(moves[y].victimdefencechange*x)) 
    if moves[y].victimattackchange != 0:
      defattack = defattack - int(moves[y].victimattackchange*x)
      if moves[y].victimattackchange > 0:
        print(name2,"attack decreased by",int(moves[y].victimattackchange*x))
      else:
        print(name2,"attack increased by",int(moves[y].victimattackchange*x*-1))
      if defattack <= -75:
        print("It can't go any lower!")
        defattack = -75
    if moves[y].userattackchange != 0:
      attackvalue = attackvalue + int(moves[y].userattackchange*x)
      if moves[y].userattackchange > 0:
        print(name,"attack increased by",int(moves[y].userattackchange*x))
      else:
        print(name,"attack decreased by",int(moves[y].userattackchange*x*-1))
    if moves[y].advanceseasonu != 0:
      attseason = seasonchange(attseason,1,moves,y)
    if moves[y].advanceseasonv != 0:
      defseason = seasonchange(defseason,0,moves,y)
    speed = speed - 1
  input(">")
  start.clear()
  return defhealth,defender,curdefence,attseason,defseason,health,defattack,attackvalue

def variance(damage):
  x = random.randint(-2,2)
  damage = damage + x
  y = random.randint(1,10)
  if y == 10:
    print("It was a perfect attack!")
    damage = damage * 1.5
  if y == 1:
    print("It was a dull attack!")
    damage = damage/2
  return damage

def season(pseason,eseason):
  try:
    if pseason == start.winter:
      ps = 4
    elif pseason == start.fall:
      ps = 3
    elif pseason == start.spring:
      ps = 1
    elif pseason == start.summer:
      ps = 2
    if eseason == start.winter:
      es = 4
    elif eseason == start.fall:
      es = 3
    elif eseason == start.spring:
      es = 1
    elif eseason == start.summer:
      es = 2
    uneffect = ps - 1
    effect = ps + 1
    if uneffect == 0:
      uneffect = 4
    if effect == 5:
      effect = 1
    if effect == es:
      print("It wasn't very effective...")
      p = -25
    elif uneffect == es:
      print("It was very effective!")
      p = 25
    else:
      print("It was neutral.")
      p = 0
  except:
    p = 0
  return p
    
def bar(maxhealth,health):
  dashconvert = int(maxhealth/20)
  currentdashes = int(health/dashconvert)
  remaininghealth = 20 - currentdashes
  healthDisplay = '-' * currentdashes
  remainingDisplay = ' ' * remaininghealth
  print("|" + healthDisplay + remainingDisplay + "|",health,"/",maxhealth)

def run(runable):
  if runable == False:
    start.write("You Can't run from this foe!",speed = 0.01)
    run = 0
  else:
    z = random.randint(0,1)
    if z == 0:
      start.write("You failed to escape!",speed = 0.01)
      run = 0
    else:
      start.write("You escaped!",speed = 0.01)
      run = 1
  return run

def fight(player,enemy,attacker,battleorder):
  global enemyhealth,enemydefence,playerdefence,playerseason,enemyseason,playerattack,enemyattack,enemyhealth,index
  if attacker == 0:
    while 1 == 1:
      start.write("Your health:",speed=0.01)
      bar(player.maxhealth,player.health)
      start.write("Your willpower:",speed=0.01)
      bar(player.maxwill,player.will)
      print("Enemy health:")
      bar(enemy.health,enemyhealth)
      print("")
      start.write("[1] "+str(player.moves[0].name)+": "+player.moves[0].desc,speed=0.001)
      start.write("[2] "+str(player.moves[1].name)+": "+player.moves[1].desc,speed=0.001)
      start.write("[3] "+str(player.moves[2].name)+": "+player.moves[2].desc,speed=0.001)
      start.write("[4] "+str(player.moves[3].name)+": "+player.moves[3].desc,speed=0.001)
      start.write("[5] "+str(player.moves[4].name)+": "+player.moves[4].desc,speed=0.001)
      start.write("[6] Go back.",speed=0.001)
      try:
        y = int(input(">"))-1
      except:
        start.clear()
        print(start.red+"Unclear command!"+start.white)
        print("--------------")
        y = 99
      if y == 5:
        start.clear()
        return 0
      if y in range(0,5):
        if player.will >= player.moves[y].will:
          start.clear()
          enemyhealth,enemydefence,playerdefence,playerseason,enemyseason,player.health,enemyattack,playerattack = result(player.name,enemy.name,y,player.moves,enemyhealth,enemydefence,playerdefence,playerseason,enemyseason,playerattack,player.health,player.maxhealth,enemyattack)
          player.will = player.will - player.moves[y].will
          if player.will > player.maxwill:
            player.will = player.maxwill
          return 1
        else:
          start.clear()
          start.write(start.red+"Not enough willpower!"+start.white,speed=0.01)
          print("--------------")
          y = 0
      else:
        start.clear()
        start.write(start.red+"Unclear command!"+start.white,speed=0.01)
        print("--------------")
  else:
    try:
      y = battleorder[index]
      index = index + 1
    except:
      y = random.randint(0,4)
      if enemy.moves[y].heal > 0:
        while enemy.health-(enemy.health-enemyhealth) >= enemy.health-enemy.moves[y].heal: #wether or not the enemy should use a heal move
          y = random.randint(0,4)
          print(y)
    player.health,playerdefence,enemydefence,enemyseason,playerseason,enemyhealth,playerattack,enemyattack = result(enemy.name,player.name,y,enemy.moves,player.health,playerdefence,enemydefence,enemyseason,playerseason,enemyattack,enemyhealth,enemy.health,playerattack)
    global word
    word = word + 1
    words(enemy)
    
      

def foodstats(player, food):
  global playerattack, playerdefence, playerseason
  x = 1
  print("Consumed:",food.name)
  if playerseason == food.bestseason:
    print("It was the right season!")
    x = 1.2
  player.health = player.health + int(food.healthup*x)
  player.will = player.will + int(food.willup*x)
  playerattack = playerattack + int(food.attackup*x)
  playerdefence = playerdefence + int(food.defenceup*x)
  if player.health > player.maxhealth:
    player.health = player.maxhealth
  if player.will > player.maxwill:
    player.will = player.maxwill
  input(">")

def foodpick(player):
  start.write("Your health:",speed=0.01)
  bar(player.maxhealth,player.health)
  start.write("Your willpower:",speed=0.01)
  bar(player.maxwill,player.will)
  print("What food would you like to use:")
  print("")
  foodlen = len(player.food)
  try:
    y = 0
    while y < foodlen:
      print("[",y + 1,"]",str(player.food[0+y].name),str(player.food[0+y].desc))
      y = y + 1
    print("["+str(y + 1)+"] Go back")
    z = int(input(">"))
    if z > foodlen:
      return 0
    else:
      foodstats(player,player.food[z-1])
      return 1
  except:
    start.clear()
    print(start.red+"Unclear command!"+start.white)
    print("--------------")
    input(">")
    return 0

def battle(player,enemy,runable,battleorder,food):
  global index
  index = 0
  startbattle(player,enemy)
  start.clear()
  start.write("You encountered "+enemy.name+"!",speed=0.02)
  start.write("You prepare for battle!",speed=0.02)
  print("-----------------------------")
  input(">")
  start.clear()
  while 1 == 1:
    print(player.name+" ("+playerseason+") VS "+enemy.name+" ("+enemyseason+")")
    print("Enemy health:")
    bar(enemy.health,enemyhealth)
    start.write("[1] Fight!",speed=0.01)
    start.write("[2] Food!",speed=0.01)
    start.write("[3] Do Nothing!",speed=0.01)
    start.write("[4] Run!",speed=0.01)
    start.write("[5] Give up...",speed=0.01)
    start.write("Your health:",speed=0.01)
    bar(player.maxhealth,player.health)
    start.write("Your willpower:",speed=0.01)
    bar(player.maxwill,player.will)
    print("Defence:",playerdefence)
    print("Enemy defence:",enemydefence)
    print("Attack:",playerattack)
    print("Enemy attack:",enemyattack)
    try:
      y = int(input(">"))
    except:
      start.clear()
      print(start.red+"Unclear command!"+start.white)
      print("--------------")
      y = 0      
    if y == 1:
      start.clear()
      y = fight(player,enemy,0,battleorder)
    elif y == 2:
      start.clear()
      y = foodpick(player)
      start.clear()
    elif y == 3:
      start.clear()
      start.write("You stood there looking like an idiot!",speed=0.01)
      input(">")
      start.clear()
    elif y == 4:
      win = run(runable)
      print("----------------------")
      input(">")
      start.clear()
      if win == 1:
       return False
    elif y == 5:
      start.write("You gave up...",speed=0.02)
      input(">")
      player.health = 1
      player.will = 0
      start.clear()
      return False
    else:
      start.clear()
      print(start.red+"Unclear command!"+start.white)
      print("--------------")
      y = 0
    if enemyhealth <= 0:
      start.write("You beat the "+enemy.name+"!",speed=0.02)
      start.write("You gained: ",speed=0.02)
      start.write("Gold: "+str(enemy.gold),speed=0.02)
      start.write("XP: "+str(enemy.xp),speed=0.02)
      player.gold = player.gold + enemy.gold
      player.xp = player.xp + enemy.xp
      if food != 0:
        player.food.append(food)
        print("You found:",food.name)
      playerinfo.levelup(player)
      input(">")
      start.clear()
      return True
    if y in range(1,6):
      fight(player,enemy,1,battleorder)
    if player.health <= 0:
      player.health = 1
      start.write("You lost...",speed=0.02)
      input(">")
      start.clear()
      return False