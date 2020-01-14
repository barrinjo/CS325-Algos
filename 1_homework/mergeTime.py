import time
import random

# print format
print("n | seconds")

# test n sizes from 1,000 to 15,000, at 1,000 size intervals 
for n in range(1000, 16000, 1000):
    data = []
    # fill list with random numbers between 1 and 10,000
    for i in range(n):
        data.append(random.randint(0, 10000))

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
    # print data size and sort time
    print(n, "|", time.time() - start_time)
