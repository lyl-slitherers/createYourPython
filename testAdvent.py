import random

LISTRESPONSES = ["This answer does not exist, you need to try again.", "Invalid answer. Try again.",\
                 "Your typing skills are not very good, you need to try again.",\
                 "Have you ever used a computer keyboard before? You need to try again",\
                 "Your answer does not make sense, try again",\
                 "Do you know what a number is? Type your answer again being mindful about the number keys on the top of your keyboard",\
                 "What kind of vision do you have? Do you not see the keyboard? Try again."]
LIST = ["your pet Venus Flytrap","your baby teeth","a plastic tupperware container full of weiner schnitzels",\
        "your Christmas tree","your lucky glow-in-the-dark snorkle"]

print("December 26th, 2240")
print("")
print("You are Wolfgang Steinway, a 50-year old German man, making your way across the galaxy in a spaceship at the speed of light towards Planet Galactus - a life-bearing planet about half a light year away with no established human civilization.")
print("")
print("2 Hours before,")
print("Buzzzz Buzzzz - *BREAKING NEWS* SCIENTISTS PREDICT AN 80-MILE WIDE ASTEROID WILL HIT PLANET EARTH IN 2 HOURS TIME! PREPARE . . . ")
print("")
print("Waking up completely bamboozled, you get on your Samsung Galaxy S229 to confirm the shocking news you just heard.")
print("")
print("Unfortunately, you find out the inevitable - all life on Earth will be wiped out in 2 hours.")
print("You quickly run and fill your spaceship in your garage with your valuables, your Food Creator™, and you have space for only one more item.")

randomItem1 = LIST[random.randint(0,2)]
randomItem2 = LIST[random.randint(2,4)]

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

print("")
print("You start your engine and fly up through the atmosphere, recognizing the asteroid in the distance.")
print("")
print("Noticing the crowd of spaceships leaving alongside of you, do you decide to follow them or fly alone?")
print("")

cont = True
while (cont):
    a = input("++ Press 1 to fly along with the others. \n++ Press 2 to fly alone.")
    if (a == "1"):
        saveItem = randomItem1

        print("")
        print("You follow a trio of spaceships, and put your ship on autopilot along your planned route to Planet Galactus")
        print("You decide to introduce yourself to the others.")
        print("The other ships tell you that there has been word of space robbers between planets X3245 and X4561.")
        print("")
        print("You make note of the warning, and update your route around the location of the robbers.")
        print("Returning from a trip to your Food Creator™ to get a cup of tea, you trip and spill tea all over your space radio.")
        print("Your begin to hear 'BEEP BOOP BEEP ...' and static noise from your radio. Unconcerned, you are sure that the radio was warning about the space robbers.")
        print("You brush your teeth, admire " + saveItem + ", and go to sleep.")
        
        cont = False
    elif (a == "2"):
        saveItem = randomItem2

        print("")
        print("You look at your SPS (Space Positioning System) and follow a planned out route to Planet Galactus estimated to take about 6 months.")
        print("")
        print("BEEP BOOP BEEP BOOP *TO ALL THOSE LEAVING EARTH AND HEADING TOWARDS PLANET GALACTUS* BEWARE OF AN ASTEROID BELT IN QUADRANT 271. YOU MUST URGENTLY PLAN A ROUTE AROUND THE BELT!")
        print("")
        print("You update your route on your SPS, thankful for the warning on your space radio.")
        print("You put your ship on auto-pilot, lay back, and fall asleep while admiring " + saveItem + ".")
        
        cont = False
    else:
        print("")
        print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
        print("")
        cont = True
