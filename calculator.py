import re

print("Simple Python calculator")
print("press 'quit' to exit\n")
previous = 0
run = True

def performCalc():
    problem = input("Enter Your Problem: ")
    if problem == 'quit':
        run = False

    else:
         print("Your problem is", problem)

while run:
    performCalc()