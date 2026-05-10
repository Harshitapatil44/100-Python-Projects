import random 

def roll_dice():
  return random.randit(1, 6)

while True: 
  input("Press Enter to roll dice....!")
  
  result = roll_dice()
  print(f"You Rolled: " {result}")
  
  choice = input("if Want to roll again? press Y/N for your ans").lower()
  
  if choice  != "y":
      print("Thank you for Playing")
      break

