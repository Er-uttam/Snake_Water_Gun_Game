class SnakeGame:
    while True:
      name1 = input("Enter the 1st player name : ")
      choice1 = input("Enter s for snake , w for water and  g for gun : ")
      print(f"{name1} chooose : {choice1}")
  
      name2 = input("Enter the second player name:")
      choice2 = input("Enter s for snake , w for water and  g for gun : ")
      print(f"{name2} choose : {choice2}")
  
      if(choice1 == choice2):
          print("It's a Tie.")
      elif(choice1 == "s" and choice2 == "w"):
          print(f"{name1} win !")
      elif(choice1 =="w" and choice2 == "g"):
          print(f"{name1} win !")
      elif(choice1 == "s" and choice2 == "g"):
          print(f"{name1} win!")
  
      elif(choice2 == "s" and choice1 == "w"):
          print(f"{name2} win !")
      elif(choice2 =="w" and choice1 == "g"):
          print(f"{name2} win !")
  
      elif(choice2 == "s" and choice1 == "g"):
          print(f"{name2} win!")
  
      else:
          print("Invalid choice!")
      user_option = input("Enter y for quit and n for no :")
      if user_option =="y":
        break

  
obj = SnakeGame()
obj1 = SnakeGame()
