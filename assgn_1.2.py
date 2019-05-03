x = input("Enter a string: ")
y = input("Enter a pattern: ")

m = len(x)

result = ''
loop, count = 0, 0
j = 0
i = 0

for i in range(len(x)):
    #print(i)
    if x[i] == y[j]:
        result += x[i]
        j = j + 1
    elif y[j] == '.':
        result += x[i]
        j = j + 1
    elif y[j] == '*':
        if i == 0:
            break
        if  i != m:
            if x[i] == x[i + 1]:
                result += x[i]
                i = i + 1
                if i == m-1:
                    break
    else:
        break
loop = loop + 1

if result in x:
    print('True')
else:
    print('False')
    
