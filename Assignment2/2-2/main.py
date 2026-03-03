import math

num = int(input())
cases = []
for i in range(num):
    cases.append(input())
for i in cases:
    x, y = i.split(" ")
    x, y = int(x), int(y)

    d12 = y//12 - x//12
    if x % 12 == 0:
        d12 += 1
    xsqr = math.ceil(math.sqrt(x))
    ysqr = math.floor(math.sqrt(y))
    psqrs = [z*z for z in range(xsqr, ysqr)]
    if xsqr == ysqr:
        psqrs.append(xsqr*xsqr)
    elif xsqr < ysqr:
        if xsqr == int(xsqr) and xsqr*xsqr not in psqrs:
            psqrs.append(x)
        if ysqr == int(ysqr):
            psqrs.append(ysqr*ysqr)
    ps = len(psqrs)
    b = len([z for z in psqrs if z % 12 == 0])
    print(f'{d12} {ps} {b}')