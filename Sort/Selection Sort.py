#Selection Sort

array = [11, 1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(len(array)-1):
    min_idx = i
    for j in range(i, len(array)):
        if (array[min_idx]>array[j]):
            min_idx = j
    temp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = temp

print(array)