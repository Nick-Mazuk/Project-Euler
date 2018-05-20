prod = 1;
for i in range(1,101):
    prod *= i

digits = list(str(prod))
sum = 0
for i in digits:
    sum += int(i)
print(sum)
