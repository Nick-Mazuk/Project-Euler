from eulerLibrary.Primes import Primes
from itertools import permutations

primes = Primes()


def findPermutations(n):
    string = str(n)
    perms = [int("".join(p)) for p in permutations(string)]
    return perms


def createsSequence(n):
    if not primes.isPrime(n):
        return False
    perms = findPermutations(n)
    for secondNum in perms:
        if primes.isPrime(secondNum) and secondNum != n:
            distance = secondNum - n
            thirdNum = secondNum + distance
            if (
                primes.isPrime(thirdNum)
                and len(str(thirdNum)) == 4
                and thirdNum in perms
            ):
                return str(n) + str(secondNum) + str(thirdNum)
    return False


for i in range(1000, 10000):
    if createsSequence(i) and i != 1487:
        print(createsSequence(i))
        break
