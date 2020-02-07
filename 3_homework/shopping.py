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

    # backwards lookup to see which items the family member is holding
    i = count
    w = W
    # start at the final corner of the memo.  If the value above is the same,
    # then the item in current row is not being held,
    # otherwise, add the current item to the hold list and move on to next item
    # subtracting the weight of the current item we know is being held
    # once we hit zero, there are no either no items left or no weight left
    while memo[i][w] != 0:
        # item is not being held.  iterate i to check next item
        if memo[i][w] == memo[i-1][w]:
            i -= 1
        # item is being held.  subtract weight of item, move to next item,
        # and add item to hold list
        else:
            subHoldList.append(i)
            i -= 1
            w -= wt[i]
    return memo[count][W]

# initializing ints for .txt parsing
T = N = f = 0
# file pointer to write results
out = open("results.txt", "w")
# file pointer to read file
with open("shopping.txt", "r") as file:
    # first line is how many cases we're doing
    # iterate through T
    T = int(file.readline())
    for i in range(T):
        # initialize arrays
        subtotals = []
        holdList = []
        wt = []
        val = []
        # first line in each case is the number of items
        N = int(file.readline())
        # iterate through items and add their values and weights to corresponding array
        for j in range(N):
            # temp array stores the values until they're written to their arrays
            temp = list(map(int, file.readline().split(" ")))
            val.append(temp[0])
            wt.append(temp[1])
        # first line after items have been read is family member count
        f = int(file.readline())
        # iterate through family and run knapsack algo on each one
        for k in range(f):
            # create array to store items held
            subHoldList = []
            # add optimized carry value for family member to the list of values
            subtotals.append(knapsack(int(file.readline()), wt, val, N, subHoldList))
            # add held items to list of held items
            holdList.append(subHoldList)
        # printing results
        out.write("Test Case {}\n".format(i + 1))
        # use sum to get grand total from subtotal list
        out.write("Total Price {}\n".format(sum(subtotals)))
        out.write("Member Items\n")
        # iterate through family members and print out their held items
        for j in range(f):
            out.write("    {}: ".format(j+1))
            for k in range(len(holdList[j]), 0, -1):
                out.write("{} ".format(holdList[j][k-1]))
            out.write("\n")