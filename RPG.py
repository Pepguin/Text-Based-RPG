'''
1. dictionary as player/enemy dictionary(hp, shield, strength)
2. integer
3. printStats() main loop first thing
4. getMove(): prints the options for the user and what they should choose, store the moves in a list
5. alot of "if" statements
6. player move:
  6a. check for what move as well as whether the move is a crit or if shield can be broken. "strength/power up" possible variety
  6b. possible variety (shield might stun)
7. cycle through moves to determine actions
  8a. attack or power up
#enemyMove(enemyAttack()):
    #enemyAttack():
change the dictionary, see an increase
clear (answer)
any move should be followed up by sleep
'''


import time

def clear():
  print("\033c", end="")

def getMoves():
  playerMoves = ["attack", "shield", "heal", "power up"]
  print("\n Moves: ")
  for move in playerMoves:
    print(" - " + (move))
  print("\n")
  while True: 
    playerChoice = input("What do you do? ")
    if playerChoice in playerMoves:
       return playerChoice
  print("\n")
  
def playerMoves(move):
  if move == "attack":
    if roundNum%3 == 2:
      print("Crit, your attack does twice damage! (" + str(player["strength"]*2) + " HP)" )
      time.sleep(1)
      enemy["hp"] -= player["strength"]*2
    else:
      print("You attacked the enemy! (" + str(player["strength"]) + " HP) ")
      time.sleep(1)
      enemy["hp"] -= player["strength"]
  elif move == "shield":
    if player["shield"] == "broken":
      print("Shield is broken! Wait for repair")
    else:
      print("You put up your shield")
      player["shield"] = "up"
  elif move == "heal":
    print("You healed yourself! (+15) hp")
    player["hp"] = min(player["hp"] + 15,100)
  elif move == "power up":
    print("Rage, Increased Strength!")
    player["strength"] += 5
  if player["shield"] == "broken":
    player["shield"] = "down"
      
def enemyAttack():
  if not player["shield"] == "up":
    player["hp"] -= enemy["strength"]
    print("-" + str(enemy["strength"]) + "hp")
  else:
    print("Enemy Attack Blocked! Shield Broken.")
    player["shield"] = "broken"
  
def enemyMove():
  cycle = roundNum%3
  if cycle == 0:
    print("The enemy attacked")
    time.sleep(1)      
    enemyAttack()
  elif cycle == 1:
    print("The enemy powers up")
    time.sleep(1)
    enemy["strength"] *= 2
  elif cycle == 2:
    print("The enemy released a powerful attack")
    time.sleep(2)
    enemyAttack()
    enemy["strength"] /= 2
  time.sleep(2)
  
  
def printStats():
    print("You: " + str(player["hp"]))
    if player["shield"] == "up":
      print('(shield)')
    else:
      print("\n")
    print("Enemy: " + str(enemy["hp"]))
    
  #PlayerMove(getMove())
player = {"hp":100,"shield":"down","strength":15}
enemy = {"hp":100,"shield":0,"strength":20}
roundNum = 0

print("An Enemy Has Appeared!")
time.sleep(2)

clear()
  
while True:
  printStats()
  playerMoves(getMoves())
  enemyMove()
  if player["hp"] <= 0:
    print("\n You Lose")
    break
  elif enemy["hp"] <= 0:
    print("\n Victory! Enemy Loses")
    break
  roundNum += 1
  clear()
  
  
