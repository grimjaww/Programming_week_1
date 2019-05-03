x = input("Enter a string: ")
y = input("Enter a pattern: ")

m = len(x)

result = ''
temp = 'Null'
j = 0
i = 0

for i in range(len(x)):
    #print('I:', i)
    #print('X: ',x[i])
    #print('y: ',y[j])
    #print(temp)
    if i < m and y[j] == x[i]:
        result += x[i]
        j = j + 1
        i = i + 1
        #if i < m:
        temp = x[i] 
    elif y[j] == '.':
        result += x[i]
        j = j + 1
        i = i + 1
        temp = x[i]
    elif y[j] == '*':
        if i == 0 or temp == 'Null':
            j = j + 1
            break
        if  i != m:
            if temp == x[i]:
                #print(temp)
                #print(x[i])
                result += x[i]
                i = i + 1
                #temp = x[i]
                if i == m-1:
                    break
        #print('I: ',i)
            if i < m and (temp != x[i - 1]):
                j = j + 1
    else:
        break
#loop = loop + 1

print('Result: ',result)
if x == result:
    print('True')
else:
    print('False')
    
