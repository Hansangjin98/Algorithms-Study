#Insertion Sort

array = [11, 1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
for i in range(len(array)-1):
    for j in range(i, -1, -1):
        if array[j]>array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
    

print(array)