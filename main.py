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

current_enemies = []
active_enemies = []

# Define a dictionary for stage 1 deployment spots and their strategic values
stage_1_deploy_spots = {
    "Spot_A": {"Location": 1, "View_range": [1, 2, 3, 4, 5], "% of attack": "40"},
    "Spot_B": {"Location": 2, "View_range": [2, 3, 4], "% of attack": "15"},
    "Spot_C": {"Location": 3, "View_range": [1, 2, 3, 4, 5, 6], "% of attack": "50"},
    "Spot_D": {"Location": 4, "View_range": [2, 3, 4, 5, 6], "% of attack": "40"},
    "Spot_E": {"Location": 5, "View_range": [3, 4, 5, 7], "% of attack": "30"},
}

# Access and print information about each deployment spot
for spot, info in stage_1_deploy_spots.items():
    print(f"{spot}")
    print(f"Location: ({info['Location']})")
    print(f"View range: ({info['View_range']})")
    print(f"% of attack: {info['% of attack']}")
    print("\n")

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
      
    # Story mission set 1
    while e == "1":
      clear()
      time.sleep (0.05)
      print ("(x) Back")
      print ("(1) Stage 1")
      e = input("")
      
      # Stage 1
      if e == "1":
        # Access and print information about each deployment spot
        for spot, info in stage_1_deploy_spots.items():
            print(f"{spot}")
            print(f"Location: ({info['Location']})")
            print(f"View range: ({info['View_range']})")
            print(f"% of attack: {info['% of attack']}")
            print("\n")

        input("You will now get to choose on which spot you want your squad operators to be on. \n Press Enter to continue.")
        for operator in squad_1:
          for spot in stage_1_deploy_spots.items():
            input(f"Place {operator.name} on {spot}?")
          
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

          # same thing here as above but for enemies
          enemy_count = 0
          downed_enemies = 0
          for i in current_enemies:
            enemy_count += 1
            if i.health < 0.1:
              downed_enemies += 1
          if enemy_count == downed_enemies:
            print ("mission: success")
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



