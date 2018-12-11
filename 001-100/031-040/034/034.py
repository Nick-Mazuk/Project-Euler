def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
    return product

def factorialSum(n):
    total = 0
    for digit in map(int, str(n)):
        total += factorial(digit)
    return total

total = 0

for i in range(3, 1000000):
    if factorialSum(i) == i:
        total += i

print (total)