import random
stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
========= 
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

#TODo-1 Create a variable called 'lives' to keep track of the number of lives left.
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""   #This is to have '_' for each letter in word picked from word_list
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

#TODO-1 If guess is not a letter in chosen_word, Then reduce lives by '1'
# If live goes down to 0 then game should end and it should print "You have lost the game!"
    if guess not in chosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            game_over = True
            print("You have lost the game!")

    if "_" not in display:
        game_over = True
        print("You win!")

#TODO-3 Print the ASCII art from "stages"
# That corresponds to the current number of 'lives' the user has remaining.
print(stages[lives])