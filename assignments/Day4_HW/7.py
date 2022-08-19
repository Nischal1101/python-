# WAP that tokenizes a string and display the new string with reversed tokens.
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
