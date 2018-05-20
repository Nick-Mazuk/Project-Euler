def odd(n):
    return 3 * n + 1

def even(n):
    return n / 2

def collatz(n, sequence):
    if n == 1:
        return sequence
    if n % 2 == 0:
        sequence.append(n)
        return collatz(even(n), sequence)
    sequence.append(n)
    return collatz(odd(n), sequence)

def longestCollatz(n):
    longest = -1;
    chainLength = -1;
    for i in range(1,n):
        print(i)
        chain = collatz(i,[])
        if len(chain) > chainLength:
            longest = i
            chainLength = len(chain)
    return longest, chainLength

print(longestCollatz(1000000))
