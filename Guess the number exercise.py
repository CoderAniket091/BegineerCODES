# Hide A NUMBER IN YOUR CODE AND CREATE A GUESS THE NNUMBER CODE
# NUMBER OF GUESSES IS 9
# print NO. OF GUESSES TOOK TO FINISH
# PRINT GAME OVER IF GUSSES ARE OVER AND WON IF WON

g = 9
while (g>0):
    n = 18
    print("Guess the number")
    n1 = int(input())
    g = g - 1
    if n1 == 19:
        print("You are close to it\n", "Guesses remaining", g)

    if n1 == 17:
        print("You are closer\n", "Guesses remaining", g)

    elif n1 > n:
        print("Think more lesser number\n", "Guesses remaining", g)

    elif n1 < n:
        print("Think more greator number\n", "Guesses remaining", g)

    if g == 0:
        print("Your game is over. Try again")

    if n1 == n:
        print("Congratulations!!! You Won!!!\n", "You takes", 9 - g, "guesses")
        print("To play again type y and to stop type n")
        p=input()
        if p=="y":
            print("Wise choice")
            continue
        elif p=="n":
            print("Thanks for playing guess the number v1.0")
            break
        else:
            print("Invalid option")




