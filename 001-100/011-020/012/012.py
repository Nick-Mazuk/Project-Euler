import math

def triangle(n):
    sum = 0
    for i in range(1,n):
        sum += i
    return sum

def numFactor(n):
    count = 0;
    for i in range(1,math.ceil(math.sqrt(n+1))):
        if n % i == 0:
            count += 2
    return count

def highDivisTriangle():
    for i in range (1000,100000):
        print(i)
        num = triangle(i)
        if numFactor(num) > 500:
            return num

print(highDivisTriangle())
