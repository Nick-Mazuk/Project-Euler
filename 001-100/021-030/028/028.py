sum = 0
num = 1
for i in range(1,1001,2):
    for j in range(0,4):
        sum += num
        num += i + 1
sum += num
print("sum",sum)
