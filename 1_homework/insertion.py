import time
import sys

if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
else:
    file = open("data.txt", "r")
uList = list(map(int, file.read().split(" ")))
oList = []

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

# print(oList)
print("--- %s seconds ---" % (time.time() - start_time))
