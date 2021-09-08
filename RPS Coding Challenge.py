#1 = rock
#2 = scissors
#3 = paper

import random #imports random library

def Outcome(UserTurn, CompTurn): #Comparing results function
  if UserTurn == 1 and CompTurn == 1: #user rock, CPU rock
    return "it's a draw", 0
  elif UserTurn == 1 and CompTurn == 2: #user rock, CPU scissors
    return "The User Wins", 1
  elif UserTurn == 1 and CompTurn == 3: #user rock, CPU paper
    return "The CPU Wins", 2

    
  elif UserTurn == 2 and CompTurn == 2: #User scissors vs CPU scissors
    return "it's a draw", 0
  elif UserTurn == 2 and CompTurn == 3: #User scissors vs CPU paper
    return "The User Wins", 1
  elif UserTurn == 2 and CompTurn == 1: #User scissors vs  CPU rock
    return "The CPU Wins", 2


  elif UserTurn == 3 and CompTurn == 3: #user paper, CPU paper
    return "it's a draw", 0
  elif UserTurn == 3 and CompTurn == 1: #user paper, CPU rock
    return "The User Wins", 1
  elif UserTurn == 3 and CompTurn == 2: #user paper, CPU scissors
    return "The CPU Wins", 2
    
def CompInput(): #Computer input function
  CompTurn = random.randrange(1,4)
  if CompTurn == 1 : #rock
    return 1, "the CPU chose rock"
  elif CompTurn == 2: #scissors
   return 2, "the CPU chose scissors"
  elif CompTurn == 3: #paper
    return 3, "the CPU chose paper"
  else:
    return "Invalid"

def UserInput(): #User input function
  UserTurn = input("Choose rock, paper, or scissors: ").lower()
  if UserTurn == "rock":
    return 1, "the User chose rock"
  elif UserTurn == "scissors":
    return 2, "the User chose scissors"
  elif UserTurn == "paper":
    return 3, "the User chose paper"
  else:
    print("Invalid input")
    UserInput()


def Body(): #Main function that calls on other functions
  UserWin = 0
  CompWin = 0
  Draw = 0
  Games = 0
  while UserWin < 2 and CompWin < 2 and Draw < 3 and Games < 3:
    UserTurn, UserPick = UserInput()
    CompTurn, CompPick = CompInput()
    Out = Outcome(UserTurn, CompTurn)[0]
    Win = Outcome(UserTurn, CompTurn)[1]
    print (str(Out) + ", " + str(UserPick) + ", " + str(CompPick))
    if Win == 1:
      UserWin += 1
      Games += 1
    elif Win == 2:
      CompWin += 1
      Games += 1
    elif Win == 0:
      Draw +=1
      Games += 1
    else:
      print("Error!")
  
  
  Continue = input("Exit or Continue?: ").lower()
  if Continue == "exit":
    exit
  elif Continue == "continue":
    Body()
  else:
    print("No decision")
    exit

def Main():
  Body()

Main()