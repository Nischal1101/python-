# write a function that returns only the unique items in a list.
a = [1, 2, 3, 4, 5, 7, 7, 3]
b = []


def function(x, y):
    for i in x:
        if i not in y:
            y.append(i)
    print(y)


function(a, b)
