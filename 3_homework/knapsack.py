import random

def DP(W, wt, val, count):
    memo = [[0 for i in range(W + 1)] for j in range(count + 1)]
    for i in range(count + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                memo[i][w] = 0
            elif wt[i - 1] > W:
                memo[i][w] = memo[i - 1][w]
            else:
                memo[i][w] = max(memo[i - 1][w], val[i - 1] + memo[i - 1][w - wt[i - 1]])
    return memo[count][W]
