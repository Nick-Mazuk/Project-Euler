nums = []
for a in range(2,101):
    for b in range(2,101):
        nums.append(a**b)
print(len(set(nums)))
