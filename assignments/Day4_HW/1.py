# Wap to find the largest and smallest number in a list, the length of list is unknown. Use function to perform the task
x = []
s = int(input("Enter the size of list\t"))
print("Enter the elements in a list")


def nischal():
    for i in range(s):
        a = input()
        x.append(a)
        x.sort()


# print(x)
    print(f"{x[0]} is the smallest and {x[-1]} is the largest number in the list")


nischal()
