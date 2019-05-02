x = input("Enter a string: ")
y = input("Enter a pattern: ")

result = ''
j = 0

for i in range(len(x)):
    if x[i] == y[j]:
        result += x[i]
        j = j + 1
    elif y[j] == '.':
        result += x[i]
        j = j + 1
    elif y[j] == '*':
        if x[i] == x[i + 1] and i < len(x):
            result += x[i]
            i = i + 1

if result in x:
    print('True')
else:
    print('False')
    