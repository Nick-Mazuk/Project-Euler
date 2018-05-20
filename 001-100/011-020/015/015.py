def factorial(n):
    prod = 1;
    for i in range(1,n + 1):
        prod *= i
    return prod

def comb(n,r):
    return factorial(n) / (factorial(r) * factorial(n - r))

print (comb(40,20))
