#Credits: Michael Liamkin
	 Tyler Gutowski

#Date of Program Creation: February 14, 2019

#Contact: mliamkin56@gmail.com
	  tygutowski@gmail.com

#Name: THE ESCAPE TO PLANET GALACTUS

--------------------------------------------------------------------------------------------------------------------------------------------------

#GENERAL USAGE:

+ MADE FOR USAGE WITH PYTHON 3.7.2

+ Program is a create your own adventure with multiple storylines.

+ Player is introduced to the story, and must choose option 1 or 2 when prompted at a certain point

+ If a key is hit while words are being automatically displayed, the rate at which they display will increase

INSTALLATION:

+ Python must be installed at https://www.python.org/

+ Check off boxes to install pip package manager and to install python test suite

+ To install the different modules, read below

--------------------------------------------------------------------------------------------------------------------------------------------------

---> Modules: <---

# pygame

pygame is a module that deals with making functioning games in python

## Installation

To install pygame, your version of python should be installed with the package manager pip - which should be selected when downloading python

Into Command prompt type:

pip install pygame

## Usage

import pygame

____________________________________________________________________________________________________________________________________________________

# time

time is a module that is preinstalled onto most version of python that deals with setting time in a program, and setting delays


## Installation

The time module is preinstalled during the installation phase of python (if python test suite is checked during installation)


## Usage

import time
from time import sleep

sleep(0.02)
sleep(1)


____________________________________________________________________________________________________________________________________________________


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

____________________________________________________________________________________________________________________________________________________


# random

random is a module that is used to generate random numbers


## Installation

The random module is preinstalled during the installation phase of python (if python test suite is checked during installation)


## Usage

import random

NAME = GERMANFIRSTNAMES[random.randint(0,len(GERMANFIRSTNAMES)-1)] + " " + GERMANLASTNAMES[random.randint(0,len(GERMANLASTNAMES)-1)]

print(LISTRESPONSES[random.randint(0,len(LISTRESPONSES)-1)])
NAME = GERMANFIRSTNAMES[random.randint(0,len(GERMANFIRSTNAMES)-1)] + " " + GERMANLASTNAMES[random.randint(0,len(GERMANLASTNAMES)-1)]