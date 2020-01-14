import time
import random

# print format
print("n | seconds")

# test n sizes from 1,000 to 15,000, at 1,000 size intervals 
for n in range(1000, 16000, 1000):
    uList = []
    oList = []
    # fill list with random numbers between 1 and 10,000
    for i in range(n):
        uList.append(random.randint(0, 10000))

    # start timer
    start_time = time.time()

    # iterate through unsorted list and sort items in the sorted list
    for i in range(len(uList)):
        # if list is empty, add first item
        if(not len(oList)):
            oList.append(uList[i])
        else:
            # bool to check if we've inserted the item
            insert = False
            # iterate through sorted list and until a smaller number is found
            for j in range(len(oList), 0, -1):
                if(oList[j - 1] <= uList[i]):
                    # insert the item and exit loop
                    oList.insert(j, uList[i])
                    insert = True
                    break
            # if end of loop is reached without insert, insert item at beginning of list
            if not insert:
                oList.insert(0, uList[i])

    # print data size and sort time
    print(n, "|", time.time() - start_time)
