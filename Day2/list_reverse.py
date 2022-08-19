listss = [1, 2, 3, 4, 5]
y = []
for i in listss:
    y.append(listss[i])
print(y)
# print(listss[-5:])


x = [1, 2, 3, 4]
for i in range(len(listss)):
    y.insert(i, x[-i-1])
print(y)
