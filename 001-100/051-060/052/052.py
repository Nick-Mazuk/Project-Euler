def sameDigits(nums):
    num1List = list(str(nums[0]))
    num2List = list(str(nums[1]))
    num3List = list(str(nums[2]))
    num4List = list(str(nums[3]))
    num5List = list(str(nums[4]))
    num6List = list(str(nums[5]))
    return sorted(num1List) == sorted(num2List) == sorted(num3List) == sorted(num4List) == sorted(num5List) == sorted(num6List)

def multiples(num):
    return [num, num * 2, num * 3, num * 4, num * 5, num * 6]

found = False

i = 1;

while not found:
    mults = multiples(i)
    if sameDigits(mults):
        found = True
        print (i)
    if (i % 10000 == 0):
        print (i)
    i += 1
