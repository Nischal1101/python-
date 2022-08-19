y = int(input("Enter a number"))
try:
    print(len(y))
except TypeError:
    print(fr"Coding is not for you\n {y} ")
except:
    print(fr"ohno error!\n {y}")
