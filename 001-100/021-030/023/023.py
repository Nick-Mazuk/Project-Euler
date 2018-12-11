import math
def divisors(n):
    divi = []
    for i in range(1,math.ceil(n / 2) + 1):
        if n % i == 0:
            divi.append(i)
    return divi

def isAbundant(n):
    sum = 0
    for divisor in divisors(n):
        sum += divisor
    if sum > n:
        return True
    return False

def abundantSieve(n):
    abundants = []
    for i in range(1, n):
        if isAbundant(i):
            abundants.append(i)
    return abundants

abundants = abundantSieve(28123)

#finding the sums of the abundants

sums = []

for abundantA in abundants:
    for abundantB in abundants:
        if abundantA + abundantB < 28123:
            sums.append(abundantA + abundantB)

sums = list(set(sums))

total = 0

for i in range(1,28123):
    if i not in sums:
        total += i

print (total)
