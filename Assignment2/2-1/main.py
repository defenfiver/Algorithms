num = int(input())
cases = []
for i in range(num):
    cases.append(input())
for i in cases:
    n, m, c = i.split(" ")
    empty = int(n)//int(m)
    total = empty
    while empty >= int(c):
        new = empty//int(c)
        leftover = empty % int(c)
        total += new
        empty = empty//int(c) + leftover
    print(total)