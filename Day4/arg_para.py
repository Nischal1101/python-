# write a program to add all the numbers supplied by the user
def my_function(*args):
    sum = 0
    for i in range(len(args)):
        sum = sum+args[i]
    print("the sum is ", sum)


my_function(1, 2, 3, 4, 5)
