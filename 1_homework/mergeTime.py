import time
import random

# if len(sys.argv) > 1:
#     file = open(sys.argv[1], "r")
# else:
#     file = open("data.txt", "r")
for n in range(1000, 16000, 1000):
    data = []
    for i in range(n):
        data.append(random.randint(1, 10000))

    start_time = time.time()

    def mergeSort(array):
        if(len(array) > 1):
            half = len(array)//2
            left = array[:half]
            right = array[half:]
            # print(left, right)

            mergeSort(left)
            mergeSort(right)

            iter = i = j = 0
            while i < len(left) or j < len(right):
                # print(right, left)
                if j == len(right):
                    array[iter] = left[i]
                    i += 1
                elif i == len(left):
                    array[iter] = right[j]
                    j += 1
                elif left[i] <= right[j]:
                    array[iter] = left[i]
                    i += 1
                else:
                    array[iter] = right[j]
                    j += 1
                iter += 1

    # print(data)
    mergeSort(data)
    # print((n, (time.time() - start_time)))
    # print(n)
    print(time.time() - start_time)
