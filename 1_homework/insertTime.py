import time
import random

# if len(sys.argv) > 1:
#     file = open(sys.argv[1], "r")
# else:
#     file = open("data.txt", "r")
print("(n, time(sec))")
for n in range(1000, 16000, 1000):
    uList = []
    oList = []
    for i in range(n):
        uList.append(random.randint(1, 10000))

    start_time = time.time()

    for i in range(len(uList)):
        if(not len(oList)):
            oList.append(uList[i])
        else:
            insert = False
            for j in range(len(oList), 0, -1):
                if(oList[j - 1] <= uList[i]):
                    oList.insert(j, uList[i])
                    insert = True
                    break
            if not insert:
                oList.insert(0, uList[i])

    # print((n, (time.time() - start_time)))
    print(time.time() - start_time)
