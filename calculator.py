import re

print("Simple Python calculator")
print("type 'quit' to exit\n")
initial = 0
run = True

def performCalc():
    global run
    global initial
    problem = ""
    if initial == 0:   
         problem = input("Enter Your Problem:")
    else:
        problem = input(str(initial))


    if problem == 'quit':
        print('Quitting Simple Python Calculator')
        run = False

    else:
        problem = re.sub('[a-zA-Z,.:()" "]', '', problem)

        if initial == 0:
            initial =  eval(problem)
        else:
            initial = eval(str(initial) + problem)

while run:
    performCalc()