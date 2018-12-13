def fifthPower(n):
    num = str(n)
    total = 0
    for digit in num:
        total += int(digit) ** 5
    if total == n:
        return True
    return False


total = 0

for i in range(2, 354294):
    if fifthPower(i):
        total += i

print("total", total)
