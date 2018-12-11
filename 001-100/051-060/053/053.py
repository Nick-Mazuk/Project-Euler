import math

def factorialize(n):
    arr = []
    for i in range(n):
        factorial = math.factorial(i)
        arr.append(factorial)
    return arr

factorial = factorialize(101)

def combination(n,r):
    factorial[n]
    factorial[r]
    return factorial[n]/(factorial[r] * factorial[n - r])

counter = 0

for n in range(1, 101):
    for r in range (1, n + 1):
        if (combination(n, r) > 1000000):
            counter += 1

print(counter)