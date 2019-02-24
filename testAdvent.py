#Michael Liamkin, Tyler Gutowski
#2/14/2019
#Space adventure

import random
import time
import sys
from time import sleep
from os import system, name 

#CODE: https://www.geeksforgeeks.org/clear-screen-python/

##DEFAULT TYPESPEED IS TYPESPEED
##DEFAULT TYPEWAITTIME IS 0.5
TYPESPEEDS = 0.04
TYPESPEEDM = 0.025
TYPESPEEDF = 0.015
TYPESPEEDN = 0
TYPEWAITTIMES = 0.75
TYPEWAITTIMEM = 0.5
TYPEWAITTIMEF = 0.35
TYPEWAITTIMEN = 0


TYPESPEEDTYPESN = "Slow"
TYPESPEEDTYPEMN = "Medium"
TYPESPEEDTYPEFN = "Fast"
TYPESPEEDTYPENN = "None"
TYPEWAITTIMESN = "Slow"
TYPEWAITTIMEMN = "Medium"
TYPEWAITTIMEFN = "Fast"
TYPEWAITTIMENN = "None"

TYPESPEED = TYPESPEEDM
TYPEWAITTIME = TYPEWAITTIMEM
def clear(): 
    if name == 'nt': 
        _ = system('cls')
GERMANFIRSTNAMES = ["Wolfgang","Günter","Heinz","Hans","Friedrich","Wilhelm"]

GERMANLASTNAMES = ["Steinway","Werner","Konrad","Ziegler","Frank","Krause"]

NAME = GERMANFIRSTNAMES[random.randint(0,len(GERMANFIRSTNAMES)-1)] + " " + GERMANLASTNAMES[random.randint(0,len(GERMANLASTNAMES)-1)]

LISTRESPONSES = ["This answer does not exist, you need to try again.", "Invalid answer. Try again.",\
                 "Your typing skills are not very good, you need to try again.",\
                 "Have you ever used a computer keyboard before? You need to try again",\
                 "Your answer does not make sense, try again",\
                 "Do you know what a number is? Type your answer again being mindful about the number keys on the top of your keyboard",\
                 "What kind of vision do you have? Do you not see the keyboard? Try again."]
LIST = ["your pet Venus Flytrap","your jar of baby teeth","your plastic tupperware container full of weiner schnitzels","your smallest pair of clown shoes",\
        "your second favorite Christmas tree","your lucky glow-in-the-dark snorkle", "your favorite purple pen", "your red superhero cape"]

line1 = "December 26th, 2240\n\n" + \
        "You are "+NAME+", a 50-year old German man, making your way across the galaxy in a spaceship at the speed of light towards Planet Galactus - a life-bearing planet about half a light year away with no established human civilization.\n\n"
line2 = "2 Hours Prior:\n"

alert1 = "Buzzzz Buzzzz - *BREAKING NEWS* SCIENTISTS PREDICT AN 80-MILE WIDE ASTEROID WILL HIT PLANET EARTH IN 2 HOURS TIME! PREPARE . . . \n\n"
                
line3 = "Waking up completely shocked, you get on your Samsung Galaxy S229 to confirm the shocking news you just heard.\n\n" + \
        "Unfortunately, you find out the inevitable - all life on Earth will be wiped out in 2 hours." + \
        " You quickly run and fill your spaceship in your garage with all of your valuables and your Food Generator™.  You have space for only one more item.\n\n"


#####CHOICES#####


LONEWOLF = False #Fly alone

PASSIVE = False #Don't aggro the spacemen

TOOKABEATING = False #Gets beat up

SENTIMENTAL = False #Keeps your saveItem

INJURED = False #You got yourself hurt

SLOWPOKE = False #You slow down for the asteroid belt

FIGHTER = False #Try to escape or wriggle free

DAMAGEDSHIP = False #You damaged your ship

MONSTER = False #You attacked the defenseless bandit

OUTOFFUEL = False #You run out of fuel

DAMAGEDSHIP = False #You damage your ship

EASYLIVING = False #Everything goes right

#################


#CODE: https://stackoverflow.com/questions/20302331/typing-effect-in-python
print(" ______     _____     __   __   ______     __   __     ______   __  __     ______     ______           ______     ______     __         ______     ______     ______   __  __     ______    ")
print("/\  __ \   /\  __-.  /\ \ / /  /\  ___\   /\ '-.\ \   /\__  _\ /\ \/\ \   /\  == \   /\  ___\         /\  ___\   /\  __ \   /\ \       /\  __ \   /\  ___\   /\__  _\ /\ \/\ \   /\  ___\   ")
print("\ \  __ \  \ \ \/\ \ \ \ \' /   \ \  __\   \ \ \-.  \  \/_/\ \/ \ \ \_\ \  \ \  __<   \ \  __\         \ \ \__ \  \ \  __ \  \ \ \____  \ \  __ \  \ \ \____  \/_/\ \/ \ \ \_\ \  \ \___  \  ")
print(" \ \_\ \_\  \ \____-  \ \__|    \ \_____\  \ \_\\'\ _\    \ \_\  \ \_____\  \ \_\ \_\  \ \_____\        \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \ \_____\    \ \_\  \ \_____\  \/\_____\ ")
print("  \/_/\/_/   \/____/   \/_/      \/_____/   \/_/ \/_/     \/_/   \/_____/   \/_/ /_/   \/_____/         \/_____/   \/_/\/_/   \/_____/   \/_/\/_/   \/_____/     \/_/   \/_____/   \/_____/ ")
sleep(3)
print("\nOPTIONS:")
print("  For full immersion, we recommend you keep all settings at 'Medium'")
print("  Text Speed = " + TYPESPEEDTYPEMN)
print("  Text Delay = " + TYPEWAITTIMEMN)
cont = True
while (cont):
    options = input("  ++ Press 1 to change the text delay\n  ++ Press 2 to change the text speed\n  ++ Press 3 to continue\n\n")
    if (options == "1"):
        cont1 = True
        while (cont1):
            ts = input("  ++ Press 1 for slow text speed\n  ++ Press 2 for medium text speed\n  ++ Press 3 for fast text speed\n  ++ Press 4 for no text speed\n\n")
            if(ts == "1"):
                TYPEWAITTIME = TYPEWAITTIMES
                cont1 = False
            elif(ts == "2"):
                TYPEWAITTIME = TYPEWAITTIMEM
                cont1 = False
            elif(ts == "3"):
                TYPEWAITTIME = TYPEWAITTIMEF
                cont1 = False
            elif(ts == "4"):
                TYPEWAITTIME = TYPEWAITTIMEN
                cont1 = False
            else:
                print("")
                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                print("")
                cont1 = True
    elif (options == "2"):
        cont1 = True
        while (cont1):
            ts = input("  ++ Press 1 for slow text delay\n  ++ Press 2 for medium text delay\n  ++ Press 3 for fast text delay\n  ++ Press 4 for no text delay\n\n")
            if(ts == "1"):
                TYPESPEED = TYPESPEEDS
                cont1 = False
            elif(ts == "2"):
                TYPESPEED = TYPESPEEDM
                cont1 = False
            elif(ts == "3"):
                TYPESPEED = TYPESPEEDF
                cont1 = False
            elif(ts == "4"):
                TYPESPEED = TYPESPEEDN
                cont1 = False
            else:
                print("")
                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                print("")
                cont1 = True
    elif (options == "3"):
        cont = False
    else:
        print("")
        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
        print("")
        cont = True
for s in line1:
    sleep(TYPESPEED)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(TYPEWAITTIME)

for s in line2:
    sleep(TYPESPEED)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(TYPEWAITTIME)

for s in alert1:
    sleep(TYPESPEED)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(TYPEWAITTIME)

for s in line3:
    sleep(TYPESPEED)
    sys.stdout.write(s)
    sys.stdout.flush()

randomItem1 = LIST[random.randint(0,3)]
randomItem2 = LIST[random.randint(4,6)]

print("You can either bring " + randomItem1 + ", or " + randomItem2 + ".")
print("")

#
cont = True
while (cont):
    a = input("++ Press 1 to bring " + randomItem1 + ". \n++ Press 2 to bring " + randomItem2 + ".\n\n")
    if (a == "1"):
        saveItem = randomItem1
        cont = False
    elif (a == "2"):
        saveItem = randomItem2
        cont = False
    else:
        print("")
        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
        print("")
        cont = True

line4 = "\nYou start your engine and fly up through the atmosphere, seeing the asteroid in the distance.\n\n" + \
        "Noticing the crowd of spaceships leaving alongside of you, do you decide to follow them or fly alone?\n\n"

for s in line4:
    sleep(TYPESPEED)
    sys.stdout.write(s)
    sys.stdout.flush()

##
cont = True
while (cont):
    a = input("++ Press 1 to fly along with the others. \n++ Press 2 to fly alone.\n\n")

    
    if (a == "1"):
        line5 = "\nYou follow a trio of spaceships, and put your ship on autopilot along your planned route to Planet Galactus\n"  + \
                "You decide to introduce yourself to the others.\n" + \
                "The other ships tell you that there has been word of space robbers between planets X3245 and X4561.\n\n" + \
                "You make note of the warning, and update your route around the location of the robbers.\n" + \
                "Returning from a trip to your Food Creator™ to get a cup of tea, you trip and spill tea all over your space radio.\n" + \
                "Your begin to hear static noise from your radio. Unconcerned, you are sure that the radio was warning about the space robbers.\n" + \
                "You brush your teeth, admire " + saveItem + ", and go to sleep.\n\n"
        for s in line5:
            sleep(TYPESPEED)
            sys.stdout.write(s)
            sys.stdout.flush()
        sleep(TYPEWAITTIME)
        line15 = "The next morning, you notice the ships that you were following are completely out of sight.\n" + \
                 "Confused, you check your radar to locate the other ships, and you see they went around quadrant 271.\n" + \
                 "You think they might have made a mistake, and decide to meet up with them by going through quadrant 271.\n\n" + \
                 "Approaching the region, you start hearing little ticks on your ship - like small objects hitting it.\n"+\
                 "You don't want to delay your trip by too much, but you're not sure what lies ahead."
        for s in line15:
            sleep(TYPESPEED)
            sys.stdout.write(s)
            sys.stdout.flush()
        cont8 = True

###
        while (cont8):
            a = input("\n++ Press 1 to keep going through the region full speed. \n++ Press 2 to slow down.\n\n")

            
            if (a == "1"):
                
                line16 = "\nThe ticks on your ship keep getting louder and louder, until you see full blown asteroids in front of you.\n" + \
                         "You are forced to take manual control of the ship and need to steer away from the asteroids."
                for s in line16:
                    sleep(TYPESPEED)
                    sys.stdout.write(s)
                    sys.stdout.flush()
                hitanything = False
                #TY: ASTEROIDS MOVE FAST
                if(hitanything):
                    DAMAGEDSHIP = True
                    GOTOMERCHANTSTATION = True
                cont8 = False
            elif (a == "2"):
                SLOWPOKE = True
                line16 = "\nThe ticks on your ship keep getting louder and louder, until you see full blown asteroids in front of you.\n" + \
                         "You are forced to take manual control of the ship and need to steer away from the asteroids."
                for s in line16:
                    sleep(TYPESPEED)
                    sys.stdout.write(s)
                    sys.stdout.flush()
                hitanything = False
                #TY: ASTEROIDS MOVE SLOWLY
                if(hitanything):
                    DAMAGEDSHIP = True
                    GOTOMERCHANTSTATION = True
                cont8 = False
            else:
                print("")
                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                print("")
                cont8 = True
        cont = False
        
        
        
    elif (a == "2"):
        cont = False
        LONEWOLF = True
        line6 = "\nYou look at your SPS (Space Positioning System) and follow a planned out route to Planet Galactus estimated to take about 6 months.\n\n" + \
                "*TO ALL THOSE LEAVING EARTH AND HEADING TOWARDS PLANET GALACTUS* BEWARE OF AN ASTEROID BELT IN QUADRANT 271. YOU MUST URGENTLY PLAN TO NAVIGATE AROUND THE BELT!*\n\n" + \
                "You update your route on your SPS, thankful for the warning on your space radio.\n" + \
                "You put your ship on auto-pilot, lay back, and fall asleep while admiring " + saveItem + ".\n\n" + \
                "The next day,\n" + \
                "As you approach between planets X3245 and X4561, you see something white approaching you from behind, growing larger and larger, until\n\n" + \
                "WHAM!\n\n" + \
                "You hear a loud clang and feel your ship shake.\n" + \
                "Confused, you look out your rear view space mirror, and notice that a rather large white ship has grappled onto your ship and is tugging you backwards.\n" + \
                "You've only got two options:\n\n"
                
        for s in line6:
            sleep(TYPESPEED)
            sys.stdout.write(s)
            sys.stdout.flush()

###
        cont2 = True
        while (cont2):
            a = input("++ Press 1 to attempt to escape by trying to overpower the grapple. \n++ Press 2 to accept that you cannot escape, and submit.\n\n")
            if (a == "1"):
                FIGHTER = True
                line7 = "\nYou turn all power towards your engines, hoping that will give you the acceleration you need to lose the ship.\n"+\
                        "You begin to accelerate away from the white ship.\n" + \
                        "You remember you have a uranium deposit somewhere on the ship and go to search for it.\n\n" + \
                        "You manage to find it sitting under " + saveItem + " and throw it into the fuel gauge.\n" + \
                        "You gleefully fly away at light speed - escaping a potential disaster.\n" + \
                        "Escaping from planet X4561, you get back on track to your planned route to the planet, and rest for the night after putting your ship on auto-pilot.\n\n" + \
                        "CLANK!\n\n"+\
                        "You look in your rear view space mirror, you notice the return of the white ship and its grapple with a deathly grip!\n" + \
                        "You wonder after all this time how they found you, and realize the grapple must have planted a tracker.\n" + \
                        "\nAccepting defeat, you open your air lock and find two people in bright green space suits quickly coming in and, without warning, detaining and bagging you up in merely a few seconds.\n" + \
                        "\nThrough a hole in the bag, you notice an emblem on their helmets. " +\
                        "\nThese aren't military personelle, but instead bandits.  They're probably going to try to loot and scrap your ship, selling all of your valubles. "+\
                        "\nThe men begin carrying you to their ship.\n\n" + \
                        "\nYou notice the thug in the back is beginning to get tired.  You may be able to shake out of his grip.\n\n"

                for s in line7:
                    sleep(TYPESPEED)
                    sys.stdout.write(s)
                    sys.stdout.flush()

####
                cont5 = True
                while (cont5):
                    a = input("++ Press 1 to shake free. \n++ Press 2 to not do anything.\n\n")
                    if (a == "1"):
                        INJURED = True
                        FIGHTER = True
                        line12 = "\nIt turns out the guard in the front ended up dropping you, and you hit your head.  The guard in the back puts you down, and they both kick you once for good measure."+\
                                 "\nYou fall unconscious."+\
                                 "\nThey continue carrying you to their ship."

                        
                        for s in line12:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()

                            
                        cont5 = False
                    elif (a == "2"):

                        line13 = "\nGood choice, you don't want to make them any more mad at you.\n"

                        for s in line13:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()
                                
                        cont5 = False
                    else:
                        print("")
                        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                        print("")
                        cont5 = True
                
                cont2 = False
            elif (a == "2"):

                line8 = "\nYou slow your ship to a halt and open the doors to your spacecraft.  Two rather large men in bright orange spacesuits enter your spacecraft.\n" + \
                        "They introduce themselves as Richard Johnathan and John Richardson - stating that they have come to take all your valuables or they will physically damage your body.\n\n"

                for s in line8:
                    sleep(TYPESPEED)
                    sys.stdout.write(s)
                    sys.stdout.flush()

####
                cont3 = True
                while (cont3):
                    a = input("++ Press 1 to revolt against the men. \n++ Press 2 to agree to their demands.\n\n")
                    if (a == "1"):
                        if(INJURED):
                            line66 = "\nYou are injured from earlier.  You don't have the energy to revolt against the two." #If you are injured, it just prints, it should force you to input 2
                            for s in line66:
                                sleep(TYPESPEED)
                                sys.stdout.write(s)
                                sys.stdout.flush()
                            
                            cont3 = True
                        if(not(INJURED)):
                            PASSIVE = False
                            line9 = "\nYou immediately assume the fighting position of an alpha male gorilla, asserting your dominance over the two space men.\n" + \
                                    "You charge up to the men, but one of them uses a plasma taser against you.\n" + \
                                    "You fall to the floor, unable to move, and Richard Johnathan tells you not to move again.\n\n"

                            for s in line9:
                                sleep(TYPESPEED)
                                sys.stdout.write(s)
                                sys.stdout.flush()

#####
                            cont4 = True
                            while (cont4):
                                a = input("++ Press 1 to attack John Richardson.\n++ Press 2 to lay prone on the floor.")
                                if (a == "1"):
                                    INJURED = True
                                    PASSIVE = False
                                    FIGHTER = True
                                    OUTOFFUEL = True
                                    line10 = "\nCongratulations! You got punched in the face and knocked out. Have you not learned your lesson? \n\n" + \
                                             "The men detain you and begin stuffing you in a bodybag.  They begin taking you into their ship."
                                    
                                    for s in line10:
                                        sleep(TYPESPEED)
                                        sys.stdout.write(s)
                                        sys.stdout.flush()
                                    
                                    cont4 = False
                                elif (a == "2"):
                                    PASSIVE = False
                                    INJURED = False
                                    OUTOFFUEL = True
                                    line11 = "\nThe men steal everything you own, excluding "+saveItem+"."+\
                                             "They both ironically apologize and return to their own ship, only to fly away into the depths of space.\n"+\
                                             "You check your fuel gauge and you barely have enough to make it to the nearest merchantile station.\n\n"
                                    

                                    for s in line11:
                                        sleep(TYPESPEED)
                                        sys.stdout.write(s)
                                        sys.stdout.flush()
                                        
                                    cont4 = False
                                else:
                                    print("")
                                    print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                                    print("")
                                    cont4 = True
                        cont3 = False
                    elif (a == "2"):
                        PASSIVE = True
                        INJURED = False
                        OUTOFFUEL = False
                        line12 = "\nYou agree to their demands, so the men tell you to sit down.\n"+\
                                 "They let you watch as they steal everything off of your ship.\n"+\
                                 "The men thank you for being easy, and offer to fill up your fuel tank.  What kind hearts.\n\n"
                        for s in line12:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()
                        
                        cont3 = False
                    else:
                        print("")
                        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                        print("")
                        cont3 = True               
                cont2 = False
            else:
                print("")
                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                print("")
                cont2 = True
            if(FIGHTER):
                line17 = "\n\nYou wake up in the bag, and through a hole in your bag, you see a guard watching some form of alien entertainment on his holograph box.\n" + \
                         "You hope you still have " + saveItem + ".\n\n"
                
                for s in line17:
                    sleep(TYPESPEED)
                    sys.stdout.write(s)
                    sys.stdout.flush()

######
                cont9 = True
                while (cont9):
                    a = input("++ Press 1 to escape the bag and fight the guard. \n++ Press 2 to wait it out.\n\n")
                    if (a == "1"):
                        if(INJURED):
                            line67 = "\nYou are injured from earlier.  You don't have the energy to fight the guard.\n\n"
                            for s in line67:
                                sleep(TYPESPEED)
                                sys.stdout.write(s)
                                sys.stdout.flush()
                            cont9 = True
                            
                        else:
                            line18 = "\nYou slowly manage to unzip the bag, and creep over to the bandit.\n"
                                     
                            for s in line18:
                                sleep(TYPESPEED)
                                sys.stdout.write(s)
                                sys.stdout.flush()
                            cont9 = False
                            cont12 = True
                            while (cont12):
                                a = input("\n++ Press 1 to quietly escape. \n++ Press 2 to attack the bandit.\n\n")
                                if (a == "2"):
                                    MONSTER = True
                                    line20 = "You ready yourself to fight, and bonk him on the top of the head with a frying pan that was coincidentally lying on the table besides you.\n\n"

                                    for s in line20:
                                        sleep(TYPESPEED)
                                        sys.stdout.write(s)
                                        sys.stdout.flush()
                                    
                                    cont12 = False
                                elif (a == "1"):

                                    line21 = "\nYou decide to sneak away, hoping the bandit won't notice your absence."+\
                                             "You quietly walk about the ship, looking around for an exit.\n\n" + \
                                             '"HEY! What are you doing out here?" - screams one of the bandits in the hall.\n\n' + \
                                             "You run through the hall as the bandit chases you, and you turn around a corner in an attempt to stop them in their tracks.\n" + \
                                             "Right as you hear their footsteps behind you, you...\n"
                                    for s in line21:
                                        sleep(TYPESPEED)
                                        sys.stdout.write(s)
                                        sys.stdout.flush()
                                    cont12 = False
                                    cont18 = True
                                    while (cont18):
                                        a = input("\n++ Press 1 to do an iron fist take down. \n++ Press 2 to do a ceiling demon take down.\n\n")
                                        if (a == "1"):

                                            line93 = "\nYou trip the bandit, planting your fist right where they are supposed to fall, knocking them out."

                                            for s in line93:
                                                sleep(TYPESPEED)
                                                sys.stdout.write(s)
                                                sys.stdout.flush()
                                            cont18 = False
                                            cont9 = False
                                        elif (a == "2"):

                                            line94 = "\nYou crawl up the wall, just like a possessed Spiderman, and do a flip off the ceiling, landing directly on top of the bandit.  He is instantly knocked out."

                                            for s in line94:
                                                sleep(TYPESPEED)
                                                sys.stdout.write(s)
                                                sys.stdout.flush()
                                            cont18 = False
                                            cont9 = False
                                        else:
                                            print("")
                                            print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                                            print("")
                                            cont18 = True
                    elif (a == "2"):

                        line19 = "\nYou wait for something to happen in his show, so you would go unnoticed.\n\n" + \
                                 "Eventually, some argument stirs up in a language you don't understand, and the guard is completely distracted.\n\n" + \
                                 "You sneak away, hoping the bandit doesn't notice that you're gone.\n\n" + \
                                 "You quietly walk about the ship, looking around for an exit.\n\n" + \
                                 '"HEY! What are you doing out here?" - screams one of the bandits in the hall.\n\n' + \
                                 "You run through the hall as the bandit chases you, and you turn around a corner in an attempt to stop them in their tracks.\n" + \
                                 "Right as you hear their footsteps behind you, you...\n"

                        for s in line19:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()

                        cont10 = True
                        while (cont10):
                            a = input("\n++ Press 1 to do an iron fist take down. \n++ Press 2 to do a ceiling demon take down.\n\n")
                            if (a == "1"):

                                line20 = "\nYou trip the bandit, planting your fist right where they are supposed to fall, knocking them out."

                                for s in line20:
                                    sleep(TYPESPEED)
                                    sys.stdout.write(s)
                                    sys.stdout.flush()
                                cont9 = False
                                cont10 = False
                            elif (a == "2"):

                                line21 = "\nYou crawl up the wall, just like a possessed Spiderman, and do a flip off the ceiling, landing directly on top of the bandit.  He is instantly knocked out."

                                for s in line21:
                                    sleep(TYPESPEED)
                                    sys.stdout.write(s)
                                    sys.stdout.flush()
                                cont10 = False
                                cont9 = False
                            else:
                                print("")
                                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                                print("")
                                cont9 = True
                    else:
                        print("")
                        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                        print("")
                        cont10 = True

                        
            if(not(FIGHTER)):
               line87 = "The bandits leave you to be, and you're grateful for that.\n"+\
                        "You look back, and the only thing that the bandits left behind was "+saveItem+"."+\
                        "You turn on your engines, give "+saveItem+" a smile, turn on your FTL drive, and leave the quadrant as fast as you possibly can and continue on your journey to Planet Galactus.\n\n\n"

               for s in line87:
                        sleep(TYPESPEED)
                        sys.stdout.write(s)
                        sys.stdout.flush()

            if(DAMAGEDSHIP):
                SENTIMENTAL = False
                line22 = "You drag him into a closet room nearby, and put on his space suit, and put on one of the space helmets you found in the closet.\n\n" + \
                     "You grab a garbage bag from the closet, and begin filling it with anything you can find.  You manage to get back the majority of your stuff.\n"+\
                     "You eventually find an escape pod, and propel yourself into space, in an attempt to find your spaceship.\n" + \
                     "After you see your ship, and quickly fly directly to it.\n" + \
                     "Your ship is in poor condition after the beating given to it by the asteroids."+\
                     "You need to get your FTL drive repaired."+\
                     "You do not have enough money to repair your ship, so you are forced into selling "+saveItem+"."
                for s in line22:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()
            elif(OUTOFFUEL):
                SENTIMENTAL = False
                line22 = "You drag him into a closet room nearby, and put on his space suit, and put on one of the space helmets you found in the closet.\n\n" + \
                     "You grab a garbage bag from the closet, and begin filling it with anything you can find.  You manage to get back the majority of your stuff.\n"+\
                     "You eventually find an escape pod, and propel yourself into space, in an attempt to find your spaceship.\n" + \
                     "After you see your ship, and quickly fly directly to it.\n" + \
                     "Your ship is nearly out of fuel.  You need to refill your tank at the nearest Merchantile Outpost.\n"+\
                     "You do not have enough money to purchase fuel, so you are forced into selling "+saveItem+"."
                for s in line22:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()
            else:
                line22 = "You drag him into a closet room nearby, and put on his space suit, and put on one of the space helmets you found in the closet.\n\n" + \
                     "You grab a garbage bag from the closet, and begin filling it with anything you can find.  You manage to get back the majority of your stuff.\n"+\
                     "You eventually find an escape pod, and propel yourself into space, in an attempt to find your spaceship.\n" + \
                     "After you see your ship, and quickly fly directly to it.\n" + \
                     "You turn on your engines, give "+saveItem+" a smile, turn on your FTL drive, and leave the quadrant as fast as you possibly can and continue on your journey to Planet Galactus.\n\n\n"
                for s in line22:
                            sleep(TYPESPEED)
                            sys.stdout.write(s)
                            sys.stdout.flush()


            #TY: ESCAPE POD NAVIGATION BACK TO YOUR SHIP
                            
            line101 = ""
            line102 = ""
            line103 = ""
            line104 = ""
            line105 = ""
            line106 = ""
            line107 = ""
            line108 = ""
            line109 = ""
            
            if(not(LONEWOLF) and FIGHTER):
                line101 = "You put up a good fight against the bandits."
            if(SLOWPOKE):
                line102 = "You took your time flying through the asteroid field, and delayed your trip by a few weeks."
            if(INJURED):
                line103 = "You managed to get hurt during your endeavors"
            if(SENTIMENTAL):
                line104 = "You kept "+saveItem+" with you all the way to Planet Galactus."
            if(TOOKABEATING):
                line105 = "You ended up getting beat up by the bandits."
            if(not(LONEWOLF) and PASSIVE):
                line106 = "You tried to be passive towards the bandits."
            if(LONEWOLF):
                line107 = "You were a lone wolf, and flew solo."
            if(LONEWOLF and DAMAGEDSHIP):
                line108 = "You were a poor pilot, and hit a few asteroids."
            if(not(LONEWOLF) and MONSTER):
                line109 = "You bonked the bandit on the head without him knowing."
            if(not(LONEWOLF) and not(FIGHTER)):
                line101 = "You didn't try to fight the bandits."
            if(not(SLOWPOKE)):
                line102 = "You sped through the asteroid field, getting there on time."
            if(not(INJURED)):
                line103 = "You stayed safe on the way to Planet Galactus"
            if(not(SENTIMENTAL)):
                line104 = "You had to sell "+saveItem+" to make it to Planet Galactus."
            if(not(TOOKABEATING)):
                line105 = "You didn't get hurt by the bandits."
            if(not(LONEWOLF) and not(PASSIVE)):
                line106 = "You were aggressive towards the bandits."
            if(not(LONEWOLF)):
                line107 = "You're sociable, and flew with other ships."
            if(LONEWOLF and (not(DAMAGEDSHIP))):
                line108 = "You were a good pilot, and avoided all of the asteroids."
            if(not(LONEWOLF) and not(MONSTER)):
                line109 = "You did not hurt the bandit when you could have."
                
            line1000 = "Through your adventures:\n\n"
            if(not(line101 == "")):
                line1000 += line101 + "\n\n"
            if(not(line102 == "")):
                line1000 += line102 + "\n\n"
            if(not(line103 == "")):
                line1000 += line103 + "\n\n"
            if(not(line104 == "")):
                line1000 += line104 + "\n\n"
            if(not(line105 == "")):
                line1000 += line105 + "\n\n"
            if(not(line106 == "")):
                line1000 += line106 + "\n\n"
            if(not(line107 == "")):
                line1000 += line107 + "\n\n"
            if(not(line108 == "")):
                line1000 += line108 + "\n\n"
            if(not(line109 == "")):
                line1000 += line109 + "\n\n"
                
            for s in line1000:
                sleep(TYPESPEED)
                sys.stdout.write(s)
                sys.stdout.flush()
            creds = "Planet Galactus created by Tyler Gutowski and Mishka Liamkin.\n"+\
                    "Created for the 2019 Codecraft competition.\n"+\
                    "Tyler Gutowski Github: https://github.com/tygutowski\n\n\n"+\
                    "Thank you for playing.  We hope you enjoyed."
            
            for s in creds:
                sleep(TYPESPEED)
                sys.stdout.write(s)
                sys.stdout.flush()
            
        cont = False
        cont2 = False
        
    else:
        print("")
        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
        print("")
        cont = True
