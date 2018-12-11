# Not Finished
# Should produce the right answer in a really long time

import time
import itertools

start_time = time.time()

def getNum(string):
    numString = ''
    counter = 0
    for char in string:
        counter += 1
        if (char == '1'):
            numString += str(counter)
            counter = 0
    counter += 1
    numString += str(counter)
    return sorted(numString)

def getBinaryNumbers(n):
    binaryTuples = map(list, itertools.product([0, 1], repeat=n))
    binaries = map(lambda thing: ''.join(str(x) for x in thing), binaryTuples)
    return binaries

i = 0
while True:
    print('i', i)
    if 2 ** i < 1000000:
        i += 1
        continue
    binaries = getBinaryNumbers(i)
    print('binaries')
    numberLists = [getNum(x) for x in binaries]
    print("list")
    numbers = set(map(lambda thing: ''.join(str(x) for x in thing), numberLists))
    print('set')
    if len(numbers) > 1000000:
        break
    i += 1

print ('p', i + 1)

print("--- %s seconds ---" % (time.time() - start_time))

