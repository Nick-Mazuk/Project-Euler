def squareDigit(num):
    sum = 0
    while num:
        sum += (num % 10) ** 2
        num //= 10
    return sum

def squareDigitChain(num):
    if(num == 1 or num == 89):
        return num
    return squareDigitChain(squareDigit(num))

counter = 0

for i in range(1, 10000000):
    if i % 100000 == 0:
        print(i)
    if squareDigitChain(i) == 89:
        counter += 1

print (counter)