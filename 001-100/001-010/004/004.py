import math

def isPalindrome(num):
    numString = str(num)
    for i in range(0, math.ceil(len(numString) / 2)):
        if numString[i] != numString[-(i+1)]:
            return False
    return True

def findPalindromes(n):
    palindromes = []
    for i in range(n, 99, -1):
        for j in range(n, 99, -1):
            if isPalindrome(i * j):
                palindromes.append(i*j)
    return palindromes

def largestPalindrome(n):
    return max(findPalindromes(n))

print (largestPalindrome(999))
