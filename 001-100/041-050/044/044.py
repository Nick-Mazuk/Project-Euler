def pentagonSieve(n):
    arr = []
    for i in range (1, n + 1):
        arr.append(i * (3 * i - 1) / 2)
    return set(arr)

pentagons = pentagonSieve(10000)

minD = 9223372036854775807 # maximum integer from Python 2

for pj in pentagons:
    for pk in pentagons:
        if (pj + pk in pentagons and abs(pj - pk) in pentagons):
            minD = abs(pj - pk)

print (minD)