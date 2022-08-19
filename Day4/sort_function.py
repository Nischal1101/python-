x = [5, 2, 3, 1, 0]
x.sort(reverse=True)
print(x)
y = ['apple', 'cat', 'monkey', 'sachin', 'tangsdada']
y.sort(key=lambda l: len(l), reverse=True)
print(y)
