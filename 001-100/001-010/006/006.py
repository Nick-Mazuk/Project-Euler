def sumSquare(n):
    sum = 0
    for i in range(1,n):
        sum = sum + i**2
    return sum

def squareSum(n):
    sum = 0
    for i in range(1,n):
        sum = sum + i
    return sum**2

def squareSumDif(n):
    return squareSum(n) - sumSquare(n)

print (squareSumDif(101))
