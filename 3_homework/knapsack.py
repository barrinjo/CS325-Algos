import random
import time

def DP(W, wt, val, count):
    memo = [[0 for i in range(W + 1)] for j in range(count + 1)]
    for i in range(count + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                memo[i][w] = 0
            elif wt[i - 1] > w:
                memo[i][w] = memo[i - 1][w]
            else:
                memo[i][w] = max(memo[i - 1][w],
                val[i - 1] + memo[i - 1][w - wt[i - 1]])
    return memo[count][W]

def recursion(W, wt, val, i):
    if W == 0 or i == 0:
        return 0

    if W < wt[i - 1] :
        return recursion(W, wt, val, i - 1)
    else:
        return max(recursion(W, wt, val, i - 1),
        val[i - 1] + recursion(W-wt[i-1], wt, val, i - 1))

for W in range(30, 150, 30):
    for i in range(10, 32, 2):
        wt_DP = []
        val_DP = []
        for j in range(i):
            wt_DP.append(random.randint(1, 20))
            val_DP.append(random.randint(1, 100))
        wt_rec = wt_DP.copy()
        val_rec = val_DP.copy()
        print("N={} W={} ".format(i, W), end = " ")
        rec_time = time.time()
        print("Rec Max = {}".format(recursion(W, wt_rec, val_rec, i)), end = " ")
        print("time = {} ".format("%.5f" % (time.time() - rec_time)), end=" ")
        dp_time = time.time()
        print("DP Max = {}".format(DP(W, wt_DP, val_DP, i)), end=" ")
        print("time = {}".format("%.5f" % (time.time() - dp_time)))
