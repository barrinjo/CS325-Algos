import random
import time

# Dynamic programming solution to 0-1 knapsack problem:
# takes arguments for weight available (W), weight list for items (wt),
# value list for items (val), and number of items (item)
def knapsack(W, wt, val, count, subHoldList):
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
                # if val[i - 1] + memo[i - 1][w - wt[i - 1]] > memo[i - 1][w]:
                #     holdList[0] = i
    # for i in range(len(memo)):
    #     print(memo[i])
    i = count
    w = W
    while memo[i][w] != 0:
        if memo[i][w] == memo[i-1][w]:
            i -= 1
        else:
            subHoldList.append(i)
            i -= 1
            w -= wt[i]
    return memo[count][W]

# small function to find the location of an item in an array
def lookup(arr, target):
    count = 0
    # iterate through until the item is found
    while count < len(arr) and arr[count] != target:
        count += 1
    # return location
    return count

T = N = f = 0
out = open("results.txt", "w")
with open("shopping.txt", "r") as file:
    T = int(file.readline())
    for i in range(T):
        subtotals = []
        holdList = []
        wt = []
        val = []
        N = int(file.readline())
        for j in range(N):
            temp = list(map(int, file.readline().split(" ")))
            val.append(temp[0])
            wt.append(temp[1])
        f = int(file.readline())
        for k in range(f):
            subHoldList = []
            subtotals.append(knapsack(int(file.readline()), wt, val, N, subHoldList))
            holdList.append(subHoldList)
        out.write("Test Case {}\n".format(i + 1))
        out.write("Total Price {}\n".format(sum(subtotals)))
        out.write("Member Items\n")
        for j in range(f):
            out.write("{}: ".format(j+1))
            for k in range(len(holdList[j]), 0, -1):
                out.write("{} ".format(holdList[j][k-1]))
            out.write("\n")