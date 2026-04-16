def f(arr, N, limit):
    arr.sort()
    total = 0
    while True:
        if arr[0]+total > limit:  # if nothing is able to added to the total
            break
        for x in range(len(arr)-1, -1, -1):  # starts at the largest number
            if arr[x]+total <= limit:
                total += arr[x]
                break
            else:
                arr.pop(x)
    tmp = limit // arr[0]
    if tmp * arr[0] > total:
        total = tmp * arr[0]
    return total

46.61
18.4
15
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        nums = []
        tmp = input().split(" ")
        types = int(tmp[0])
        speed_limit = int(tmp[1])
        tmp_nums = input().split(" ")
        for j in tmp_nums:
            nums.append(int(j))
        print(f(nums, types, speed_limit))
