# Imports
import time
import random
import math
import os


# From imports
from Classes import Operator, Enemy
from Utils import clear



# Setting up the modules
# colorama.init() # for some reason colorama is currently fucked


# Operators

op_1 = Operator("Adnachiel", "DPS", 0, 300, 300)
op_2 = Operator("Ranger", "DPS", 0, 300, 300)

operators = [op_1, op_2]
player_operators = [op_1, op_2]
squad_1 = [op_1, op_2]
squad_2 = []
squad_3 = []
squad_4 = []
active_squad = 1

# Enemies

slug = Enemy("Slug", 600, 0, 5)

current_enemies = []
active_enemies = []

p_lives = 5
breakloop = False

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
    print ("(1) Campaign 1")
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
        
        # vvv handles operator placement 
        
        print ("enemy count: 6")
        if active_squad == 1:
          attemptsForPos = 0
          for i in squad_1:
            attemptsForPos = 0
            breakloop = False
            while True:
              if breakloop == True:
                break
              attemptsForPos += 1
              clear()
              pos = 0
              if attemptsForPos == 0:
                pos = random.randint(2, 6)
              elif attemptsForPos == 1:
                pos = random.randint(3, 5)
              elif attemptsForPos == 2:
                pos = random.randint(3, 6)
              expected_pos = random.randint((pos - 1), (pos + 1))
              print ("Intel says that this position - position ", attemptsForPos, " - should give operator ", i.name, "a vision of ", expected_pos)
              print ("")
              print ("This information may be slightly inaccurate. Proceed with operator placement?")
              if attemptsForPos > 2:
                print ("(This is your last placement re-roll for this operator.)")
              while True:
                proceed = input("proceed? (y/n)")
                clear()
                if proceed == "y":
                  i.vision = pos
                  breakloop = True
                  break
                else:
                  if attemptsForPos < 3:
                    break
                if attemptsForPos > 2:
                  pos = random.randint(3, 6)
                  expected_pos = pos
                  print ("Intel says that this position ( position ", attemptsForPos, ") should give operator ", i.name, "a vision of ", expected_pos)
                  print ("")
                  print (f"Due to your hesistancy in deciding. we have automatically deployed {i.name} to position {attemptsForPos}, giving them an expected vision of {expected_pos}")
                  print ("")
                  breakloop = True
                  break
                else:
                  break

        # ^^^ handles operator placement
        print ("That's it for the operator placement orders. Prepare for battle.")
        input("Press Enter to continue)")
        
        # Less nerdy stuff below 
                  
            
        current_enemies = [Enemy("Slug", 600, 0, 5) for _ in range(3)]
        active_enemies = [Enemy("Slug", 600, 0, 5) for _ in range(3)]

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
          for i in current_enemies:
            enemy_count += 1
            if i.health < 0.1:
              active_enemies.remove(i)
          if enemy_count == 0 and p_lives > 0:
            print ("")
            print ("[^^ COMBAT LOG ^^]")
            print ("")
            print ("mission: success")
            print (f"lives remaining: {p_lives}")
            input("")
            break
            
          for i in active_enemies:
            if i.health < 0.1:
              active_enemies.remove(i)
            if i.health > 0.1:
              i.turnstopass -= 1
              if i.turnstopass < 0:
                p_lives -= 1
                i.health -= 999999 # kill the enemy once it passes
                print (f"{i.name} passed your defense. -1 life.")
                # checking if the enemies passed le defense
                if downed_operators == operator_count or p_lives < 0:
                  print ("")
                  print ("^^^^ Combat log (for nerds and occasionally debugging) ^^^^")
                  print ("mission: failure.")
                  input("")
                  break
            
          print (f"number of inactive enemies: {len(current_enemies)}")
          print (f"number of active enemies: {len(active_enemies)}")
          for i in active_enemies:
            print (f"{i.name} hp: {i.health}")
          if len(active_enemies) < 1 and len(current_enemies) > 0:
            e = random.choice(current_enemies)
            active_enemies.append(e)
            current_enemies.remove(e)
            

          if active_squad == 1:
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
                  if enemy.turnstopass == 4:
                    operatorhasattacked = True
                    enemy.health -= operator.attack
                    break 
              # if enemy will pass in 5 or 6 turns idk
              if operatorhasattacked == False:
                for enemy in active_enemies:
                  if enemy.turnstopass == 5:
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
    print ("(2) Squad 2")
    print ("(3) Squad 3")
    print ("(4) Squad 4")
    e = input("")
    if e == "x":
      menu = "main"
    if e == "1":
      for operator in squad_1:
        print (operator)
    if e == "2":
      for operator in squad_2:
        print (operator)
    if e == "3":
      for operator in squad_3:
        print (operator)
    if e == "4":
      for operator in squad_4:
        print (operator)
      input("")

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
