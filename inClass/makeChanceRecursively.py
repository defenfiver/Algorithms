def makeChange(x, coins):
    if not coins:
        return 0
    using = max(coins)
    y = x // using
    coins.remove(using)
    if y == 0:
        return makeChange(x, coins)
    test1 = y + makeChange((x - y * using), coins)
    test2 = makeChange(x, coins)
    if test1 > 0:
        if test2 > 0:
            return min(test1, test2)
        return test1
    return test2


print(makeChange(30, [1, 10, 25]))
