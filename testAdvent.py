#Michael Liamkin, Tyler Gutowski
#2/14/2019
#Space adventure

import random
import time
import sys
from time import sleep
from os import system, name 

#CODE: https://www.geeksforgeeks.org/clear-screen-python/

def clear(): 
    if name == 'nt': 
        _ = system('cls')

LISTRESPONSES = ["This answer does not exist, you need to try again.", "Invalid answer. Try again.",\
                 "Your typing skills are not very good, you need to try again.",\
                 "Have you ever used a computer keyboard before? You need to try again",\
                 "Your answer does not make sense, try again",\
                 "Do you know what a number is? Type your answer again being mindful about the number keys on the top of your keyboard",\
                 "What kind of vision do you have? Do you not see the keyboard? Try again."]
LIST = ["your pet Venus Flytrap","your baby teeth","your plastic tupperware container full of weiner schnitzels",\
        "your Christmas tree","your lucky glow-in-the-dark snorkle", "your favorite purple pen", "your red superhero cape"]

line1 = "December 26th, 2240\n\n" + \
        "You are Wolfgang Steinway, a 50-year old German man, making your way across the galaxy in a spaceship at the speed of light towards Planet Galactus - a life-bearing planet about half a light year away with no established human civilization.\n\n"
line2 = "2 Hours before,\n"

alert1 = "Buzzzz Buzzzz - *BREAKING NEWS* SCIENTISTS PREDICT AN 80-MILE WIDE ASTEROID WILL HIT PLANET EARTH IN 2 HOURS TIME! PREPARE . . . \n\n"
                
line3 = "Waking up completely bamboozled, you get on your Samsung Galaxy S229 to confirm the shocking news you just heard.\n" + \
        "Unfortunately, you find out the inevitable - all life on Earth will be wiped out in 2 hours." + \
        " You quickly run and fill your spaceship in your garage with your valuables, your Food Creator™, and you have space for only one more item.\n\n"

#CODE: https://stackoverflow.com/questions/20302331/typing-effect-in-python

for s in line1:
    sleep(0.02)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(0.5)

for s in line2:
    sleep(0.02)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(0.5)

for s in alert1:
    sleep(0.02)
    sys.stdout.write(s)
    sys.stdout.flush()

sleep(0.5)

for s in line3:
    sleep(0.02)
    sys.stdout.write(s)
    sys.stdout.flush()

randomItem1 = LIST[random.randint(0,3)]
randomItem2 = LIST[random.randint(4,6)]

print("You can either bring " + randomItem1 + " or " + randomItem2 + ".")
print("")

cont = True
while (cont):
    a = input("++ Press 1 to bring " + randomItem1 + ". \n++ Press 2 to bring " + randomItem2 + ".")
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

line4 = "\nYou start your engine and fly up through the atmosphere, recognizing the asteroid in the distance.\n\n" + \
        "Noticing the crowd of spaceships leaving alongside of you, do you decide to follow them or fly alone?\n\n"

for s in line4:
    sleep(0.02)
    sys.stdout.write(s)
    sys.stdout.flush()

cont = True
while (cont):
    a = input("++ Press 1 to fly along with the others. \n++ Press 2 to fly alone.")
    if (a == "1"):

        line5 = "\nYou follow a trio of spaceships, and put your ship on autopilot along your planned route to Planet Galactus\n"  + \
                "You decide to introduce yourself to the others.\n" + \
                "The other ships tell you that there has been word of space robbers between planets X3245 and X4561.\n\n" + \
                "You make note of the warning, and update your route around the location of the robbers.\n" + \
                "Returning from a trip to your Food Creator™ to get a cup of tea, you trip and spill tea all over your space radio.\n" + \
                "Your begin to hear 'BEEP BOOP BEEP ...' and static noise from your radio. Unconcerned, you are sure that the radio was warning about the space robbers.\n" + \
                "You brush your teeth, admire " + saveItem + ", and go to sleep.\n\n"

        for s in line5:
            sleep(0.02)
            sys.stdout.write(s)
            sys.stdout.flush()

        sleep(1)

        line15 = "The next morning, you notice the ships that you were following are completely out of sight.\n" + \
                 "Confused, you check your radar to locate the other ships, and you see they went around quadrant 271.\n" + \
                 "You think they might have made a mistake, and decide to meet up with them by going through quadrant 271.\n\n" + \
                 "Approaching the region, you start hearing little ticks on your ship - like small objects hitting it.\n"

        for s in line15:
            sleep(0.02)
            sys.stdout.write(s)
            sys.stdout.flush()

        cont8 = True
        
        while (cont8):
            a = input("\n++ Press 1 to keep going through the region full speed. \n++ Press 2 to slow down.")
            if (a == "1"):

                line16 = "\nThe ticks on your ship keep getting louder and louder, until you see full blown asteroids in front of you.\n" + \
                         "You are forced to take manual control of the ship and need to steer away from the asteroids."

                for s in line16:
                    sleep(0.02)
                    sys.stdout.write(s)
                    sys.stdout.flush()

                #TY: Add a program here to control ship around asteroids here - Make the asteroids really fast here (because user chose to keep going full speed through the belt)
                
                cont8 = False
            elif (a == "2"):

                line16 = "\nThe ticks on your ship keep getting louder and louder, until you see full blown asteroids in front of you.\n" + \
                         "You are forced to take manual control of the ship and need to steer away from the asteroids."

                for s in line16:
                    sleep(0.02)
                    sys.stdout.write(s)
                    sys.stdout.flush()

                #TY: Add a program here to control ship around asteroids - make asteroids a slower speed (because user chose to slow down)
                
                cont8 = False
            else:
                print("")
                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                print("")
                cont8 = True
            
        cont = False

        
        
    elif (a == "2"):

        line6 = "\nYou look at your SPS (Space Positioning System) and follow a planned out route to Planet Galactus estimated to take about 6 months.\n\n" + \
                "BEEP BOOP BEEP BOOP *TO ALL THOSE LEAVING EARTH AND HEADING TOWARDS PLANET GALACTUS* BEWARE OF AN ASTEROID BELT IN QUADRANT 271. YOU MUST URGENTLY PLAN A ROUTE AROUND THE BELT!\n\n" + \
                "You update your route on your SPS, thankful for the warning on your space radio.\n" + \
                "You put your ship on auto-pilot, lay back, and fall asleep while admiring " + saveItem + ".\n\n" + \
                "The next day,\n" + \
                "As you approach between planets X3245 and X4561, you see a speck of white behind growing larger and larger, until\n\n" + \
                "WHAM!\n\n" + \
                "You hear a loud clang and feel your ship moving back.\n" + \
                "Confused, you look out your rear view space mirror, and notice that a white ship has grappled onto your ship and is tugging you back.\n" + \
                "You've only got two options:\n\n"
                
        for s in line6:
            sleep(0.02)
            sys.stdout.write(s)
            sys.stdout.flush()

        cont2 = True
        while (cont2):
            a = input("++ Press 1 to attempt to escape by trying to overpower the grapple. \n++ Press 2 to accept that you cannot escape, and don't even try to.")
            if (a == "1"):

                line7 = "\nYou step on the gas, slightly moving away from the white ship.\n" + \
                        "You remember you have a nitro boost, so you activate it and sure enough, you escape the mighty hold of the grapple.\n\n" + \
                        "You gleefuly fly away at light speed - escaping a potential disaster.\n" + \
                        "Escaping from planet X4561, you get back on track to your planned route to the planet, and rest for the night after putting your ship on auto-pilot.\n\n" + \
                        "CLANG!!\n\n 'Another loud clang!?' you think to yourself, and in the rear view space mirror, you notice the return of the white ship and its grapple with a deathly grip!\n" + \
                        "You wonder after all this time how they found you, but you realize the grapple must have planted a tracker.\n" + \
                        "\nAccepting defeat, you open your air lock and find two people in Gucci space suits quickly crawling in and, without warning, detaining and bagging you up in mere seconds using insect-like Jiu Jitsu moves.\n" + \
                        "\nThrough a peep hole, you notice their lucious frosted tip hair and white polarized glasses with flames inside their helmets. " +\
                        "Your hearing being muffled, due to you being in a bag, you hear the murmur of the Gucci cosmonauts confidently stating that you shouldn't have tried to run from them, overhearing one of them being called Richardison and one of them Donathan.\n\n" + \
                        "\nThe men accidentally drop you, leaving one of your arms exposed.\n\n"

                for s in line7:
                    sleep(0.02)
                    sys.stdout.write(s)
                    sys.stdout.flush()

                cont5 = True
                while (cont5):
                    a = input("++ Press 1 to take a shot at one of the men. \n++ Press 2 to not do anything.")
                    if (a == "1"):
                        line12 = "\nNice job, man! The Gucci space men quickly finagle your wrist mid-jab, and direct it straight at your face - therefore knocking yourself out!\n" + \
                                 "They take you through your airlock into their ship."

                        for s in line12:
                            sleep(0.02)
                            sys.stdout.write(s)
                            sys.stdout.flush()
                                
                        cont5 = False
                    elif (a == "2"):

                        line13 = "\nGood choice, you don't want to make them any more mad at you.\n" + \
                                 "They take you through your airlock into their ship."

                        for s in line13:
                            sleep(0.02)
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

                line8 = "\nTwo people in Gucci space outfits exit the white spacecraft, and you open your airlock to them so they can enter yours.\n" + \
                        "As they stroll in, they remove their helmets to reveal two men with beautiful frosted-tip hair and white polarized glasses with flames on the side.\n" + \
                        "They introduce themselves as Richardison Michaels and Donathan Jones - stating that they have come to take all your valuables or else they will physically damage your body.\n\n"

                for s in line8:
                    sleep(0.02)
                    sys.stdout.write(s)
                    sys.stdout.flush()

                cont3 = True
                while (cont3):
                    a = input("++ Press 1 to revolt against the men. \n++ Press 2 to agree to their demands.")
                    if (a == "1"):

                        line9 = "\nYou immediately assume the fighting position of an alpha male gorrilla, asserting your dominance over the Gucci space men.\n" + \
                                "You charge up to the men, but SURPRISE! They know Jiu Jitsu!\n" + \
                                "They take you down with only their nose in just a split second, not giving you a chance to react.\n" + \
                                "They put you in a bag, but as one of them looks away, you see a chance!\n\n"

                        for s in line9:
                            sleep(0.02)
                            sys.stdout.write(s)
                            sys.stdout.flush()

                        cont4 = True
                        while (cont4):
                            a = input("++ Press 1 to jab one of the men in the chest. \n++ Press 2 to allow them to put you in the bag.")
                            if (a == "1"):

                                line10 = "\nCongratulations! You got punched in the face and knocked out. Have you not learned your lesson? \n\n" + \
                                         "The men continue stuffing you in the bag and finally zip you up, knock you out, and take you into their ship."

                                for s in line10:
                                    sleep(0.02)
                                    sys.stdout.write(s)
                                    sys.stdout.flush()
                                
                                cont4 = False
                            elif (a == "2"):

                                line11 = "\nThe men stuff you in the bag and finally zip you up, knock you out, and take you into their ship."

                                for s in line11:
                                    sleep(0.02)
                                    sys.stdout.write(s)
                                    sys.stdout.flush()
                                    
                                cont4 = False
                            else:
                                print("")
                                print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                                print("")
                                cont = True
                    
                            cont3 = False
                    elif (a == "2"):

                        line12 = "\nYou agree to their demands, so the men bundle you up, knock you out, and zip you into their bags, taking you into their ship."

                        for s in line12:
                            sleep(0.02)
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

            line17 = "\n\nYou wake up in the bag, seeing a guard turned around watching a space soccer match through your peephole.\n" + \
                     "In your pocket, you notice you still have " + saveItem + ".\n\n"
            
            for s in line17:
                sleep(0.02)
                sys.stdout.write(s)
                sys.stdout.flush()

            cont9 = True
            while (cont9):
                a = input("++ Press 1 to try to get out of your bag and knock the guard out now. \n++ Press 2 to be more stealthy and wait for a chance.")
                if (a == "1"):

                    line18 = "\nRight as you get out of the bag, the guard does an epic 360 degree kick right to your face, knocking you out again.\n\n"

                    for s in line18:
                        sleep(0.02)
                        sys.stdout.write(s)
                        sys.stdout.flush()

                    
                    cont9 = True
                elif (a == "2"):

                    line19 = "\nYou wait for a goal to occur on the space soccer game to get out of the bag, so the noise you make would go unnoticed.\n\n" + \
                             "GOOOOOOOOOAAAAAAAAALLLLLLLLL!!!\n\n" + \
                             "The teleprompter screams, and you finally get out of the bag, then do a 360 degree power hit right on to the guard's head with " + saveItem + ", knocking them out.\n\n" + \
                             "You quietly walk about the ship, looking around for an exit to your ship.\n\n" + \
                             "HEY! What are you doing here? - screams one of the bandits in the hall.\n\n" + \
                             "You run through the hall as the bandit chases you, and you turn around a corner to stop them in their tracks.\n" + \
                             "Right as you hear their footsteps near you, you ...\n"

                    for s in line19:
                        sleep(0.02)
                        sys.stdout.write(s)
                        sys.stdout.flush()

                    cont10 = True
                    while (cont10):
                        a = input("\n++ Press 1 to do an iron fist take down. \n++ Press 2 to do a ceiling demon take down.")
                        if (a == "1"):

                            line20 = "\nYou trip the bandit, planting your fist right where they are supposed to fall, knocking them out."

                            for s in line20:
                                sleep(0.02)
                                sys.stdout.write(s)
                                sys.stdout.flush()
                            
                            cont10 = False
                        elif (a == "2"):

                            line21 = "\nYou crawl up the wall, just like Spiderman, and do a flip off the ceiling, landing right onto the bandit. He gets knocked out."

                            for s in line21:
                                sleep(0.02)
                                sys.stdout.write(s)
                                sys.stdout.flush()

                            
                            cont10 = False
                        else:
                            print("")
                            print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                            print("")
                            cont10 = True


                             
                    line22 = "You drag them into a closet room nearby, and put on their space suit, as well as put on a space helmet you found in the closet.\n\n" + \
                             "You find an exit, and immediately leave through the airlock, propelling yourself in space using rocket propelled engines on the suit.\n" + \
                             "You see your ship, and quickly fly right to it.\n" + \
                             "You turn on your engines, and leave the quadrant as rapidly as you possibly could  and continue your journey to Planet Galactus."
                    
                    for s in line22:
                                sleep(0.02)
                                sys.stdout.write(s)
                                sys.stdout.flush()

                    #TY: Put a pygame of the flying thing - there is no asteroid belt here since you are escaping the bandits - just make people take the ship straight to planet galactus

                    
                    cont9 = False
                else:
                    print("")
                    print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
                    print("")
                    cont9 = True
            
        
        cont = False
        
    else:
        print("")
        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
        print("")
        cont = True
