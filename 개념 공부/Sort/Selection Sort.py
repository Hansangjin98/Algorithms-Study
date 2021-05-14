#Selection Sort

array = [11, 1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

print(array)