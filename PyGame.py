from random import randint as rn
from time import sleep as sl

def game():
    # Init variables
    sword = False
    dur = 8
    apples = 0
    nextroom = "cave"
    end = 0
    hp = 40
    maxhp = 40
    orc = False
    orchp = 32
    gatelk = False
    coat = False
    plank = 0
    boulder = False
    book = 0
    lever = False

    print("Commands:")
    print("n, e, s, w, u, d: Move in a direction")
    print("i: Interact with an object")
    print("a: Attack (while in battle)")
    print("h: Heal (while in battle)")
    print("")

    sl(2)

    # Each room is a function
    def cave(sword,apples,nextroom):
        change = False

        print("")
        print("You are in a cave.")
        print("Alongside you is a chest.")
        print("Obvious directions are north.")
        
        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()
            
            # Invalid directions
            if move in ["e", "s", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move=="n":
                # Move to next room
                nextroom = "cliff"
                change = True

            elif move=="i":
                if not sword:
                    # Give sword and apples
                    sword = True
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
                    # Prevent multiple chest openings
                    print("")
                    print("There is nothing to interact with.")
                    print("")

            else:
                print("")
                print("Invalid command!")
                print("")
        
        # Pass items to main program
        return [sword,apples,nextroom]
            
    def cliff(sword,dur,apples,hp,maxhp,orc,end,orchp,nextroom):
        change = False

        print("")
        print("You are walking alongside a cliff.")
        if not orc:
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

            while orc == False and end == 0:
                print("")
                move = input("What now? ")

                move = move.lower()

                # Prevent fleeing
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
                    if dur > 0 and sword == True:
                        print("")
                        print("You swung your sword at the orc!")

                        # Attack RNG
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

                        # Durability system
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
                            # Orc attack RNG
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
                                # Exit main with code -1 (game over)
                                end = -1
                                print("You were slain!")

                            else:
                                print("")
                                print("Your HP:", hp, "/", maxhp)
                                print("Orc HP:", orchp, "/ 32")
                                
                        else:
                            orc = True
                            print("The orc was defeated!")
                            sl(1)

                        print("")

                    else:
                        print("")
                        # For broken sword
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
                            orc = True
                            print("The orc was defeated!")
                            sl(1)

                elif move == "h":
                    if apples > 0:
                        apples -= 1
                        
                        luck = rn(1,8)
                        if luck > 1:
                            hp += 8

                            # Prevent HP overflow
                            if hp > maxhp:
                                hp = maxhp

                            print("")
                            print("You ate an apple.")
                            sl(1)
                            print("Recovered 8 HP!")
                            print("")

                        else:
                            # The orc has a chance steal your apples, what a melt
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
                    change = True

                elif move == "e":
                    nextroom = "field"
                    change = True

                elif move in ["n", "w"]:
                    print("")
                    print("You leapt off the cliff and died. Well done.")
                    print("")
                    change = True
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

        return [sword,dur,apples,hp,maxhp,orc,end,orchp,nextroom]



    def field(gatelk,hp,nextroom):
        change = False

        print("")
        print("You are in a field.")
        print("There is a campfire nearby.")
        print("Obvious directions are west, north and east.")

        while not change:
            print("")
            move = input("What now? ")

            move = move.lower()

            if move in ["s", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "w":
                nextroom = "cliff"
                change = True

            elif move == "n":
                nextroom = "forest"
                change = True

            elif move == "e":
                if gatelk:
                    nextroom = "gate"
                    change = True
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

        return [gatelk,hp,nextroom]

    def forest(nextroom,gatelk,hp,end):
        change = False

        print("")
        print("You are in the forest.")
        print("There is a pedestal nearby.")
        print("Obvious directions are south.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["n", "e", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "s":
                nextroom = "field"
                change = True

            elif move == "i":
                if not gatelk:
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
                            gatelk = True
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
                                    change = True
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

        return [nextroom,gatelk,hp,end]

    def gate(nextroom):
        change = False
        
        print("")
        print("You are stood in the gateway.")
        print("Obvious directions are west, south and east.")
        print("")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["n", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "w":
                nextroom = "field"
                change = True

            elif move == "s":
                nextroom = "river"
                change = True

            elif move == "e":
                nextroom = "abbey"
                change = True

            elif move == "i":
                print("")
                print("There is nothing to interact with.")
                print("")

            else:
                print("")
                print("Invalid command!")
                print("")

        return nextroom

    def abbey(nextroom,plank):
        change = False

        print("")
        print("You are in the abbey.")
        print("There are some wooden planks on the ground.")
        print("Obvious directions are west and up.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()
        
            if move in ["n", "e", "s", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "w":
                nextroom = "gate"
                change = True

            elif move == "u":
                nextroom = "tower"
                change = True

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

        return [nextroom,plank]

    def tower(nextroom,coat,apples):
        change = False

        print("")
        print("You are in the tower.")
        print("Alongside you is a chest.")
        print("Obvious directions are down.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["n", "e", "s", "w", "u"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "d":
                nextroom = "abbey"
                change = True

            elif move == "i":
                if not coat:
                    coat = True
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

        return [nextroom,coat,apples]

    def river(nextroom,plank):
        change = False
        
        print("")
        print("You are stood on the riverbank.")
        print("Obvious directions are north and south.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["e", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "n":
                nextroom = "gate"
                change = True

            elif move == "s":
                # The player cannot progress without the plank
                if plank != 2:
                    print("")
                    print("The river is too deep to cross.")
                    print("")
                else:
                    nextroom = "snow"
                    change = True

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

        return [nextroom,plank]

    def snow(nextroom,coat,hp,end):
        change = False
        
        print("")
        print("You are in a snowy field.")
        print("It is dangerously cold.")
        print("Obvious directions are north or south.")

        if not coat:
            sl(1)
            # The player will die without the coat
            hp -= 20
            print("You suffered 20 frost damage.")
            sl(1)
            if hp <= 0:
                end = -1
                print("You froze to death!")
                change = True
            else:
                print("Your HP:", hp, "/", maxhp)
                print("")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["e", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "n":
                nextroom = "river"
                change = True

            elif move == "s":
                nextroom = "mountain"
                change = True

            elif move == "i":
                print("")
                print("There is nothing to interact with.")
                print("")

            else:
                print("")
                print("Invalid command!")
                print("")

        return [nextroom,coat,hp,end]

    def mountain(nextroom,coat,hp,end,dur,boulder):
        change = False

        print("")
        print("You are at the base of the mountain.")
        print("There is a pedestal nearby.")
        print("Obvious directions are north and up.")

        if not coat:
            sl(1)
            hp -= 20
            print("You suffered 20 frost damage.")
            sl(1)
            if hp <= 0:
                end = -1
                print("You froze to death!")
                change = True
            else:
                print("Your HP:", hp, "/", maxhp)
                print("")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["e", "s", "w", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "n":
                nextroom = "snow"
                change = True

            elif move == "u":
                if boulder == False:
                    print("")
                    print("A boulder blocks your path.")
                    print("")
                else:
                    nextroom = "castle"
                    change = True

            elif move == "i":
                if sword == False:
                    # The player cannot progress without the sword
                    print("")
                    print("There is a sword-shaped slit in the top of the pedestal.")
                    print("")
                elif boulder == False:
                    # Repair sword
                    dur = 12
                    boulder = True
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

        return [nextroom,coat,hp,end,dur,boulder]

    def castle(nextroom,apples,orc,orchp):
        change = False
        
        print("")
        print("You are outside the castle.")
        print("Nearby is a pair of scales.")
        print("Obvious directions are west and down.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["n", "e", "s", "u"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "w":
                # The player cannot progress if they have apples
                if apples > 0:
                    print("")
                    print("The door is locked.")
                    print("")
                else:
                    orc = False
                    orchp = 64
                    nextroom = "hall"
                    change = True

            elif move == "d":
                nextroom = "mountain"
                change = True

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

        return [nextroom,apples,orc,orchp]

    def hall(nextroom,book,lever):
        change = False
        
        print("")
        print("You are in the hall.")
        print("Obvious directions are north, south, east and down.")

        while not change:
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
                change = True

            elif move == "n":
                if book == 1:
                    nextroom = "chamber"
                    change = True
                else:
                    print("")
                    print("The door is locked.")
                    print("")

            elif move == "d":
                if lever:
                    nextroom = "dungeon"
                    change = True
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

        return [nextroom,book,lever]

    def chamber(nextroom,apples,lever):
        change = False
        
        print("")
        print("You are in the chamber.")
        print("There are four levers on the wall.")
        print("Obvious directions are south.")

        while not change:
            print("")
            move=input("What now? ")
        
            move=move.lower()

            if move in ["n", "e", "w", "u", "d"]:
                print("")
                print("You cannot move in that direction.")
                print("")

            elif move == "s":
                nextroom = "hall"
                change = True

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
                    # Get trolled nerd
                    nextroom = "cave"
                    change = True
                elif flip == "2":
                    if apples == 0:
                        apples += 8
                        print("")
                        print("A hole opened up in the wall.")
                        sl(1)
                        print("You got 8 apples!")
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
                    if lever == False:
                        lever = True
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
                    print("There is no lever with that label.")
                    print("")

            else:
                print("")
                print("Invalid command!")
                print("")

        return [nextroom,apples,lever]

    def library(nextroom,book,lever):
        change = False
        
        print("")
        print("You are in the library.")
        print("The lectern in front of you carries a book.")
        print("Obvious directions are north.")

        while change == False:
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

                elif not lever:
                    print("")
                    print("There is nothing to interact with.")
                    print("")
                    
                elif book == 1:
                    # Rewards the player for backtracking, this is how you unlock hard mode
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

        return [nextroom,book,lever]

    def dungeon(book,dur,apples,hp,maxhp,orc,end,orchp,nextroom):
        change = False

        print("")
        print("You are stood in the dungeon.")
        if not orc:
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

            while orc == False and end == 0:
                print("")
                move = input("What now? ")

                move = move.lower()

                if move in ["n", "e", "s", "w", "u", "d"]:
                    print("")
                    print("You can't run now!")
                    print("")

                elif move == "a":
                    if dur > 0 and sword == True:
                        print("")
                        print("You swung your sword at the orc!")

                        luck = rn(1,8)
                        if luck == 1:
                            sl(0.5)
                            # This orc is magic, shiver me timbers
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
                                # It's wizard time babey
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
                            orc = True
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
                            orc = True
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
                            # Healing is better to balance the final fight
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
                            # What a meanie
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

            while not change:
                print("")
                move=input("What now? ")
        
                move=move.lower()

                if move in ["e", "s", "w", "u", "d"]:
                    print("")
                    print("You cannot move in that direction.")
                    print("")

                elif move == "n":
                    # Exits main with code 1 (your did it)
                    print("")
                    print("You push open the golden door, and take a step through.")
                    print("")
                    sl(1)
                    change = True
                    end = 1

                elif move == "i":
                    if book == 2:
                        # Requires both books to be collected
                        print("")
                        print("In a moment of inspiration, you piece the two books together.")
                        sl(1)
                        print("Combined, it reads:")
                        print("Let not my secret seal your tomb")
                        print("Utter the name of the very second room.")
                        print("")
                        code = input("What do you say? ")
                        
                        code = code.lower()

                        if code == "cliff":
                            # Unlock hard mode
                            dur = 0
                            apples = 4
                            nextroom = "cave"
                            maxhp += 40
                            hp = maxhp - 20
                            orc = False
                            orchp = 32
                            gatelk = False
                            coat = False
                            plank = 0
                            boulder = False
                            book = 0
                            lever = False
                            change = True
                            
                            print("")
                            print("You have unlocked hard mode. Good luck!")
                            print("A blinding glow surrounds you...")
                            print("")
                            sl(4)
                            # """Clear""" the screen
                            print("\n"*100)
                        else:
                            # You got it wrong, womp womp
                            print("")
                            print("Your words echo upon deaf ears.")
                            print("")

                    else:
                        print("")
                        print("There is nothing to interact with.")
                        print("")

                else:
                    print("")
                    print("Invalid command!")
                    print("")

        return [book,dur,apples,hp,maxhp,orc,end,orchp,nextroom]

    while end == 0:
        if nextroom == "cave":
            # Take output of function as an array
            vals = cave(sword,apples,nextroom)
            # Set variables
            sword = vals[0]
            apples = vals[1]
            nextroom = vals[2]

        if nextroom == "cliff":
            vals = cliff(sword,dur,apples,hp,maxhp,orc,end,orchp,nextroom)
            sword = vals[0]
            dur = vals[1]
            apples = vals[2]
            hp = vals[3]
            maxhp = vals[4]
            orc = vals[5]
            end = vals[6]
            orchp = vals[7]
            nextroom = vals[8]

        if nextroom == "field":
            vals = field(gatelk,hp,nextroom)
            gatelk = vals[0]
            hp = vals[1]
            nextroom = vals[2]

        if nextroom == "forest":
            vals = forest(nextroom,gatelk,hp,end)
            nextroom = vals[0]
            gatelk = vals[1]
            hp = vals[2]
            end = vals[3]

        if nextroom == "gate":
            nextroom = gate(nextroom)

        if nextroom == "abbey":
            vals = abbey(nextroom,plank)
            nextroom = vals[0]
            plank = vals[1]

        if nextroom == "tower":
            vals = tower(nextroom,coat,apples)
            nextroom = vals[0]
            coat = vals[1]
            apples = vals[2]

        if nextroom == "river":
            vals = river(nextroom,plank)
            nextroom = vals[0]
            plank = vals[1]

        if nextroom == "snow":
            vals = snow(nextroom,coat,hp,end)
            nextroom = vals[0]
            coat = vals[1]
            hp = vals[2]
            end = vals[3]

        if nextroom == "mountain":
            vals = mountain(nextroom,coat,hp,end,dur,boulder)
            nextroom = vals[0]
            coat = vals[1]
            hp = vals[2]
            end = vals[3]
            dur = vals[4]
            boulder = vals[5]

        if nextroom == "castle":
            vals = castle(nextroom,apples,orc,orchp)
            nextroom = vals[0]
            apples = vals[1]
            orc = vals[2]
            orchp = vals[3]

        if nextroom == "hall":
            vals = hall(nextroom,book,lever)
            nextroom = vals[0]
            book = vals[1]
            lever = vals[2]

        if nextroom == "chamber":
            vals = chamber(nextroom,apples,lever)
            nextroom = vals[0]
            apples = vals[1]
            lever = vals[2]

        if nextroom == "library":
            vals = library(nextroom,book,lever)
            nextroom = vals[0]
            book = vals[1]
            lever = vals[2]

        if nextroom == "dungeon":
            vals = dungeon(book,dur,apples,hp,maxhp,orc,end,orchp,nextroom)
            book = vals[0]
            dur = vals[1]
            apples = vals[2]
            hp = vals[3]
            maxhp = vals[4]
            orc = vals[5]
            end = vals[6]
            orchp = vals[7]
            nextroom = vals[8]

    def calcscore(list):
        sum = 0
        for x in list:
            try:
                sum += x
            except TypeError:
                0 # Placeholder for try to work
            else:
                for y in range(1):
                   break # Placeholder for try to work, also more free points
        return sum
              
    if end == 1:
        end = int(float(bool(str(end)))//1) # Wow, free points!
        
        stats = {
            "Health": hp,
            "Max health": maxhp,
            "Weapon durability": dur,
            "No. apples": apples
        }

        SCORE = calcscore([hp, maxhp, dur, apples]) # This is a constant, it doesn't change
        print("")
        print(stats)
        print("")
        print("Your final score is", SCORE)
        try:
            file = open("highscore.txt", "r")
        except FileNotFoundError:
            # Create highscore file if it doesn't exist
            print("No high score found!")
            file = open("highscore.txt", "w")
            file.write(str(SCORE))
            file.close()
        else:
            hscore = int(file.read())
            file.close()
            if SCORE > hscore:
                # Update high score if beaten
                print("This beats the previous high score of", hscore)
                file = open("highscore.txt", "w")
                file.write(str(SCORE))
                file.close()
            else:
                print("The current high score is", hscore)
        sl(1)
        print("")
        print("Your did it!!!")
        sl(4)

    if end == -1:
        print("")
        print("Game over!")
        sl(4)

# The entire game is a function to make it not global
game()
