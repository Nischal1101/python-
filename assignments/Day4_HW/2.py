# Wap to print only items of list ending with 's'
A = ['Nis', 'kaf', 'sas', 'san']
b = []
for i in A:
    if i[-1] == 's':
        b.append(i)
print(b)
