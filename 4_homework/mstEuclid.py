import math
import time
import sys

if len(sys.argv) == 2:
    # open file from argv
    try:
        file = open(sys.argv[1], "r")
    # exit with error if file not found
    except:
        print("No file named \"{}\" found".format(sys.argv[1]))
        quit()
else :
    print("usage: \"python3 mstEuclid.py <filename.txt>\"")
    quit()

# Class that holds the points that make an edge,
# the weight, and what tree the edge is currently in
class edge:
    def __init__(self, parent_1, parent_2):
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.x = self.parent_1[0] - self.parent_2[0]
        self.y = self.parent_1[1] - self.parent_2[1]
        self.weight = round(math.sqrt(self.x*self.x + self.y*self.y))
        self.tree = 0

# array that holds every point
forest = []
# get line 1 which holds the number of vertices
V = int(file.readline())
# read in file and create list of points
for i in range(V):
    forest.append(tuple(map(int, file.readline().split(" "))))

# array to hold compete list of edges between vertices
edgeList = []
# loop twice and make pairs of every possible combination
for i in range(len(forest)-1):
    for j in range(i+1, len(forest), 1):
        edgeList.append(edge(forest[i], forest[j]))

# sort list by increasing weight of each edge
edgeList.sort(key=lambda x: x.weight)

# function to lookup the tree values of an edges two parents
def parent(point):
    # iterate through the list of edges
    for i in range(len(edgeList)):
        # once there's a match, return tree value
        if point == edgeList[i].parent_1 or point == edgeList[i].parent_2:
            if edgeList[i].tree > 0:
                return edgeList[i].tree
    return 0

# index to track new tree values
treeDex = 1
# iterate through list of edges
for i in range(0, len(edgeList)):
    # get the tree values of the parents of current edge
    p1 = parent(edgeList[i].parent_1)
    p2 = parent(edgeList[i].parent_2)
    # if they're equal, only add to a tree if they're zero
    # if they're not zero, then don't add them (that will cause cycle!)
    if p1 == p2:
        if p1 == 0:
            # if the parent tree values are both zero, then we're creating a new tree
            # assign a tree value of the current treeDex and iterate treeDex
            edgeList[i].tree = treeDex
            treeDex += 1
    # if they're not equal, it gets more complicated
    else:
        # if either parent tree value is 0, add the
        # current edge to the nonzero parent tree
        if p1 != 0:
            edgeList[i].tree = p1
        else:
            edgeList[i].tree = p2
        # if the other point being added is a nonzero value, 
        # then it belongs to a different existing tree, and
        # we need to merge the trees
        if p2 != edgeList[i].tree and p2 > 0:
            for j in range(len(edgeList)):
                if edgeList[j].tree == p2:
                    edgeList[j].tree = p1
        elif p1 != edgeList[i].tree and p1 > 0:
            for j in range(len(edgeList)):
                if edgeList[j].tree == p1:
                    edgeList[j].tree = p2

sum = 0
# print format
print("Point(x, y)         Distance")
# iterate through edgeList and print out edges with nonzero values
for i in range(len(edgeList)):
    # nonzero trees are in the MST
    if edgeList[i].tree > 0:
        # add the weight to the total distance
        sum += edgeList[i].weight
        # print parent information and distance of edge
        print("{} - {}     {}".format(edgeList[i].parent_1, edgeList[i].parent_2, edgeList[i].weight))

# print total distance
print("    Total Distance: {}".format(sum))
