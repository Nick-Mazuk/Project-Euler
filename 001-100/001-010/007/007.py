def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
    return True

def primeSieve(n):
    primes = [2,3];
    x = 5
    while len(primes) <= n:
        if checkForPrime(primes, x):
            primes.append(x)
        x = x + 1
    return primes[n - 1]

print(primeSieve(10001))
