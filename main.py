#A tenary operator is an operator that is able to evaluate something based on if it is true or not

#An example is

age = int(input('Enter your age '))
discount = True if age >= 65 else False
print(discount)


#A switch case statement is a control mechanism that tests values stored in a variable and executes the corresponding case statements

#An example is



def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"


switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(int(input('Enter a number between 1-7 '))))
print(switch(int(input('Enter another number between 1-7 '))))