sum = 2

fibonacci = [1,2];

def appendFib(fibList):
    newNum = fibList[-1]+fibList[-2]
    fibList.append(newNum)
    return newNum

num = 0;

while num < 4000000:
    num = appendFib(fibonacci)
    if num % 2 == 0:
        sum = sum + num

print (sum)
