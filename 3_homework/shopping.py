import random
import time

# Dynamic programming solution to 0-1 knapsack problem:
# takes arguments for weight available (W), weight list for items (wt),
# value list for items (val), and number of items (item)
def DP(W, wt, val, count):
    # initialize a memo to store sub-optimizations
    # memo has an extra column and row of zeros so we don't segfault
    # and we don't need complex exceptions for border cases
    memo = [[0 for i in range(W + 1)] for j in range(count + 1)]
    # nested loop: iterate through entire memo
    for i in range(count + 1):
        for w in range(W + 1):
            # initialize border with 0 value
            if i == 0 or w == 0:
                memo[i][w] = 0
            # if current item can't fit in bad at specified weight,
            # take optimization of the same weight for the last item
            elif wt[i - 1] > w:
                memo[i][w] = memo[i - 1][w]
            # if the item can fit in the max, take the max between the 
            # weight option for the previous item optimization or the
            # value of the current item added with the current optimization
            # of the current weight minus the weight of the new item
            else:
                memo[i][w] = max(memo[i - 1][w],
                val[i - 1] + memo[i - 1][w - wt[i - 1]])
    return memo[count][W]

with open("shopping.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
