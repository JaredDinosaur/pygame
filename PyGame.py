from random import randint as rn
from time import sleep as sl

sword = 0
dur = 8
apples = 0
nextroom = "cave"
end = 0
hp = 40
maxhp = 40
orc = 0
orchp = 32
gatelk = 0
coat = 0
plank = 0
boulder = 0
book = 0
lever = 0

print("Commands:")
print("n, e, s, w, u, d: Move in a direction")
print("i: Interact with an object")
print("a: Attack (while in battle)")
print("h: Heal (while in battle)")
print("")

sl(2)

def cave():
    change = 0
    global sword
    global apples
    global nextroom

    print("")
    print("You are in a cave.")
    print("Alongside you is a chest.")
    print("Obvious directions are north.")
    
    while change==0:
        print("")
        move=input("What now? ")
    
        move=move.lower()
    
        if move in ["e", "s", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move=="n":
            nextroom = "cliff"
            change = 1

        elif move=="i":
            if sword == 0:
                sword = 1
                apples += 4

                print("")
                print("You opened the chest and found", end="\r")
                sl(0.5)
                print("You opened the chest and found.", end="\r")
                sl(0.5)
                print("You opened the chest and found..", end="\r")
                sl(0.5)
                print("You opened the chest and found...", end="\r")
                sl(0.5)
                print("You opened the chest and found a wooden sword!")
                sl(0.5)
                print("You also found", end="\r")
                sl(0.5)
                print("You also found.", end="\r")
                sl(0.5)
                print("You also found..", end="\r")
                sl(0.5)
                print("You also found...", end="\r")
                sl(0.5)
                print("You also found 4 apples!")
                sl(0.5)
                print("")

            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")
        
def cliff():
    change = 0
    global sword
    global dur
    global apples
    global hp
    global maxhp
    global orc
    global end
    global orchp
    global nextroom

    print("")
    print("You are walking alongside a cliff.")
    if orc == 0:
        sl(0.5)
        print("You hear rustling from a nearby bush", end="\r")
        sl(0.5)
        print("You hear rustling from a nearby bush.", end="\r")
        sl(0.5)
        print("You hear rustling from a nearby bush..", end="\r")
        sl(0.5)
        print("You hear rustling from a nearby bush...")
        sl(0.5)
        print("An orc leapt from the bush!")

        sl(0.5)

        while orc == 0 and end == 0:
            print("")
            move = input("What now? ")

            move = move.lower()

            if move in ["s", "e"]:
                print("")
                print("You can't run now!")
                print("")

            elif move in ["n", "w"]:
                print("")
                print("You leapt off the cliff and died. Well done.")
                print("")

                end = -1

            elif move in ["u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "a":
                if dur > 0 and sword == 1:
                    print("")
                    print("You swung your sword at the orc!")

                    luck = rn(1,8)
                    if luck == 1:
                        sl(0.5)
                        print("And missed!")
                        dmg = 0
                    elif luck == 2:
                        sl(0.5)
                        print("You landed a critical hit!")
                        dmg = rn(8,10)
                    else:
                        dmg = rn(3,5)

                    sl(0.5)

                    orchp -= dmg
                    print("Dealt", dmg, "damage to the orc!")
                    
                    sl(0.5)

                    if luck != 1:
                        dur -= 1
                    if dur == 0:
                        print("Your sword broke!")
                        dmg = rn(1,4)
                        sl(0.5)
                        orchp -= dmg
                        print("Shrapnel hit the orc, dealing", dmg, "damage!")

                    sl(0.5)

                    if orchp > 0:
                        luck = rn(1,8)
                        if luck == 1:
                            print("The orc threw a punch!")
                            sl(0.5)
                            print("And missed!")
                            dmg = 0
                        elif luck == 2:
                            print("The orc hit you with all its might!")
                            dmg = rn(9,12)
                        else:
                            print("The orc threw a punch!")
                            dmg = rn(4,6)

                        sl(0.5)

                        hp-=dmg
                        print("You recieved", dmg, "damage!")

                        sl(0.5)

                        if hp <= 0:
                            end = -1
                            print("You were slain!")

                        else:
                            print("")
                            print("Your HP:", hp, "/", maxhp)
                            print("Orc HP:", orchp, "/ 32")
                            
                    else:
                        orc = 1
                        print("The orc was defeated!")
                        sl(1)

                    print("")

                else:
                    print("")
                    luck = rn(1,6)
                    if luck > 1:
                        print("You kicked the orc!")
                        dmg = 1
                    else:
                        print("You lunged at the orc with full force!")
                        dmg = rn(8,12)
                    
                    sl(0.5)
                    orchp -= dmg
                    print("Dealt", dmg, "damage to the orc!")
                    sl(0.5)
                    if orchp > 0:
                        luck = rn(1,8)
                        if luck == 1:
                            print("The orc threw a punch!")
                            sl(0.5)
                            print("And missed!")
                            dmg = 0
                        elif luck == 2:
                            print("The orc hit you with all its might!")
                            dmg = rn(9,12)
                        else:
                            print("The orc threw a punch!")
                            dmg = rn(4,6)

                        sl(0.5)

                        hp-=dmg
                        print("You recieved", dmg, "damage!")

                        sl(0.5)

                        if hp <= 0:
                            end = -1
                            print("You were slain!")

                        else:
                            print("")
                            print("Your HP:", hp, "/", maxhp)
                            print("Orc HP:", orchp, "/ 32")
                            
                    else:
                        orc = 1
                        print("The orc was defeated!")
                        sl(1)

            elif move == "h":
                if apples > 0:
                    apples -= 1
                    
                    luck = rn(1,8)
                    if luck > 1:
                        hp += 8

                        if hp > maxhp:
                            hp = maxhp

                        print("")
                        print("You ate an apple.")
                        sl(1)
                        print("Recovered 8 HP!")
                        print("")

                    else:
                        orchp += 8
                        if orchp > 32:
                            orchp = 32

                        print("")
                        print("You pulled out an apple.")
                        sl(1)
                        print("The orc snatched it from you!")
                        sl(1)
                        print("The orc recovered 8 HP!")
                        print("")

                    sl(1)
                    print("Your HP:", hp, "/", maxhp)
                    print("Orc HP:", orchp, "/ 32")
                    print("")

                else:
                    print("")
                    print("You have no healing items.")
                    print("")

            elif move == "i":
                print("")
                print("That won't help now.")
                print("")

            else:
                print("")
                print("Invalid command!")
                print("")

    else:
        print("Obvious directions are east or south.")

        while change == 0:
            print("")
            move = input("What now? ")

            move = move.lower()

            if move == "s":
                nextroom = "cave"
                change = 1

            elif move == "e":
                nextroom = "field"
                change = 1

            elif move in ["n", "w"]:
                print("")
                print("You leapt off the cliff and died. Well done.")
                print("")
                change = 1
                end = -1

            elif move in ["u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "i":
                print("")
                print("There nothing to interact with.")
                print("")

            else:
                print("")
                print("Invalid command!")
                print("")

def field():
    change = 0

    global gatelk
    global hp
    global nextroom

    print("")
    print("You are in a field.")
    print("There is a campfire nearby.")
    print("Obvious directions are west, north and east.")

    while change==0:
        print("")
        move = input("What now? ")

        move = move.lower()

        if move in ["s", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "w":
            nextroom = "cliff"
            change = 1

        elif move == "n":
            nextroom = "forest"
            change = 1

        elif move == "e":
            if gatelk == 1:
                nextroom = "gate"
                change = 1
            else:
                print("")
                print("A colossal iron gate blocks your way.")
                print("")

        elif move == "i":
            print("")
            print("You rest by the campfire.")
            if hp < maxhp:
                heal = maxhp-hp
                hp = maxhp
                sl(1)
                print("You recovered",heal,"HP!")
            print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def forest():
    change = 0
    
    global nextroom
    global gatelk
    global hp
    global end

    print("")
    print("You are in the forest.")
    print("There is a pedestal nearby.")
    print("Obvious directions are south.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["n", "e", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "s":
            nextroom = "field"
            change = 1

        elif move == "i":
            if gatelk == 0:
                print("")
                print("The pedestal reads: ")
                print("The number I seek binds to you like tar")
                print("The count of the rooms you have entered thus far.")
                print("")
                print("There are buttons on the pedestal, labelled 1-6.")
                button=input("Which do you press? ")

                if button in ["1", "2", "3", "4", "5", "6"]:
                    if button == "4":
                        print("")
                        print("You hear a distant rumble.")
                        gatelk = 1
                    else:
                        print("")
                        print("An arrow is fired from the base of the pedestal!")
                        sl(1)
                        hp -= 10
                        print("You suffered 10 damage.")
                        sl(1)
                        if hp <= 0:
                                end = -1
                                print("You were slain!")
                                change = 1
                        else:
                            print("Your HP:", hp, "/", maxhp)
                            print("")
            
                else:
                    print("")
                    print("There is no button with that label.")
                    print("")

            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def gate():
    change = 0

    global nextroom
    
    print("")
    print("You are stood in the gateway.")
    print("Obvious directions are west, south and east.")
    print("")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["n", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "w":
            nextroom = "field"
            change = 1

        elif move == "s":
            nextroom = "river"
            change = 1

        elif move == "e":
            nextroom = "abbey"
            change = 1

        elif move == "i":
            print("")
            print("There is nothing to interact with.")
            print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def abbey():
    change = 0

    global nextroom
    global plank

    print("")
    print("You are in the abbey.")
    print("There are some wooden planks on the ground.")
    print("Obvious directions are west and up.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()
    
        if move in ["n", "e", "s", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "w":
            nextroom = "gate"
            change = 1

        elif move == "u":
            nextroom = "tower"
            change = 1

        elif move == "i":
            if plank == 0:
                plank = 1
                print("")
                print("You took one of the wooden planks.")
                print("")
            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def tower():
    change = 0

    global nextroom
    global coat
    global apples
    
    print("")
    print("You are in the tower.")
    print("Alongside you is a chest.")
    print("Obvious directions are down.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["n", "e", "s", "w", "u"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "d":
            nextroom = "abbey"
            change = 1

        elif move == "i":
            if coat == 0:
                coat = 1
                apples += 2

                print("")
                print("You opened the chest and found", end="\r")
                sl(0.5)
                print("You opened the chest and found.", end="\r")
                sl(0.5)
                print("You opened the chest and found..", end="\r")
                sl(0.5)
                print("You opened the chest and found...", end="\r")
                sl(0.5)
                print("You opened the chest and found a wool coat!")
                sl(0.5)
                print("You also found", end="\r")
                sl(0.5)
                print("You also found.", end="\r")
                sl(0.5)
                print("You also found..", end="\r")
                sl(0.5)
                print("You also found...", end="\r")
                sl(0.5)
                print("You also found 2 apples!")
                sl(0.5)
                print("")

            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def river():
    change = 0

    global nextroom
    global plank
    
    print("")
    print("You are stood on the riverbank.")
    print("Obvious directions are north and south.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["e", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "n":
            nextroom = "gate"
            change = 1

        elif move == "s":
            if plank != 2:
                print("")
                print("The river is too deep to cross.")
                print("")
            else:
                nextroom = "snow"
                change = 1

        elif move == "i":
            if plank == 1:
                print("")
                print("You placed the plank over the river.")
                print("")
                plank = 2
            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def snow():
    change = 0

    global nextroom
    global coat
    global hp
    global end
    
    print("")
    print("You are in a snowy field.")
    print("It is dangerously cold.")
    print("Obvious directions are north or south.")

    if coat == 0:
        sl(1)
        hp -= 20
        print("You suffered 20 frost damage.")
        sl(1)
        if hp <= 0:
            end = -1
            print("You froze to death!")
            change = 1
        else:
            print("Your HP:", hp, "/", maxhp)
            print("")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["e", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "n":
            nextroom = "river"
            change = 1

        elif move == "s":
            nextroom = "mountain"
            change = 1

        elif move == "i":
            print("")
            print("There is nothing to interact with.")
            print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def mountain():
    change = 0

    global nextroom
    global coat
    global hp
    global end
    global dur
    global boulder

    print("")
    print("You are at the base of the mountain.")
    print("There is a pedestal nearby.")
    print("Obvious directions are north and up.")

    if coat == 0:
        sl(1)
        hp -= 20
        print("You suffered 20 frost damage.")
        sl(1)
        if hp <= 0:
            end = -1
            print("You froze to death!")
            change = 1
        else:
            print("Your HP:", hp, "/", maxhp)
            print("")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["e", "s", "w", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "n":
            nextroom = "snow"
            change = 1

        elif move == "u":
            if boulder == 0:
                print("")
                print("A boulder blocks your path.")
                print("")
            else:
                nextroom = "castle"
                change = 1

        elif move == "i":
            if sword == 0:
                print("")
                print("There is a sword-shaped slit in the top of the pedestal.")
                print("")
            elif boulder == 0:
                dur = 12
                boulder = 1
                print("")
                print("You placed your sword in the pedestal.")
                sl(1)
                print("It emits a blinding flash of light", end = "\r")
                sl(0.5)
                print("It emits a blinding flash of light.", end = "\r")
                sl(0.5)
                print("It emits a blinding flash of light..", end = "\r")
                sl(0.5)
                print("It emits a blinding flash of light...")
                sl(0.5)
                print("You got the steel sword!")
                sl(1)
                print("The boulder has vanished!")
                print("")
            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def castle():
    change = 0

    global nextroom
    global apples
    global orc
    global orchp
    
    print("")
    print("You are outside the castle.")
    print("Nearby is a pair of scales.")
    print("Obvious directions are west and down.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["n", "e", "s", "u"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "w":
            if apples > 0:
                print("")
                print("The door is locked.")
                print("")
            else:
                orc = 0
                orchp = 64
                nextroom = "hall"
                change = 1

        elif move == "d":
            nextroom = "mountain"
            change = 1

        elif move == "i":
            if apples > 0:
                apples = 0
                print("")
                print("You place all of your apples onto the scales.")
                sl(1)
                print("You hear a faint click.")
                print("")
            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def hall():
    change = 0

    global nextroom
    global book
    global lever
    
    print("")
    print("You are in the hall.")
    print("Obvious directions are north, south, east and down.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["w", "u"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "e":
            print("")
            print("The door has locked behind you.")
            print("")

        elif move == "s":
            nextroom = "library"
            change = 1

        elif move == "n":
            if book == 1:
                nextroom = "chamber"
                change = 1
            else:
                print("")
                print("The door is locked.")
                print("")

        elif move == "d":
            if lever == 1:
                nextroom = "dungeon"
                change = 1
            else:
                print("")
                print("There is a metal grate on the floor.")
                print("")

        elif move == "i":
            print("")
            print("There is nothing to interact with.")
            print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def chamber():
    change = 0

    global nextroom
    global apples
    global lever
    
    print("")
    print("You are in the chamber.")
    print("There are four levers on the wall.")
    print("Obvious directions are south.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["n", "e", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "s":
            nextroom = "hall"
            change = 1

        elif move == "i":
            print("The levers are labeled as such:")
            print("##1##")
            print("2#C#3")
            print("##4##")
            print("")
            flip = input("Which will you pull? ")

            if flip == "1":
                print("")
                print("You hear a click under your feet.")
                sl(1)
                print("A trapdoor opens beneath you!")
                print("")
                nextroom = "cave"
                change = 1
            elif flip == "2":
                if apples == 0:
                    apples += 6
                    print("")
                    print("A hole opened up in the wall.")
                    sl(1)
                    print("You got 6 apples!")
                    print("")
                else:
                    print("")
                    print("Nothing happened.")
                    print("")
            elif flip == "3":
                print("")
                print("Nothing happened.")
                print("")
            elif flip == "4":
                if lever == 0:
                    lever = 1
                    print("")
                    print("You hear creaking behind you.")
                    sl(1)
                    print("The grate in the hall has opened!")
                    print("")
                else:
                    print("")
                    print("Nothing happened.")
                    print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def library():
    change = 0

    global nextroom
    global book
    global lever
    
    print("")
    print("You are in the library.")
    print("The lectern in front of you carries a book.")
    print("Obvious directions are north.")

    while change == 0:
        print("")
        move=input("What now? ")
    
        move=move.lower()

        if move in ["e", "s", "w", "u", "d"]:
            print("")
            print("You cannot move in that direction.")
            print("")

        elif move == "n":
            nextroom = "hall"
            change = 1

        elif move == "i":
            if book == 0:
                book = 1
                print("")
                print("You take the book from the lectern.")
                sl(1)
                print("It reads:")
                print("Let     my        seal      tomb")
                print("      the      of     very        room.")
                print("")
                sl(1)
                print("You hear scraping in the hall.")
                print("The northern door has unlocked!")
                print("")

            elif lever == 0:
                print("")
                print("There is nothing to interact with.")
                print("")
                
            elif book == 1:
                book = 2
                print("")
                print("Another book has appeared on the lectern.")
                print("You take the book.")
                sl(1)
                print("It reads:")
                print("    not    secret      your     ")
                print("Utter     name    the      second      ")
                
            else:
                print("")
                print("There is nothing to interact with.")
                print("")

        else:
            print("")
            print("Invalid command!")
            print("")

def dungeon():
    change = 0

    global book
    global dur
    global apples
    global hp
    global maxhp
    global orc
    global end
    global orchp
    global nextroom

    print("")
    print("You are stood in the dungeon.")
    if orc == 0:
        sl(0.5)
        print("An ominous figure approaches you", end="\r")
        sl(0.5)
        print("An ominous figure approaches you.", end="\r")
        sl(0.5)
        print("An ominous figure approaches you..", end="\r")
        sl(0.5)
        print("An ominous figure approaches you...")
        sl(0.5)
        print("An orc emerged from the shadows!")

        sl(0.5)

        while orc == 0 and end == 0:
            print("")
            move = input("What now? ")

            move = move.lower()

            if move in ["n", "e", "s", "w", "u", "d"]:
                print("")
                print("You can't run now!")
                print("")

            elif move == "a":
                if dur > 0 and sword == 1:
                    print("")
                    print("You swung your sword at the orc!")

                    luck = rn(1,8)
                    if luck == 1:
                        sl(0.5)
                        print("The orc reflected the damage!")
                        dmg = rn(3,5)
                    elif luck == 2:
                        sl(0.5)
                        print("You landed a critical hit!")
                        dmg = rn(14,16)
                    else:
                        dmg = rn(3,5)

                    sl(0.5)

                    if luck != 1:
                        orchp -= dmg
                        print("Dealt", dmg, "damage to the orc!")
                    else:
                        hp -= dmg
                        print("You recieved", dmg, "damage!")
                    
                    sl(0.5)

                    dur -= 1
                    if dur == 0:
                        print("Your sword broke!")
                        dmg = rn(4,7)
                        sl(0.5)
                        orchp -= dmg
                        print("Shrapnel hit the orc, dealing", dmg, "damage!")

                    sl(0.5)

                    if orchp > 0:
                        luck = rn(1,8)
                        if luck == 1:
                            print("The orc threw a punch!")
                            sl(0.5)
                            print("And missed!")
                            dmg = 0
                        elif luck == 2:
                            print("The orc cursed you!")
                            dmg = rn(6,8)
                        else:
                            print("The orc threw a punch!")
                            dmg = rn(4,6)

                        sl(0.5)

                        hp-=dmg
                        print("You recieved", dmg, "damage!")

                        if luck == 2:
                            sl(0.5)
                            maxhp -= dmg
                            print("Your maximum HP was reduced by", dmg, "points!")

                        sl(0.5)

                        if hp <= 0:
                            end = -1
                            print("You were slain!")

                        else:
                            print("")
                            print("Your HP:", hp, "/", maxhp)
                            print("Orc HP:", orchp, "/ 64")
                            
                    else:
                        orc = 1
                        print("The orc was defeated!")
                        sl(1)

                    print("")

                else:
                    print("")
                    luck = rn(1,6)
                    if luck > 1:
                        print("You kicked the orc!")
                        dmg = 1
                    else:
                        print("You lunged at the orc with full force!")
                        dmg = rn(4,8)
                    
                    sl(0.5)
                    orchp -= dmg
                    print("Dealt", dmg, "damage to the orc!")
                    sl(0.5)
                    if orchp > 0:
                        luck = rn(1,8)
                        if luck == 1:
                            print("The orc threw a punch!")
                            sl(0.5)
                            print("And missed!")
                            dmg = 0
                        elif luck == 2:
                            print("The orc cursed you!")
                            dmg = rn(6,8)
                        else:
                            print("The orc threw a punch!")
                            dmg = rn(4,6)

                        sl(0.5)

                        hp-=dmg
                        print("You recieved", dmg, "damage!")

                        if luck == 2:
                            sl(0.5)
                            maxhp -= dmg
                            print("Your maximum HP was reduced by", dmg, "points!")

                        sl(0.5)

                        if hp <= 0:
                            end = -1
                            print("You were slain!")

                        else:
                            print("")
                            print("Your HP:", hp, "/", maxhp)
                            print("Orc HP:", orchp, "/ 64")
                            
                    else:
                        orc = 1
                        print("The orc was defeated!")
                        sl(1)

            elif move == "h":
                if apples > 0:
                    apples -= 1
                    
                    luck = rn(1,8)
                    if luck > 2:
                        hp += 8

                        if hp > maxhp:
                            hp = maxhp

                        print("")
                        print("You ate an apple.")
                        sl(1)
                        print("Recovered 8 HP!")
                        print("")

                    elif luck == 2:
                        heal=maxhp-hp
                        hp = maxhp
                        maxhp += 8

                        print("")
                        print("You ate an apple.")
                        sl(1)
                        print("The apple was enchanted!")
                        sl(1)
                        print("Recovered", heal, "HP!")
                        sl(1)
                        print("Your maximum HP was increased by 8 points!")

                    else:
                        print("")
                        print("You pulled out an apple.")
                        sl(1)
                        print("The orc crushed it!")
                        print("")

                    sl(1)
                    print("Your HP:", hp, "/", maxhp)
                    print("Orc HP:", orchp, "/ 64")
                    print("")

                else:
                    print("")
                    print("You have no healing items.")
                    print("")

            elif move == "i":
                print("")
                print("That won't help now.")
                print("")

            else:
                print("")
                print("Invalid command!")
                print("")

    else:
        print("There is a gigantic golden door in front of you.")
        print("Obvious directions are north.")

        while change == 0:
            print("")
            move=input("What now? ")
    
            move=move.lower()

            if move in ["e", "s", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "n":
                print("")
                print("You push open the golden door, and take a step through.")
                print("")
                sl(1)
                change = 1
                end = 1

            elif move == "i":
                if book == 2:
                    print("")
                    print("In a moment of inspiration, you piece the two books together.")
                    sl(1)
                    print("Combined, it reads:")
                    print("Let not my secret seal your tomb")
                    print("Utter the name of the very second room.")
                    print("")
                    code = input("What do you say?")
                    
                    code = code.lower()

                    if code == "cliff":
                        dur = 0
                        apples = 0
                        nextroom = "cave"
                        maxhp += 10
                        hp = maxhp - 20
                        orc = 0
                        orchp = 32
                        gatelk = 0
                        coat = 0
                        plank = 0
                        boulder = 0
                        book = 0
                        lever = 0
                        change = 1
                        print("")
                        print("You have unlocked hard mode. Good luck!")
                        print("A blinding glow surrounds you...")
                        print("")
                        sl(2)
                        print("\n"*100)
                    else:
                        print("")
                        print("Your words echo upon deaf ears. ")
                        print("")

                else:
                    print("")
                    print("There is nothing to interact with.")
                    print("")

            else:
                print("")
                print("Invalid command!")
                print("")

while end == 0:
    if nextroom == "cave":
        cave()
    if nextroom == "cliff":
        cliff()
    if nextroom == "field":
        field()
    if nextroom == "forest":
        forest()
    if nextroom == "gate":
        gate()
    if nextroom == "abbey":
        abbey()
    if nextroom == "tower":
        tower()
    if nextroom == "river":
        river()
    if nextroom == "snow":
        snow()
    if nextroom == "mountain":
        mountain()
    if nextroom == "castle":
        castle()
    if nextroom == "hall":
        hall()
    if nextroom == "chamber":
        chamber()
    if nextroom == "library":
        library()
    if nextroom == "dungeon":
        dungeon()
                
if end == 1:
    print("")
    print("Your did it!!!")
    sl(4)

if end == -1:
    print("")
    print("Game over!")
    sl(4)
