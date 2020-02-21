import math
import time
import sys

try:
    file = open(sys.argv[1], "r")
    # file = open("graph2.txt", "r")
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

def parent(point):
    for i in range(len(edgeList)):
        if point == edgeList[i].parent_1 or point == edgeList[i].parent_2:
            if edgeList[i].tree > 0:
                return edgeList[i].tree
    return 0

treeList = []
treeDex = 1
mst = []
for i in range(0, len(edgeList)):
    if edgeList[i].tree == 0:
        p1 = parent(edgeList[i].parent_1)
        p2 = parent(edgeList[i].parent_2)
        if p1 == p2:
            if p1 == 0:
                edgeList[i].tree = treeDex
                treeDex += 1
        elif p1 != p2:
            if p1 != 0:
                edgeList[i].tree = p1
            else:
                edgeList[i].tree = p2
            if p2 != edgeList[i].tree and p2 > 0:
                for j in range(len(edgeList)):
                    if edgeList[j].tree == p2:
                        edgeList[j].tree = p1
            elif p1 != edgeList[i].tree and p1 > 0:
                for j in range(len(edgeList)):
                    if edgeList[j].tree == p1:
                        edgeList[j].tree = p2

print("Point(x, y)         Distance")
for i in range(len(edgeList)):
    if edgeList[i].tree > 0:
        print("{} - {}     {}".format(edgeList[i].parent_1, edgeList[i].parent_2, edgeList[i].weight))
        # print("{}\n{}\n{}\n{}".format(edgeList[i].parent_1[0], edgeList[i].parent_1[1], edgeList[i].parent_2[0], edgeList[i].parent_2[1]))

# with open("test.txt", "w") as file:
#     for i in range(len(edgeList)):
#         file.write("tree: {}, {}= {} - {}\n".format(edgeList[i].tree, edgeList[i].weight, edgeList[i].parent_1, edgeList[i].parent_2))