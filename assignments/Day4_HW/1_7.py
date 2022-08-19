#1 Wap to find the largest and smallest number in a list, the length of list is unknown. Use function to perform the task
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

#2 Wap to print only items of list ending with 's'
A = ['Nis', 'kaf', 'sas', 'san']
b = []
for i in A:
    if i[-1] == 's':
        b.append(i)
print(b)

#3 WAP to filter the list of integers using lambda function
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: x % 2 == 0, x))
odd = list(filter(lambda x: x % 2 != 0, x))
print(even)
print(odd)

#4 wap to find the intersection of two given arrays using function
s = [1, 2, 3, 5,  7, 8, 9, 10]
t = [1, 2, 4, 8, 9]
s = set(s)
t = set(t)

#7 WAP that tokenizes a string and display the new string with reversed tokens.
x = 'he is a good boy.'
b = ''
z = ''
for i in x:
    if i != ' ':
        b = i+b
    elif i == ' ':
        z = z+' '+b
        b = ''
print(z)



def function():
    print(s.intersection(t))


function()


