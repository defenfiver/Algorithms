def brickFactory(bricks, N):
    NZ = 0
    total = 0
    while NZ != N:
        ma = max(bricks)
        ima = bricks.index(ma)
        total += ma
        bricks[ima] = 0
        NZ += 1
        if ima+1 < N:
            if bricks[ima + 1] != 0:
                bricks[ima+1] = 0
                NZ += 1
        if ima-1 >= 0:
            if bricks[ima-1] != 0:
                bricks[ima-1] = 0
                NZ += 1
    return total


if __name__ == "__main__":
    n = int(input())
    tmp_nums = input().split(" ")
    nums = []
    for i in tmp_nums:
        nums.append(int(i))
    print(brickFactory(nums, n))
