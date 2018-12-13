import math

class Primes:
    def __init__(self):
        self.__primeList = [2, 3]
        self.__primeSet = set([2, 3])

    def __generatePrimes(self, n):
        for x in range(self.__primeList[-1], n + 2, 2):
            if self.__checkForPrime(x):
                self.__addPrime(x)

    def __checkForPrime(self, x):
        for p in self.__primeList:
            if x % p == 0:
                return False
            if p > math.sqrt(x):
                break
        return True
    
    def __isPrime(self, n):
        if n in self.__primeSet:
            return True
        return False
    
    def isPrime(self, n):
        if n > self.__primeList[-1]:
            self.__generatePrimes(n)
        return self.__isPrime(n)
    
    def __addPrime(self, p):
        self.__primeSet.add(p)
        self.__primeList.append(p)
