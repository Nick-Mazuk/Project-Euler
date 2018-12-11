fibonacci = [1,1];

def appendFib(fibList):
    newNum = fibList[-1]+fibList[-2]
    fibList.append(newNum)
    return newNum

while len(str(fibonacci[-1])) < 1000:
    appendFib(fibonacci)

print (len(fibonacci))
