from decimal import Decimal, getcontext
import math

getcontext().prec = 10000


def recurringDecimalLength(d):
    decimal = str(Decimal(1) / Decimal(d))[:-1]
    lastDigit = decimal[-1]
    decimalLen = len(decimal)
    for i in range(2, decimalLen):
        if decimal[-i] == lastDigit:
            if (
                decimal[decimalLen - i :]
                == decimal[decimalLen - 2 * i + 1 : decimalLen - i + 1]
            ):
                return i
    return 0


maxLength = 0
maxD = 0

for i in range(2, 1000):
    repeatLength = recurringDecimalLength(i)
    if repeatLength > maxLength:
        maxD = i
        maxLength = repeatLength

print(maxD)

