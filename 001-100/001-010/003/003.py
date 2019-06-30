import math


def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
    return True


def primeSieve(n):
    primes = [2, 3]
    for x in range(5, n):
        if checkForPrime(primes, x):
            primes.append(x)
    return primes


def isFactor(n, f):
    if n % f == 0:
        return True
    return False


num = 600851475143


def largestPrimeFactor(n):
    primes = primeSieve(math.ceil(math.sqrt(n)))
    for i in range(len(primes) - 1, 0, -1):
        if num % primes[i] == 0:
            return primes[i]
    return -1

print(largestPrimeFactor(num))

