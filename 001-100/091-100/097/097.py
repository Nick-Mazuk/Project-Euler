num = 1
for i in range(7830457):
    num *= 2
    num %= 10000000000

num *= 28433
num %= 10000000000

num += 1

print(num)