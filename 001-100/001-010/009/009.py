def euclids(m,n):
    if m < n:
        temp = n
        n = m
        m = temp
    return [m**2 - n**2, 2*m*n, m**2 + n**2]

def addsToThousand(abc):
    sum = abc[0] + abc[1] + abc[2]
    if sum == 1000:
        return True
    return False

def triplets():
    for m in range(0,100):
        for n in range(0,100):
            triplet = euclids(m,n)
            if addsToThousand(triplet):
                return triplet

def prodArray(abc):
    return abc[0] * abc[1] * abc[2]

print(prodArray(triplets()))
