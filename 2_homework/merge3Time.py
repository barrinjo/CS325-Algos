import time
import random

# print format
print("n | seconds")

# test n sizes from 1,000 to 15,000, at 1,000 size intervals 
for n in range(10000, 160000, 10000):
    data = []
    # fill list with random numbers between 1 and 10,000
    for i in range(n):
        data.append(random.randint(0, 10000))

    # start timer
    start_time = time.time()

    def mergeSort(array):
        # if list is of length 3 or more, recursively merge like normal 
        if len(array) > 2:
            # floor length instead of divide in case len is odd number
            # split array into two arrays at index of floored length
            mid1 = len(array)//3
            mid2 = (len(array)//3)*2
            left = array[:mid1]
            center = array[mid1:mid2]
            right = array[mid2:]

            # recursively call mergeSort on each split list
            mergeSort(left)
            mergeSort(center)
            mergeSort(right)

            # setup iterators for merge operation
            iter = i = j = k = 0
            # merge is based on which arrays have unsorted items left
            # first loop assumes that all arrays have unsorted items left
            while i < len(left) and j < len(right) and k < len(center):
                # whichever array has the lowest integer, add that to the sorted array and iterate
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
            
            # 1 loop for each condition once one of the arrays is empty
            # first goes if the center array is empty
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    array[iter] = left[i]
                    i += 1
                else:
                    array[iter] = right[j]
                    j += 1
                iter += 1

            # second goes if the left array is empty
            while j < len(right) and k < len(center):
                if right[j] <= center[k]:
                    array[iter] = right[j]
                    j += 1
                else:
                    array[iter] = center[k]
                    k += 1
                iter += 1

            # last goes if the right array is empty
            while i < len(left) and k < len(center):
                if left[i] <= center[k]:
                    array[iter] = left[i]
                    i += 1
                else:
                    array[iter] = center[k]
                    k += 1
                iter += 1

            # last three loops are simple
            # there is nothing left to compare, adding the rest of the items from whichever array is left
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
        # if array length is 2, just sort them
        # no case for array of len 1 because we just leave it alone
        elif len(array) == 2:
            if array[1] < array[0]:
                temp = array[0]
                array[0] = array[1]
                array[1] = temp

    # call function on data and print time
    mergeSort(data)
    # print data size and sort time
    print(time.time() - start_time)
