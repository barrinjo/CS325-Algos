import random

graph = []
i = 0
while i < 100:
    temp = (random.randint(0,100), random.randint(0,100))
    if temp not in graph:
        graph.append(temp)
        i += 1

with open("graph3.txt", "w") as file:
    file.write("100\n")
    print(len(graph))
    for i in range(len(graph)):
        file.write("{} {}\n".format(graph[i][0], graph[i][1]))
