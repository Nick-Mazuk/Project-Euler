string = "12345678910"

for i in range(11,1000000):
    string += str(i)

product = 1
for i in range(0, 7):
    product *= int(string[(10 ** i) - 1])

print(product)
