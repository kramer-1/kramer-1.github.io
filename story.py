import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.02)
        
def die():
    delay_print(' You died. ')

def live():
    delay_print(' You survived! ')

def greeting():
    delay_print("Do you want to go on an adventure? ")
    time.sleep(.3)
    start=input("(Yes/No): ")
    start2(start)

def start2(start):
    if start.lower() == "yes":
        delay_print("You are walking down a path in a forest, and the path splits. On the left, there is a stone path. On the right, there is an old wooden path. Which way do you want to go? ")
        pathSplit=input("(Left/Right): ")
        pathSplit2(pathSplit, start)
    elif start.lower() == "no":
        sys.exit()
    else:
        delay_print("That's not an option. ")
        greeting()

def pathSplit2(pathSplit, start):
    if pathSplit.lower() == "left":
        delay_print("You find a big brick house. Do you enter the house or keep walking on the path? ")
        brickHouse=input("(Enter/Path): ")
        brickHouse2(brickHouse, pathSplit, start)
    elif pathSplit.lower() == "right":
        delay_print("The path splits off and there is a bridge. Do you cross the bridge or stay on the path? ")
        bridgeOrPath=input("(Bridge/Path): ")
        bridgeOrPath2(bridgeOrPath, pathSplit, start)
    else:
        delay_print("That's not an option. ")
        start2(start)

def brickHouse2(brickHouse, pathSplit, start):
    if brickHouse.lower() == "enter":
        delay_print("You hear a loud noise from upstairs. Do you leave or investigate? ")
        leaveOrInvestigate=input("(Leave/Investigate): ")
        leaveOrInvestigate2(leaveOrInvestigate, brickHouse, pathSplit, start)
    elif brickHouse.lower() == "path":
        delay_print("You step in quicksand and start sinking. Do you fight against it or do nothing? ")
        fightOrNothing=input("(Fight/Nothing): ")
        fightOrNothing2(fightOrNothing, brickHouse, pathSplit, start)
    else:
        delay_print("That's not an option. ")
        pathSplit2(pathSplit, start)

def leaveOrInvestigate2(leaveOrInvestigate, brickHouse, pathSplit, start):
    if leaveOrInvestigate.lower() == "leave":
        delay_print("You go outside and find a huge pot of gold!")
        live()
    elif leaveOrInvestigate.lower() == "investigate":
        delay_print("You go upstairs and somebody shoots you in the head.")
        die()
    else:
        delay_print("That's not an option. ")
        brickHouse2(brickHouse, pathSplit, start)
        
def fightOrNothing2(fightOrNothing, brickHouse, pathSplit, start):
    if fightOrNothing.lower() == "fight":
        delay_print("You keep trying but it's not working.")
        die()
    elif fightOrNothing.lower() == "nothing":
        delay_print("You sink to your death.")
        die()
    else:
        delay_print("That's not an option. ")
        brickHouse2(brickHouse, pathSplit, start)

def bridgeOrPath2(bridgeOrPath, pathSplit, start):
    if bridgeOrPath.lower() == "bridge":
        delay_print("The bridge snaps as you are crossing it and you fall into a river. Do you try to swim to the shore or drown? ")
        swimOrDrown=input("(Swim/Drown): ")
        swimOrDrown2(swimOrDrown, bridgeOrPath, pathSplit, start)
    elif bridgeOrPath.lower() == "path":
        delay_print("You find some berries on a bush. Do you eat them or not? ")
        eatOrDont=input("(Eat/Don't): ")
        eatOrDont2(eatOrDont, bridgeOrPath, pathSplit, start)
    else:
        delay_print("That's not an option. ")
        pathSplit2(pathSplit, start)

def swimOrDrown2(swimOrDrown, bridgeOrPath, pathSplit, start):
    if swimOrDrown.lower() == "swim":
        delay_print("You are able to get out of the water and you find a chest with $5,000,000 inside!")
        live()
    elif swimOrDrown.lower() == "drown":
        delay_print("You drowned.")
        die()
    else:
        delay_print("That's not an option. ")
        bridgeOrPath2(bridgeOrPath, pathSplit, start)

def eatOrDont2(eatOrDont, bridgeOrPath, pathSplit, start):
    if eatOrDont.lower() == "dont" or eatOrDont.lower() == "don't":
        delay_print("You are starving!!!")
        die()
    elif eatOrDont.lower() == "eat":
        delay_print("Its poisonous!")
        die()
    else:
        delay_print("That's not an option. ")
        bridgeOrPath2(bridgeOrPath, pathSplit, start)

greeting()

blank=input('')
