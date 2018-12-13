from eulerLibrary.Palindrome import Palindrome

palindrome = Palindrome()


def lychrel(n):
    for i in range(50):
        newNum = n + palindrome.reverse(n)
        if palindrome.isPalendrome(newNum):
            return False
        n = newNum
    return True


count = 0

for i in range(1, 10000):
    if lychrel(i):
        count += 1

print(count)
