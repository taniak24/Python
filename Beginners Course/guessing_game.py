
secret_word = "giraffe"
guess = ""
tries = 0
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if tries < 3:
        guess = input("Enter a guess: ")
        tries += 1
    else:
        out_of_guesses = True

if(out_of_guesses):
    print("You are out of guesses!")
else:
    print("YOU WIN!")
