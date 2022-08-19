listss = input("Enter any string")
print(listss)
listss = list(listss)
print(listss)
y = []
for i in range(len(listss)):
    y.insert(i, listss[-i-1])
print(y)
