import story
import battle
import playerinfo
import start 

win = False

location = start.local1

win = story.cutscene1()

story.cutscene2(win)

story.menu(playerinfo.ella,location)

story.cutscene3(location)

story.menu(playerinfo.ella,location)