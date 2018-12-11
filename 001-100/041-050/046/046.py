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

def twiceSquareSieve(n):
    arr = []
    for i in range(n):
        arr.append(2 * ((i + 1) ** 2))
    return set(arr)

primes = primeSieve(10000)
squares = twiceSquareSieve(1000)

for i in range(3,100000, 2):
    if i in primes:
        continue
    test = 0
    outlier = True
    while primes[test] < i:
        if i - primes[test] in squares:
            outlier = False
            break
        test += 1
    if outlier:
        print ('outlier', i)
        break
