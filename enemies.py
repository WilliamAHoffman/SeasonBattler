import start
import moves
import random
import useables

class Enemy:
  def __init__(self, name, attack, defence, health, moves, xp, gold, season, desc, words):
    self.name = name
    self.attack = attack
    self.defence = defence
    self.health = health
    self.moves = moves
    self.xp = xp
    self.gold = gold
    self.season = season
    self.desc = desc
    self.words = words

#1 = spring
#2 = summer
#3 = fall
#4 = winter
#5 = unbound
    
#event enemies

enemy1words = [start.ename1+" slithers around!",start.ename1+" is covered in Autumn leaves!"]
enemy1moves = [moves.bite,moves.bite,moves.bite,moves.nothing,moves.nothing]
enemy1 = Enemy(start.ename1, 0, 0, 50,enemy1moves, random.randint(50,70), random.randint(1,10), start.fall,"A small orange snake covered in Autumn leaves!",enemy1words)

enemy2words = [0,start.ename2+" spits coins all over the floor!"]
enemy2moves = [moves.chomp,moves.bite,moves.chomp,moves.guard,moves.offensivestance]
enemy2 = Enemy(start.ename2, 10, 5, 100, enemy2moves, random.randint(80,120), random.randint(75,100), start.summer,"A fake chest!",enemy2words)

enemy3words = [start.ename3+" surrounds itself in the blood of its prey.",0,start.ename3+" spins webs everywhere."]
enemy3moves = [moves.venom,moves.leech,moves.web,moves.bite,moves.doublefang]
enemy3 = Enemy(start.ename3,5,-3,100,enemy3moves,100,10,start.fall,"A rose red tarantula.",enemy3words)

prismboywords = [start.ename4+" reflects blightly!"]
prismboymoves = [moves.bite,moves.bite,moves.bite,moves.bite,moves.bite]
prismboy = Enemy(start.ename4,50,20,250,prismboymoves,150,25,start.unbound,"A great artifact of the old days.",prismboywords)

markuswords = [start.markus+": You can't beat me.",0,start.markus+": No matter how much you try.",start.markus+": It will all end soon."]
markusmoves = [moves.autumnbounty,moves.overfresh,moves.beatdown,moves.fallform,moves.ancientergos]
markus = Enemy(start.markus,20,20,300,markusmoves,500,100,start.fall,"The grave tender.",markuswords)

#graveyard enemies

enemygraveyardwords1 = [start.ename1gy+" is covered in Autumn leaves!",0,start.ename1gy+" slithers around a grave!"]
enemygraveyardmoves1 = [moves.bite,moves.chomp,moves.offensivestance,moves.nothing,moves.venom]
enemygraveyard1 = Enemy(start.ename1gy,10,0,50,enemygraveyardmoves1,random.randint(50,70),random.randint(1,10),start.fall,"An orange snake covered in Autumn leaves!",enemygraveyardwords1)

enemygraveyardwords2 = [start.ename2gy+" is an ant made of crumbs!",0,start.ename2gy+" tries to steal your crumbs!"]
enemygraveyardmoves2 = [moves.autumnbounty,moves.bite,moves.peirceingleaves,moves.peirceingleaves,moves.weaken]
enemygraveyard2 = Enemy(start.ename2gy,0,0,60,enemygraveyardmoves2,random.randint(60,80),random.randint(10,15),start.fall,"An ant made of crumbs",enemygraveyardwords2)

enemygraveyardwords3 = []
enemygraveyardmoves3 = [moves.overfresh,moves.glaciermelt,moves.weaken,moves.leech,moves.shadowdrown]
enemygraveyard3 = Enemy(start.ename3gy,-10,-20,200,enemygraveyardmoves3,random.randint(70,80),0,start.winter,"A ghost at the end of its time.",enemygraveyardwords3)

enemygraveyardwords4 = [start.ename4gy+" plays a little tone.",0,start.ename4gy+" starts jamming out!"]
enemygraveyardmoves4 = [moves.summersong,moves.sonicstrick,moves.fright,moves.autumnbounty,moves.sonicstrick]
enemygraveyard4 = Enemy(start.ename4gy,0,0,90,enemygraveyardmoves4,random.randint(80,99),random.randint(10,15),start.fall,"Skeleton with a knack for playing the xylophone.",enemygraveyardwords4)