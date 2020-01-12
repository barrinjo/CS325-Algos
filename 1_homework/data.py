import random
import sys

list = []
for i in range(int(sys.argv[1])):
    list.append(random.randint(1, 1000))

first = True
with open("data.txt", "w") as file:
    for item in list:
        if first:
            file.write("%s" % item)
            first = False
        else:
            file.write(" %s" % item)
    file.write("\n")
