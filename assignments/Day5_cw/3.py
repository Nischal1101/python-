# WAP that counts number of words in a sentence entered by user
x = input("Enter a sentence")
count = 1
for i in x:
    if i == ' ':
        count = count+1
print(count)
