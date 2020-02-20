import math
import time
import sys

try:
    file = open(sys.argv[1], "r")
except:
    print("No file named \"{}\" found".format(sys.argv[1]))
    quit()

# try:
#     file = open(sys.argv[1], "r")
# except:
#     file = open("4_homework/graph.txt", "r")

forest = []
V = int(file.readline())
for i in range(V):
    forest.append(tuple(map(int, file.readline().split(" "))))

class edge:
    def __init__(self, parent_1, parent_2):
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.x = self.parent_1[0] - self.parent_2[0]
        self.y = self.parent_1[1] - self.parent_2[1]
        self.weight = round(math.sqrt(self.x*self.x + self.y*self.y))
        self.tree = 0

edgeList = []
for i in range(len(forest)-1):
    for j in range(i+1, len(forest), 1):
        edgeList.append(edge(forest[i], forest[j]))

edgeList.sort(key=lambda x: x.weight)
# for i in range(len(edgeList)):
#     print(edgeList[i].weight, edgeList[i].parent_1, edgeList[i].parent_2)

def parent(point):
    for i in range(len(edgeList)):
        if point == edgeList[i].parent_1 or point == edgeList[i].parent_2:
            if edgeList[i].tree > 0:
                return edgeList[i].tree
    return 0

treeList = []
treeDex = 1
mst = []
for i in range(len(edgeList)):
    if edgeList[i].tree == 0:
        p1 = parent(edgeList[i].parent_1)
        p2 = parent(edgeList[i].parent_2)
        if p1 == 0 and p2 == 0:
            edgeList[i].tree = treeDex
            treeDex += 1
        elif p1 != p2:
            edgeList[i].tree = p1
        if p2 != edgeList[i].tree and p2 > 0:
            for j in range(len(edgeList)):
                if edgeList[j].tree == p2:
                    edgeList[j].tree = p1

for i in range(len(edgeList)):
    if edgeList[i].tree > 0:
        # print("{} - {}   {}".format(edgeList[i].weight, edgeList[i].parent_1, edgeList[i].parent_2))
        print(edgeList[i].parent_1, edgeList[i].parent_2)
# for i in range(len(mst)):
#     print(mst[i].weight, mst[i].parent_1, mst[i].parent_2)