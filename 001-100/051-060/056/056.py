def sumDigits(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum

max = 0

for a in range (100):
    for b in range (100):
        num = a ** b
        sum = sumDigits(num)
        if sum > max:
            max = sum

print (max)