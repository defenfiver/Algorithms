"""
Idea for the solution came from
https://towardsdatascience.com/understanding-dynamic-programming-75238de0db0d/
"""


def f(arr, N):
    dp = [0 for _ in range(N)]
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for x in range(2, N):
        # arr[0] + f(2)
        inc = arr[x] + dp[x-2]  # if you included 0
        # 0 + f(1)
        exc = dp[x-1]  # if you excluded 0
        dp[x] = max(inc, exc)
    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    tmp_nums = input().split(" ")
    nums = []
    for i in tmp_nums:
        nums.append(int(i))
    print(f(nums, n))
