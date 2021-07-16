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
game()
