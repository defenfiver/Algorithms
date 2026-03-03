num = int(input())
cases = []
for i in range(num):
    cases.append(int(input()))
for i in cases:
    if i == 1:
        print(8)
    else:
        xyz = i+i+1
        print(xyz * xyz)