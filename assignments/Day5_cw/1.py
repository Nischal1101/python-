# WAP to print the multipication table of any number entered by user
x = input("Enter any number")
x = int(x)
for i in range(1, 11):
    s = x*i
    print(f"{x}*{i}= ", s)
