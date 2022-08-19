a=input("Enter first number")
b=input("Enter second number")
c=input("Enter third number")
if a>b and a>c:
    print(f"{a} is the greatest")
elif b>c and b>a:
    print(f"{b} is the greatest")
else:    
    print(f"{c} is the greatest")

