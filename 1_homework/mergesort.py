import time
import sys

# filename is pulled from command line, otherwise use "data.txt"
if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
else:
    file = open("data.txt", "r")
# read file and create list with " " as delimeter
data = list(map(int, file.read().split(" ")))
# remove first index which we don't need in this program
del data[0]

# start timer
start_time = time.time()

def mergeSort(array):
    # if list is of length 1, no action is needed 
    if(len(array) > 1):
        # floor length instead of divide in case len is odd number
        # split array into two arrays at index of floored length
        half = len(array)//2
        left = array[:half]
        right = array[half:]

        # recursively call mergeSort on each split list
        mergeSort(left)
        mergeSort(right)

        # setup iterators for merge operation
        iter = i = j = 0
        # merge as long as iterators are smaller than array sizes
        while i < len(left) or j < len(right):
            # j is done, so write i to merged array
            if j == len(right):
                array[iter] = left[i]
                i += 1
            # i is done, so write j to merged array
            elif i == len(left):
                array[iter] = right[j]
                j += 1
            # compare items in arrays, write smaller to merged array
            elif left[i] <= right[j]:
                array[iter] = left[i]
                i += 1
            else:
                array[iter] = right[j]
                j += 1
            # iterate to next spot in array
            iter += 1

# call function on data and print time
mergeSort(data)
# write data to file
first = True
with open("merge.txt", "w") as file:
    for item in data:
        if first:
            file.write("%s" % item)
            first = False
        else:
            file.write(" %s" % item)
    file.write("\n")
# print("%s seconds" % (time.time() - start_time))
