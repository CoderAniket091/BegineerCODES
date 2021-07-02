#SNAKE,WATER,GUN GAME
#DO WHILE LOOP FOR 10 TIMES
#DISPLAY SCORES AND FOR EACH WIN GIVE EACH POINT AND DECLARE WINNER AFTER 10 LOOPS

print("WELCOME TO SNAKE, WATER, GUN")
print("TYPE S FOR SNAKE, W FOR WATER AND G FOR GUN")
loop = 10
p = 0
p1 = 0
while(loop>0):
    print("Enter your chocie")
    c1 = input()
    c2 = c1.capitalize()
    import random

    choices = ["Snake", "Water", "Gun"]
    c = random.choice(choices)
    # print(c)
    print("Computer's choice", c)

    if c=="Snake" and c2=="S":
        print("IT's a tie.\n", "POINTS =",p)
        loop = loop-1
    if c=="Water" and c2=="W":
        print("IT's a tie.\n", "POINTS =",p)
        loop = loop-1
    if c=="Gun" and c2=="G":
        print("IT's a tie.\n", "POINTS =",p)
        loop = loop-1
    elif c=="Snake" and c2=="W":
        p = p + 1
        print("You Won\n", "POINTS =", p)
        loop = loop-1
    elif c=="Snake" and c2=="G":
        print("You lose\n","POINTS =",p)
        p1 = p1+1
        loop = loop-1
    elif c=="Water" and c2=="S":
        p = p + 1
        print("You Won\n","POINTS =",p)
        loop = loop-1
    elif c=="Water" and c2=="G":
        print("You lose\n","POINTS =",p)
        p1 = p1+1
        loop = loop - 1
    elif c == "Gun" and c2 == "S":
        print("You lose\n","POINTS =",p)
        p1 = p1+1
        loop = loop - 1
    elif c == "Gun" and c2 == "W":
        p = p + 1
        print("You won\n","POINTS =",p)
        loop = loop - 1

def umpire(p,p1):
    if p==p1:
        print("It's a tie")
    elif p>p1:
        print("You Won. CONGRATULATIONS!!!")
    else:
        print("You Lose. Better Luck Next Time!!!")
umpire(p,p1)
