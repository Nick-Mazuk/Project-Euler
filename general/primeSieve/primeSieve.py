def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
    return True

def primeSieve(n):
    primes = [2,3];
    for x in range (5,n):
        if checkForPrime(primes, x):
            primes.append(x)
    return primes
