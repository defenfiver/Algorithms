x = int(input())
init = []
for i in range(x):
    init.append([int(input())])
nums = []
counter = []
for i in range(x):
    c = init[i]
    if c not in nums:
        nums.append(c)
        counter.append(1)
    else:
        counter[nums.index(c)] += 1
ma = max(counter)
maxes = []
for i in range(len(counter)):
    if counter[i] == ma:
        maxes.append(nums[i])
print(min(maxes)[0])