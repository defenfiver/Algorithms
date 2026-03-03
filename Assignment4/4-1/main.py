nums = input()
missions = input().split(" ")
numMissions, agents = nums.split(" ")
toSum = []
counter, multi = 0, 1
for i in range(int(numMissions)):
    missions[i] = int(missions[i])
missions.sort(reverse=True)
for i in range(int(numMissions)):
    toSum.append(int(missions[i]) * multi)
    counter += 1
    if counter >= int(agents):
        counter = 0
        multi += 1
print(sum(toSum))
