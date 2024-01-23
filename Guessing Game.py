secret_word = "Hello"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of Guesses, You lose!")
else:
    print("You Win!")

#Line 1 - : Variables set. The secret word to guess is "Hello" to win the game. This can be changed if required.
#Line 2 - : The guess variable has been set as an empty string to be later used with an input() function.
#Line 3 - : The variable guess_count is used to help us keep track of how many guesses the user has had.
#Line 4 - : The guess_limit will be the maximum amount of guesses a user can have.
#Line 5 - : out_of_guess is set to false as it will start off as that until the user loses. Then it will show True

#Line 7 -: As long as the guess variable is not equal to secret word and the user is not ouf of gueses then the user will be given the opporunity to keep guessing.
#Line 12 -:If the out_of_guess = True then that means that the user has lost.
#Line 14 -: This is an if statement which will be used to print the "Out of Guesses, You lose!" message.
#Line 16 -: This is an else statement which will be the opposite of the if statement which will display a "You Win" message once the user has guessed it correctly.