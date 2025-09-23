import random

print("====Game Hub====")

#Guess the number
print("\n Guess the Number")
ran_number = random.randint(1,20)
guess1 = int(input("Guess a number between 1 to 20: "))

if guess1 == ran_number:
    print("Correct! You got it in 1 try.")
else:
    guess2 = int(input("try again:"))
    if guess2 == ran_number:
        print("Correct! You got it in second attempt!")
    else:
        guess3 = int(input("try again:"))
        if guess3 == ran_number:
            print('Correct! You got it in final attempt')
        else:
            print("Sorry you lost the game! the correct number is :", ran_number)

#Dice roller
print("\nDice Roller Game!")
roll1 = random.randint(1,6)
roll2 = random.randint(1,6)
roll3 = random.randint(1,6)
roll4 = random.randint(1,6)
roll5 = random.randint(1,6)
dice_rolls = [roll1, roll2, roll3, roll4, roll5]
print("Dice rolled 5 time : ", dice_rolls)


# FizzDuzz
print("\nFizzDuzz Game!")
for number in range(1,20):
    if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 7 == 0:
        print("Pop")
    else:
        print(number)




