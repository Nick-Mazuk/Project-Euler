#this is the brute force method. I may go back later and try to not brute force

divisors = [11,12,13,14,15,16,17,18,19,20]

#min is the smallest number for 10, the max is when you multiply 11-20 together
def main():
    for i in range(2520,670442572800):
        goodI = True
        for n in divisors:
            if i % n != 0:
                goodI = False
                continue
        if goodI:
            return i

print (main())
