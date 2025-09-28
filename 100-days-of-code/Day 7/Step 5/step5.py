import random
#TODO-1 Update the word list to use the 'word_list' from hangman_words.py

#TODo-2 Import the logo from the hangman-art.py and print it at the start of the game.
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
lives = 6

#TODO-3 Import the logo from the hangman_art.py and print
print(logo)

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
    #TODO-6 Update the code below to tell the user how many lives they have left.
    print(f"************** {lives}/6 Lives left *********************")
    guess = input("Guess a letter: ").lower()

    #TODO-4 If the user had entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed:- {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)

#TODO-5 If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
# e.g. You guessed d, that's not in the word. You lose a life.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

        #TODO-7 Update the print statement below to give the user the correct word they were trying to guess.

        if lives == 0:
            game_over = True
            print(f"***********IT WAS {chosen_word}!, YOU LOSE***************")

    if "_" not in display:
        game_over = True
        print("You win!")

#TODO-3 Update the code below to use the stages list from the file hangman_art.py
print(stages[lives])