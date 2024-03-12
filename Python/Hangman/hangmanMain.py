#Hangman Game

#Import relevant modules and files
import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, win, lose, logo

#Generate a random word, get length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create game end and life objects
end_of_game = False
lives = 6

#print game logo
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blank based on word length
display = []
for _ in range(word_length):
    display += "_"

#While not the end of game
while not end_of_game:
    #Record player letter guess
    guess = input("Guess a letter: ").lower()

    #Clear previous guesses
    clear()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}.")

    #Check guessed letter, position
    for position in range(word_length):
        letter = chosen_word[position]

        #Testing code
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        #Display guessed letter if correct
        if letter == guess:
            display[position] = letter

    #Check if user is wrong, if so tell them
    if guess not in chosen_word:

        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        #Also remove a life
        lives -= 1
        #If 0 lives end game
        if lives == 0:
            end_of_game = True
            print("You ran out of lives!")
            print(lose)

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters, if so they win
    if "_" not in display:
        end_of_game = True
        print(win)

    #Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])