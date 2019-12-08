a,b = 193651, 649729
from collections import Counter
def checkAdj(x):
    y = str(x)
    repeats = []
    check = False
    for i in range(len(y)-1):
        if y[i] == y[i+1]:
            repeats.append(int(y[i]))
            check = True
    return check, repeats

def checkNoDecrease(x):
    y = str(x)
    check = True
    for i in range(len(y)-1):
        if y[i] > y[i+1]:
            check = False
    return check
count = 0
for i in range(a, b):
    if i == 222244:
        print(count)
    repeatDigits = []
    ca, repeats = checkAdj(i)
    if i == 222244:
        print(repeats)
    counted = Counter(repeats)
    target = -1
    if len(counted)>0:
        for k in counted.elements():
            if counted[k]==1:
                target = k
        if ca and checkNoDecrease(i):
            if len(set(repeats))==1 and len(repeats) ==1:            
                count +=1
            elif len(repeats)>1 and target >0 :
                count +=1
    if i == 222244:
        print(count)
    #print(count)
    
        

print(count)