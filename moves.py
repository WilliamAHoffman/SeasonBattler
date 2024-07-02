import start

class Move:
  def __init__(self, name, userattack, userdefence, will, heal, victimdefencechange, victimattackchange, userattackchange, peirce, desc, advanceseasonu, advanceseasonv,bestseason,directchange,speed):
    self.name = name
    self.userattack = userattack
    self.userdefence = userdefence
    self.will = will
    self.heal = heal
    self.victimdefencechange = victimdefencechange
    self.victimattackchange = victimattackchange
    self.userattackchange = userattackchange
    self.peirce = peirce
    self.desc = desc
    self.advanceseasonu = advanceseasonu
    self.advanceseasonv = advanceseasonv
    self.bestseason = bestseason
    self.directchange = directchange
    self.speed = speed

test = Move("Test", 10, 0, 0, 10, 0, 0, 0, True,"test", 0, 0, start.winter, False, 2)

punch = Move(start.move1,10,0,5,0,0,0,0,False,"10 power, uses 5 will.",0,0,0,False,1)
guard = Move(start.move2,0,3,5,0,0,0,0,False,"Increased defence by 3, uses 5 will.",0,0,0,False,1)
bite = Move(start.move3,15,0,5,0,0,0,0,False,"15 power, uses 5 will.",0,0,0,False,1)
struggle = Move(start.move4,5,0,0,0,0,0,0,False,"5 power.",0,0,0,False,1)
nothing = Move(start.move5,0,0,0,0,0,0,0,False,"This does nothing.",0,0,0,False,1)
chomp = Move(start.move6,20,0,5,0,0,0,0,False,"20 power, uses 5 will.",0,0,0,False,1)
recover = Move(start.move7,0,0,5,10,0,0,0,False,"Healths health by 10, uses 5 will.",0,0,start.spring,False,1)
glaciermelt = Move(start.move8,20,0,10,0,0,0,0,False,"20 power, uses 10 will, advances season by 1.",1,0,start.winter,False,1)
autumnbounty = Move(start.move9,0,0,10,10,0,0,0,False,"Heals 10 hp, changes season to fall, uses 10 will.",3,0,start.fall,True,1)
peirceingleaves = Move(start.move10,15,0,10,0,0,0,0,True,"15 power, peirces defence, uses 10 will.",0,0,start.fall,False,1)
weaken = Move(start.move11,0,0,2,0,0,10,0,False,"Weakens the foe by 10 attack, 2 will.",0,0,0,False,1)
refresh = Move(start.move12,0,0,-5,0,0,0,0,False,"Replenishes 5 will.",0,0,0,False,1)
offensivestance = Move(start.move13,0,-5,2,0,0,0,20,False,"Lowers defence by 5 increases attack by 20, uses 2 will.",0,0,0,False,1)
overfresh = Move(start.move14,0,-5,-10,30,0,0,-5,False,"The ends justify the means.",0,0,0,False,1)
fallform = Move(start.move15,0,5,10,0,0,0,20,False,"Increases defence 5, attack 20, uses 10 will.",0,0,start.fall,False,1)
beatdown = Move(start.move16,10,0,10,0,0,0,2,False,"Attacks 3 times dealing 10 power, increasing attack by 2, uses 10 will.",0,0,0,False,3)
ancientergos = Move(start.move17,10,0,15,0,2,4,0,True,"Peirces 5 times 10 power each, lowers enemy attack 4 and defence 2, uses 15 will.",0,0,0,False,5)
venom = Move(start.move18,15,0,10,0,2,10,0,False,"15 power, weakens enemy defence by 2 and attack by 10, uses 10 will.",0,0,0,False,1)
leech = Move(start.move19,25,0,15,10,0,0,0,False,"25 power and heals 10 hp, uses 15 will.",0,0,0,False,1)
shadowdrown = Move(start.move20,10,0,10,0,0,0,5,True,"peirces 3 times 10 power, uses attack 5, uses will 10.",0,0,0,False,3)
sonicstrick = Move(start.move21,15,0,10,0,0,0,0,True,"Ignores defence 10 power, uses 10 will.",0,0,0,False,1)
fright = Move(start.move22,0,0,5,0,3,10,0,False,"Lowers enemy defence 3 and attack by 10, uses 5 will.",0,0,start.fall,False,1)
summersong = Move(start.move23,0,0,0,0,0,0,0,False,"changes the enemies season to summer",0,2,0,True,1)
refresh2 = Move(start.move24,0,0,-10,0,0,0,0,False,"Replenishes 10 will.",0,0,0,False,1)
web = Move(start.move25,5,0,5,0,1,15,0,False,"5 power, lowers enemy defence by 1 and attack by 15, uses 5 will",0,0,0,False,1)
doublefang = Move(start.move26,10,0,7,0,0,0,0,False,"10 power, attacks twice, uses 7 will",0,0,start.fall,False,2)

#lvl moves

regenerator = Move(start.lvlmove1,0,0,5,20,0,0,0,False,"Healths health by 20, uses 5 will.",0,0,start.spring,False,1)
frostform = Move(start.lvlmove2,0,5,10,0,0,0,20,False,"Increases defence 5, attack 20, uses 10 will.",0,0,start.winter,False,1)
worlddown = Move(start.lvlmove3,20,0,15,0,0,0,0,False,"20 power, reverses enemy season, uses 15 will.",0,2,0,False,1)

lvlupmove = [regenerator,frostform,worlddown,nothing,nothing,nothing,nothing,nothing,nothing,nothing,nothing,nothing,nothing,nothing,nothing]