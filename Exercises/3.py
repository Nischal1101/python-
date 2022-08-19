# write a function that returns the list with only integers
from sre_compile import isstring
import string


x = [1, 2, 3, 'tangs', 'dada']
y = []
def function(x):
    for i in x:
        if (isstring(i) == True):
         continue

        else:
         y.append(i)
    return y
print("The required list is ",function(x))
