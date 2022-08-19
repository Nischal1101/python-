# WAP to filter the list of integers using lambda function
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = list(filter(lambda x: x % 2 == 0, x))
odd = list(filter(lambda x: x % 2 != 0, x))
print(even)
print(odd)
