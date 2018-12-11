from itertools import permutations

pandigitals = set(permutations(range(0, 10)))
pandigitals = set(map(lambda thing: ''.join(str(x) for x in thing), pandigitals))

primes = [2, 3, 5, 7, 11, 13, 17]

total = 0

for num in pandigitals:
    for i in range(len(primes)):
        divisible = True
        integer = int(num[i+1:i+4])
        if integer % primes[i] != 0:
            divisible = False
            break
    if divisible:
        total += int(num)

print (total)
