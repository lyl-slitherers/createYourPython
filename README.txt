#Credits: Michael Liamkin
	  Tyler Gutowski

#Date of Program Creation: February 14, 2019

#Contact: mliamkin56@gmail.com
	  tygutowski@gmail.com

#Name: PLANET GALACTUS

----------------------------------------------------------------------------------------------------------------------------------------

#GENERAL USAGE:

+ MADE FOR USAGE WITH PYTHON 3.7.2

+ Program is a create your own adventure with multiple storylines.

+ Player is introduced to the story, and must choose option 1 or 2 when prompted at a certain point

+ For best performance, please full screen the python shell when running the program (Title would shrink otherwise)

+ For changing settings:

  ++ Press 1 to change the text delay
  ++ Press 2 to change the text speed
  ++ Press 3 to continue

INSTALLATION:

+ Python must be installed at https://www.python.org/

+ Check off boxes to install pip package manager and to install python test suite

+ To install the different modules, read below

----------------------------------------------------------------------------------------------------------------------------------------

---> Modules: <---

# pygame

pygame is a module that deals with making functioning games in python

## Installation

To install pygame, your version of python should be installed with the package manager pip - which should be selected when downloading python

Into Command prompt type:

pip install pygame

## Usage

import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))

white   = (255, 255, 255)
black   = (000, 000, 000)
red     = (255, 000, 000)

clock = pygame.time.Clock()

circle = pygame.Surface((30, 30,))

________________________________________________________________________________________________________________________________________

# time

time is a module that is preinstalled onto most version of python that deals with setting time in a program, and setting delays


## Installation

The time module is preinstalled during the installation phase of python (if python test suite is checked during installation)


## Usage

import time
from time import sleep

sleep(0.02)
sleep(1)


________________________________________________________________________________________________________________________________________


# sys

sys is module that is used when variables have a lot of interaction with the user


## Installation

The time module is preinstalled during the installation phase of python (if python test suite is checked during installation)


## Usage

import sys

for s in line1:
    
	sleep(TYPESPEED)
    
	sys.stdout.write(s)
    
	sys.stdout.flush()

________________________________________________________________________________________________________________________________________


# random

random is a module that is used to generate random numbers


## Installation

The random module is preinstalled during the installation phase of python (if python test suite is checked during installation)


## Usage

import random

NAME = GERMANFIRSTNAMES[random.randint(0,len(GERMANFIRSTNAMES)-1)] + " " + GERMANLASTNAMES[random.randint(0,len(GERMANLASTNAMES)-1)]

print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
NAME = GERMANFIRSTNAMES[random.randint(0,len(GERMANFIRSTNAMES)-1)] + " " + GERMANLASTNAMES[random.randint(0,len(GERMANLASTNAMES)-1)]
