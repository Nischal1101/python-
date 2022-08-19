# write a function that returns largest of three numbers using args
x = input("Input the first number")
y= input("Input the first number")
z = input("Input the first number")


def function(*args):
    if(args[0] > args[1] and args[0] > args[2]):
        return args[0]
    elif(args[1] > z and args[1] > x):
        return args[1]
    else:
        return args[2]


print("The largest number is ", function(x, y, z))
