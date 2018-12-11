def triangleSieve(n):
    arr = []
    for i in range(n):
        arr.append(i * (i + 1) / 2)
    return set(arr)

def pentagonalSieve(n):
    arr = []
    for i in range(n):
        arr.append(i * (3 * i - 1) / 2)
    return set(arr)

def hexagonalSieve(n):
    arr = []
    for i in range(n):
        arr.append(i * (2 * i - 1))
    return set(arr)


triangles = triangleSieve(100000)
hexagonal = hexagonalSieve(100000)
pentagonal = pentagonalSieve(100000)

smallest = 100000000000000000

for num in triangles:
    if num <= 40755:
        continue
    if num in hexagonal and num in pentagonal:
        if num < smallest:
            smallest = num

print (smallest)
