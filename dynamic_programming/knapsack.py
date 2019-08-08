def knapsack(items, val, w):
    n = len(items)
    dp = [[0 for i in range(w+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for w in range(w+1):
            if items[i-1] < w:
                dp[i][w] = max(val[i-1]+dp[i-1][w-items[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][w]


if __name__ == '__main__':
    items = [2,2,4,6,3]
    val = [3, 4, 8, 9, 6]
    w = 9
    print(knapsack(items, val, w))
