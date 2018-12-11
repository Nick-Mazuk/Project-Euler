def checkForPrime(primes, x):
    for p in primes:
        if x % p == 0:
            return False
    return True

def primeSieve(n):
    primes = set([2, 3])
    for x in range(5, n, 2):
        if x % 100000 == 0:
            print(x)
        if checkForPrime(primes, x):
            primes.add(x)
    return primes

primes = primeSieve(1000000)

print('primes caluclated')

def primeleftright(p):
    while p > 0:
        if not (p in primes):
            return False
        try:
            p = int(str(p)[1:])
        except:
            p = 0
    return True

def primerightleft(p):
    while p > 0:
        if not (p in primes):
            return False
        try:
            p = int(str(p)[:-1])
        except:
            p = 0
    return True

total = 0

for p in primes:
    if primeleftright(p) and primerightleft(p) and p > 7:
        print(p)
        total += p

print('total', total)
