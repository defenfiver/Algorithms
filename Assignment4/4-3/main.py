n, e = input().split(" ")
n, e = int(n), int(e)
if n == e:
    print("0")
else:
    exploding = input().split(" ")
    tubes = [0 for x in range(n)]
    for i in range(len(exploding)):
        tmp = int(exploding[i])
        tubes[tmp] = -1
    current = -1
    for i in range(n):
        if tubes[i] == -1:
            current = i
        elif current != -1:
            tubes[i] = i - current
    tubes = tubes[::-1]
    current = -1
    for i in range(n):
        if tubes[i] == -1:
            current = i
        elif current != -1:
            if tubes[i] > i - current:
                tubes[i] = i - current
    print(max(tubes))

