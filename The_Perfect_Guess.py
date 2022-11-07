while (True):
    print("Press q to quit")
    import random
    randNumber = random.randint(1, 100)
    userGuess = None
    guesses = 0
    while (userGuess != randNumber):
        userGuess = input("Enter your number: ")
        if userGuess == 'q':
            exit()
        try:
            userGuess = int(userGuess)
            guesses += 1
            if (userGuess == randNumber):
                print("your guesss is right")
                print(f"You guess the number in {guesses} guesses")
            else:
                if (userGuess < randNumber):
                    print("You guessed it wrong! Enter larger number")
                else:
                    print("You guessed it wrong! Enter smaller number")
        except Exception as e:
            print(f"Your input resulted in an error: {e}")
    with open("The_Perfect_Guess_Highscore.txt", "r") as f:
        highscore = int(f.read())

    if (guesses < highscore):
        print("You have just broken the high score!")
        with open("The_Perfect_Guess_Highscore.txt", "w") as f:
            f.write(str(guesses))
    print("Thanks for playing this game")
