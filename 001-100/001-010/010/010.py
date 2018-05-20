def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
    return True

def primeSieve(n):
    primes = [2,3];
    for x in range (5,n,2):
        if checkForPrime(primes, x):
            primes.append(x)
    return primes

def sumList(primes):
    sum = 0;
    for p in primes:
        sum = sum + p
    return sum

print(sumList(primeSieve(2000000)))
