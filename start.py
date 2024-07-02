import os
import sys
import time

from sty import fg

txtspd = 0.02

white = fg(255,255,255)
red = fg(255,80,80)
orange = fg(242,184,75)
yellow = fg(255,255,117)
light_green = fg(0,255,76)
green = fg(0,163,49)
light_blue = fg(82,180,255)
blue = fg(0,123,255)
dark_blue = fg(19,85,156)
purple = fg(162,0,255)
light_purple = fg(205,117,255)
gray = fg(130,130,130)
silver = fg(200,230,255)
brown = fg(150,70,0)
black = fg(255,255,255)
pink = fg(255,105,180)

reset = fg.rs

bold = "\033[1m"
italic = "\033[3m"

def write(text, speed):
  for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    
    time.sleep(speed)
    
  print("") # flush a line
  
def clear():
  os.system('clear') # clears screen

#seasons
winter = silver + "Winter" + white
spring = light_green + "Spring" + white
summer = yellow + "Summer" + white
fall = orange + "Fall" + white
unbound = "Unbound"

# names
ella = light_purple + 'Ella' + white
markus = brown + 'Markus' + white
unknown = silver + '???' + white

#enemies
ename1 = orange + "Small Autumn Snake" + white
ename2 = yellow + "Mimic" + white
ename3 = red + "Rose Tarantula" + white
ename4 = red + "P" + orange + "R" + yellow + "I" + light_green + "S" + light_blue + "M" + purple + "A" + white

#graveyard enemies
ename1gy = orange + "Autumn Snake" + white
ename2gy = yellow + "Crumbl Ant" + white
ename3gy = silver + "Fading Shadow" + white
ename4gy = silver + "Xlyobone" + white

#moves
move1 = red + "Punch" + white
move2 = green + "Gaurd" + white
move3 = red + "Bite" + white
move4 = red + "Struggle" + white
move5 = gray + "Nothing" + white
move6 = red + "Chomp" + white
move7 = light_green + "Recover" + white
move8 = silver + "Glaciermelt" + white
move9 = orange + "Autumn bounty" + white
move10 = orange + "Peirceing Leaves" + white
move11 = gray + "Weaken" + white
move12 = blue + "Refresh" + white
move13 = red + "Offense Stance" + white
move14 = blue + "Overfresh" + white
move15 = orange + "Fallform" + white
move16 = red + "Beatdown" + white
move17 = purple + "Ancient Ergos" + white
move18 = red + "Venom" + white
move19 = green + "Leech" + white
move20 = purple + "Shadow Drown" + white
move21 = red + "Sonic Strick" + white
move22 = orange + "Fright" + white
move23 = yellow + "Summer Song" + white
move24 = blue + "Refresh II" + white
move25 = gray + "Web" + white
move26 = orange + "Double Fang" + white

#food
food1 = orange + "Potato" + white
food2 = silver + "Ice" + white
food3 = orange + "Crumbl" + white

#location
local1 = orange + "Graveyard" + white

#ellalvlmoves

lvlmove1 = light_green + "Regenerator" + white
lvlmove2 = silver + "Frost Form" + white
lvlmove3 = pink + "World Upside-down" + white
