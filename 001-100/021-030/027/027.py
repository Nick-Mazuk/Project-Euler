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

primes = primeSieve(10000)

# just solves the equation
def quadratic(a, b, n):
    return n ** 2 + a * n + b

# returns the length of the prime chain
def primeChain(a, b):
    stillPrimes = True
    n = 0
    while stillPrimes:
        if quadratic(a, b, n) in primes:
            n += 1
            continue
        stillPrimes = False
    return n

maxPrimes = 0
maxProduct = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        primeLength = primeChain(a, b)
        if(primeLength > maxPrimes):
            maxPrimes = primeLength
            maxProduct = a * b

print (maxProduct)