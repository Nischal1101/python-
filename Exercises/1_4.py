# 1 write a function that returns largest of three numbers using args
import string
from sre_compile import isstring
x = input("Input the first number")
y = input("Input the first number")
z = input("Input the first number")


def function(*args):
    if(args[0] > args[1] and args[0] > args[2]):
        return args[0]
    elif(args[1] > z and args[1] > x):
        return args[1]
    else:
        return args[2]


print("The largest number is ", function(x, y, z))

# 2 write a function that returns only the unique items in a list.
a = [1, 2, 3, 4, 5, 7, 7, 3]
b = []


def function(x, y):
    for i in x:
        if i not in y:
            y.append(i)
    print(y)


function(a, b)

# 3 write a function that returns the list with only integers


x = [1, 2, 3, 'tangs', 'dada']
y = []


def function(x):
    for i in x:
        if (isstring(i) == True):
            continue

        else:
            y.append(i)
    return y


print("The required list is ", function(x))

# 4 wap to sort the following list using lambda function
cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'MItsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]


cars.sort(key=lambda x: x['year'])
print(cars)
