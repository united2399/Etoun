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

sand = Operator("Sand", "DPS", 300, 300)

operators = [sand]
player_operators = [sand]
squad_1 = [sand]
active_squad = 1

# Enemies

slug = Enemy("Slug", 600, 0, 5)

current_enemies = []
active_enemies = []

p_lives = 5

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
        current_enemies = [Enemy("Slug", 600, 0) for _ in range(3)]
        active_enemies = [Enemy("Slug", 600, 0) for _ in range(3)]

        while True:
          # Set operator count and downed operator count to 0
          operator_count = 0
          downed_operators = 0
          # Reset some stuff
          operatorhasattacked = False
          # check which squad is being used
          if active_squad == 1:
            # loop over all the operators in the squad
            for i in squad_1:
              # Increase the operator count by 1
              operator_count += 1
              if i.health < 0.1: # if the operator is downed
                downed_operators += 1 # increase the downed operator count by 1
          # if all operators are downed, end the mission.
          if downed_operators == operator_count or p_lives < 0:
            print ("mission: failure.")
            input("")
            break

          # same thing here as above but for enemies
          enemy_count = 0
          downed_enemies = 0
          for i in current_enemies:
            enemy_count += 1
            if i.health < 0.1:
              downed_enemies += 1
          if enemy_count == downed_enemies and p_lives > 0:
            print ("mission: success")
            print (f"lives remaining: {p_lives}")
            input("")
            break
            
          for i in active_enemies:
            if i.health > 0.1:
              i.turnstopass -= 1
              if i.turnstopass < 0:
                p_lives -= 1
                i.health -= 999999 # kill the enemy once it passes
                print (f"{i.name} passed your defense. -1 life.")
                # checking if the enemies passed le defense
                if downed_operators == operator_count or p_lives < 0:
                  print ("mission: failure.")
                  input("")
                  break
            
          print (len(current_enemies))
          print (len(active_enemies))
          if len(active_enemies) < 1 and len(current_enemies) > 0:
            e = random.choice(current_enemies)
            active_enemies.append(e)
            current_enemies.remove(e)
            

          if active_squad == "1":
            for operator in squad_1:
              operatorhasattacked = False
            for operator in squad_1:
              # if enemy will pass in 1 turn
              for enemy in active_enemies:
                if enemy.turnstopass == 0:
                  operatorhasattacked = True
                  enemy.health -= operator.attack
                  break
              # if enemy will pass in 2 turns
              if operatorhasattacked == False:
                for enemy in active_enemies:
                  if enemy.turnstopass == 1:
                    operatorhasattacked = True
                    enemy.health -= operator.attack
                    break 
              # if enemy will pass in 3 turns
              if operatorhasattacked == False:
                for enemy in active_enemies:
                  if enemy.turnstopass == 2:
                    operatorhasattacked = True
                    enemy.health -= operator.attack
                    break 
              # if enemy will pass in 4 turns
              if operatorhasattacked == False:
                for enemy in active_enemies:
                  if enemy.turnstopass == 3:
                    operatorhasattacked = True
                    enemy.health -= operator.attack
                    break 
              # if enemy will pass in 5 turns
              if operatorhasattacked == False:
                for enemy in active_enemies:
                  if enemy.turnstopass == 43:
                    operatorhasattacked = True
                    enemy.health -= operator.attack
                    break 

              if operatorhasattacked == True:
                print (f"{operator.name} has attacked an enemy dealing {operator.attack} damage!")
              operatorhasattacked = False # Reset it for the next operator
              
        
      

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
      for operator in squad_1:
        print (operator)

  # Operators
  while menu == "operators":
    clear()
    time.sleep (0.05)
    print ("(x) Main menu")
    for operator in player_operators:
      print(operator)
    e = input("")
    if e == "x":
      menu = "main"
