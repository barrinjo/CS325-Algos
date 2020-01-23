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
    if len(array) > 2:
        # floor length instead of divide in case len is odd number
        # split array into two arrays at index of floored length
        print(array, len(array)//3)
        mid1 = len(array)//3
        mid2 = (len(array)//3)*2
        # print(mid1, mid2)
        left = array[:mid1]
        center = array[mid1:mid2]
        right = array[mid2:]
        # print(left, center, right)

        # recursively call mergeSort on each split list
        mergeSort(left)
        mergeSort(center)
        mergeSort(right)

        # setup iterators for merge operation
        iter = i = j = k = 0
        # merge as long as iterators are smaller than array sizes
        while i < len(left) and j < len(right) and k < len(center):
            if left[i] <= right[j] and left[i] <= center[k]:
                array[iter] = left[i]
                i += 1
            elif right[j] <= left[i] and right[j] <= center[k]:
                array[iter] = right[j]
                j += 1
            elif center[k] <= left[i] and center[k] <= right[j]:
                array[iter] = center[k]
                k += 1
            iter += 1
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[iter] = left[i]
                i += 1
            else:
                array[iter] = right[j]
                j += 1
            iter += 1

        while j < len(right) and k < len(center):
            if right[j] <= center[k]:
                array[iter] = right[j]
                j += 1
            else:
                array[iter] = center[k]
                k += 1
            iter += 1

        while i < len(left) and k < len(center):
            if left[i] <= center[k]:
                array[iter] = left[i]
                i += 1
            else:
                array[iter] = center[k]
                k += 1
            iter += 1

        while i < len(left):
            array[iter] = left[i]
            i += 1
            iter += 1
        
        while j < len(right):
            array[iter] = right[j]
            j += 1
            iter += 1
        
        while k < len(center):
            array[iter] = center[k]
            k += 1
            iter += 1
    elif len(array) == 2:
        if array[1] > array[0]:
            temp = array[0]
            array[0] = array[1]
            array[1] = temp


# call function on data and print time
mergeSort(data)
print(data)
# write data to file
# first = True
# with open("merge.txt", "w") as file:
#     for item in data:
#         if first:
#             file.write("%s" % item)
#             first = False
#         else:
#             file.write(" %s" % item)
#     file.write("\n")
# print("%s seconds" % (time.time() - start_time))
