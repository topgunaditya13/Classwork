import random
def game():
  move=input("Pick rock, paper, or scissors")
  comp_moves=["rock, paper, scissors"]
  comp_move = random.choice(comp_moves)
  if move=comp_move:
    print("Tie Game")
  elif move="rock":
    if comp_move="paper":
      print("Computer wins!!!")
    elif comp_move="scissors":
      print("Player wins!!!")
  elif move="paper":
    if comp_move="scissors":
      print("Computer wins!!!")
    elif comp_move="rock":
      print("Player wins!!!")
  elif move="scissors":
    if comp_move="rock":
      print("Computer wins!!!")
    elif comp_move="paper":
      print("Player wins!!!")      
user_input = input("Welcome to rock paper scissors!!! Enter everything here in lowercase. Enter y or n to continue.")
while True:
  if user_input = "y":
    game()
  if user_input = "n":
    quit()
