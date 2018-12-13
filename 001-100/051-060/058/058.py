from eulerLibrary.Primes import Primes

primes = Primes()

primeCount = 0.0
corners = 1.0
currentNumber = 1

for sideLength in range(2, 100000, 2):
    for i in range(4):
        currentNumber += sideLength
        if primes.isPrime(currentNumber):
            primeCount += 1
        corners += 1
    # test if the percentage falls below the required length
    percentage = primeCount / corners
    if(percentage < .1):
        print('Side Length', sideLength + 1, currentNumber)
        break
    if sideLength % 1000 == 0:
        print (currentNumber)
