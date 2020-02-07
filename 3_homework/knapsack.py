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

# Recursive solution to 0-1 knapsack problem:
# takes arguments for weight available (W), weight list for items (wt),
# value list for items (val), and number of items (item)
def recursion(W, wt, val, i):
    # if either the available weight or remaining items is zero, return zero
    if W == 0 or i == 0:
        return 0

    # if the current item cannot fit within the available weight,
    # enter recursive knapsack again with the next item instead
    if W < wt[i - 1] :
        return recursion(W, wt, val, i - 1)
    # if the item can fit in the knapsack, take the max between the recursive value
    # of the next item (don't add current item to bag), or the value of current item
    # added with the value of the recursive value of the next item with the remaining
    # available weight (add current item to bag)
    else:
        return max(recursion(W, wt, val, i - 1),
        val[i - 1] + recursion(W-wt[i-1], wt, val, i - 1))

# nested loop to test different Weight and total item values
for W in range(30, 120, 30):
    for i in range(10, 28, 2):
        # initialize a wt and val array for the DP program
        wt_DP = []
        val_DP = []
        # fill arrays with random values, weights between 1 and 20,
        # and values between 1 and 100
        for j in range(i):
            wt_DP.append(random.randint(1, 20))
            val_DP.append(random.randint(1, 100))
        # copy the wt and val values to two arrays for the recursive program to use
        wt_rec = wt_DP.copy()
        val_rec = val_DP.copy()
        # print current weight and item counts
        print("N={} W={} ".format(i, W), end = " ")
        # start timer for recursive algo
        rec_time = time.time()
        # print max value found
        print("Rec Max = {}".format(recursion(W, wt_rec, val_rec, i)), end = " ")
        # print program time
        print("time = {} ".format("%.5f" % (time.time() - rec_time)), end=" ")
        # start timer for dp algo
        dp_time = time.time()
        # print max value found
        print("DP Max = {}".format(DP(W, wt_DP, val_DP, i)), end=" ")
        # print program time
        print("time = {}".format("%.5f" % (time.time() - dp_time)))
