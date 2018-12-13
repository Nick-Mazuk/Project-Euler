from eulerLibrary.Palindrome import Palindrome

palindrome = Palindrome()


def isPalendromeInBothBases(num):
    if palindrome.isPalendrome(num):
        base2num = bin(num)[2:]
        if palindrome.isPalendrome(base2num):
            return True
    return False


total = 0

for i in range(1, 1000000):
    if isPalendromeInBothBases(i):
        total += i

print(total)
