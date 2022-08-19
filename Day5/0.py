# Else block runs when there is no error.
# finally block runs when try or except block runs
print("Enter two numbers")
try:
    x = int(input())
    y = int(input())
    print(x/y)
except ZeroDivisionError:
    print("You cannot place y=0")
except:
    print("ehehehehehe")
else:
    print("Something else")
finally:
    print("finally vetiyo ketaho")
