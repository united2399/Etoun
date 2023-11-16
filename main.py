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
# colorama.init() # for some reason colorama is currently fucked


# Operators

sand = Operator("Sand", 300, 300)

operators = [sand]
squad_1 = [sand]
active_squad = 1

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
      
    while e == "1":
      clear()
      time.sleep (0.05)
      print ("(x) Back")
      print ("(1) Stage 1")
      e = input("")
      if e == "1":
        while True:
          # Set operator count and downed operator count to 0
          operator_count = 0
          downed_operators = 0
          # check which squad is being used
          if active_squad == 1:
            # loop over all the operators in the squad
            for i in squad_1:
              # Increase the operator count by 1
              operator_count += 1
              if i.health < 0.1: # if the operator is downed
                downed_operators += 1 # increase the downed operator count by 1
          # if all operators are downed, end the mission.
          if downed_operators == operator_count:
            print ("mission: failure.")
            break
        
      

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
    if e == "1":
      print (squad_1)

  # Operators
  while menu == "operators":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    print (player_operators)
    e = input("")
    if e == "x":
      menu = "main"



