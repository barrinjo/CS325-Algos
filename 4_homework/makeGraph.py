import random
import sys

try:
    size = int(sys.argv[1])
except:
    print("usage: makeGraph.py <size> <filename>")
    quit()

try:
    fileName = sys.argv[2]
except:
    print("usage: makeGraph.py <size> <filename>")
    quit()

graph = []
i = 0
while i < 100:
    temp = (random.randint(0,size), random.randint(0,size))
    if temp not in graph:
        graph.append(temp)
        i += 1

with open(fileName, "w") as file:
    file.write("{}\n".format(size))
    for i in range(len(graph)):
        file.write("{} {}\n".format(graph[i][0], graph[i][1]))
