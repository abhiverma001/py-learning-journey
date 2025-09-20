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

choice1 = input('You\'re at a crossword, where do you want to go? Type "left" or "right" : ').lower()  #here lower() is used to convert all the letters into small case.

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                  'There is an island in the middle of the lake, '
                  'Type "wait" to wait for a boat, '
                  'Type "swim" to swim across : ').lower()
    if choice2 == "wait":
        choice3 = input('You have arrived at Island.'
                        'There\'re three rooms.'
                        'Please choose the correct door "Red" or "Blue" or "Yellow" to enter into the room : ').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over!")
        elif choice3 == "Blue":
            print("You've entered a room of beasts. Game Over!")
        elif choice3 == "yellow":
            print("You've found the treasure. You've Win!")
        else:
            print("You've not choosen any door, Game Over!")
    else:
        print("You got attacked by an angry trout. Game Over!")
elif choice1 == "right":
    print("Game Over!")
else:
    print("Select correct answer, please")
