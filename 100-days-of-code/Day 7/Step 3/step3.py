import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#TODO-1 - Use a while loop to let the user guess again.
guess = input("Guess a letter: ").lower()

display = ""

#TODO-2 - Change the for loop so that you keep the previous corrections are added om display variable.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)