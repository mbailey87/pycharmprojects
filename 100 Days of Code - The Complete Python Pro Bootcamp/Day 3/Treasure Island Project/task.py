print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# option one pick a direction  L= continue or R= game over
direction = input("Pick a direction Left or Right. \n").lower()
if direction == "left":
    lake = input("You come to a lake do you choose to Swim or Wait? \n").lower()
    if lake == "wait":
        door = input("A boat picks you up and takes you across the lake. \n "
                     "You see 3 doors one Red one Blue one Yellow. Which door do you open? \n").lower()
        if door == "yellow":
            print("congratulations you found the chest \n "
                  "You Win!")
        elif door == "red":
            print("A trap went off you were burned to death \n "
                  "Game Over")
        elif door == "blue":
            print("You were eaten by beasts \n "
                  "Game Over")
        else:
            print("you chose a door that doesnt exist. \n "
                  "Game Over")
    else:
        print("You were were attacked by a trout! \n "
              "Game Over")
else:
    print("You fall into a hole.\n Game Over")
# option 2 wait or swim Wait = continue Swim = game over

# option 3 which door not yellow = game over yellow 3 win


