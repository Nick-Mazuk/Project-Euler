import math

def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
        if p > math.sqrt(x):
            break
    return True


def primeSieve(n):
    primes = [2, 3]
    for x in range(5, n, 2):
        if checkForPrime(primes, x):
            primes.append(x)
    return primes


primes = set(primeSieve(1000000))

print('primes caluclated')

def isCircularPrime(n):
    digits = len(str(n))
    test = n
    for i in range(digits - 1):
        test = int(str(test)[-1] + str(test)[:-1])
        if not (test in primes):
            return False
    return True

counter = 0

for p in primes:
    if isCircularPrime(p):
        counter += 1

print(counter)