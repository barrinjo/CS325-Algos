import time

file = open("data.txt", "r")
data = list(map(int, file.read().split(" ")))
start_time = time.time()

def mergeSort(array):
    if(len(array) > 1):
        half = len(array)//2
        left = array[:half]
        right = array[half:]
        print(left, right)

        mergeSort(left)
        mergeSort(right)

        iter = i = j = 0
        while i < len(left) or j < len(right):
            print(j, len(right), left[i], right[j])
            if j == len(right) or left[i] <= right[j]:
                array[iter] = left[i]
                i += 1
            else:
                array[iter] = right[j]
                j += 1
            iter += 1

mergeSort(data)
print(data)
print("--- %s seconds ---" % (time.time() - start_time))
