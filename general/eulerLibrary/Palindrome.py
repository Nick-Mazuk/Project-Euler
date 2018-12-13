class Palindrome:
    def __init__(self):
        pass

    def isPalendrome(self, test):
        if not (isinstance(test, int) or isinstance(test, str)):
            return False
        test = str(test)
        for i in range(int(len(test) / 2 + 1)):
            if test[i - 1] != test[-i]:
                return False
        return True

    def reverse(self, test):
        isInt = isinstance(test, int)
        isString = isinstance(test, str)
        test = str(test)
        reversedTest = test[::-1]
        if isString:
            return reversedTest
        if isInt:
            return int(reversedTest)
        return False
