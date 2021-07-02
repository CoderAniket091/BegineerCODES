# Exercise-2 Faulty calculator
# Design a calculator which gives every correct answer except following ones
# 45*3=555, 56+9=77, 56/6=4

"""print("Enter your name")
name = input()
print("Machine operator is", name)"""

while (True):
    print("Enter first number")
    n1 = int(input())
    print("insert your task ex. +,-,*,/")
    task = input()
    print("Enter second number")
    n2 = int(input())

    if n1 == 45 and n2 == 3 and task == "*":
        print("Answer is :", 555)
    elif n2 == 9 and n1 == 56 and task == "+":
        print("Answer is :", 4)
    elif n1 == 56 and n2 == 6 and task == "/":
        print("Answer is :", 77)
    elif task == "+":
        print("Answer is :", n1 + n2)
    elif task == "-":
        print("Answer is :", n1 - n2)
    elif task == "*":
        print("Answer is :", n1 * n2)
    elif task == "/":
        print("Answer is :", n1 / n2)
    else:
        print("Your task or input is invalid")
    continue
