def d(n):
    arr = []
    for i in range(1, n / 2 + 1):
        if n % i == 0:
            arr.append(i)
    return sum(arr)

totalSum = 0
n = 10000

for i in range(1,n):
    pair = d(i)
    original = d(pair)
    if original == i and pair != i and pair < n:
        print(i)
        totalSum += i

print(totalSum)
