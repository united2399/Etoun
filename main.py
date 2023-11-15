# Imports
import time
import random
import math
# import colorama # for some reason colorama is currently fucked
import os


# From imports
# from colorama import Fore, Back, Style # for some reason colorama is currently fucked
from Classes import Operator, Enemy
from Utils import clear



# Setting up the modules
colorama.init()


# Operators

sand = Operator("Sand", 300, 300)

operators = [sand]

# Enemies

slug = Enemy("Slug", 600, 0)

menu = "main"

while True:
  # Clearing the screen. stopping infinite printing bullshit
  clear()
  time.sleep (0.05)

  # Main menu
  while menu == "main":
    clear()
    time.sleep (0.05)
    print ("(1) Campaign")
    print ("(2) Recruitment")
    print ("(3) Squads")
    print ("(4) Operators")
    e = input("")
    if e == "1":
      menu = "campaign"
    elif e == "2":
      menu = "recruitment"
    elif e == "3":
      menu = "squads"
    elif e == "4":
      menu = "operators"

  # Campaign
  while menu == "campaign":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    print ("(1) Plot or something 1")
    e = input("")
    if e == "x":
      menu = "main"

  # Recruitment
  while menu == "recruitment":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    print ("(1) Recruit")
    e = input("")
    if e == "x":
      menu = "main"

  # Squads
  while menu == "squads":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    print ("(1) Squad 1")
    e = input("")
    if e == "x":
      menu = "main"

  # Operators
  while menu == "operators":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    print (player_operators)
    e = input("")
    if e == "x":
      menu = "main"



