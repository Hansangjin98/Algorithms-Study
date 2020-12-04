# Quick Sort

def quickSort(array, start, end):
  if start < end: # 원소가 1개가 아닐 때 실행
    q = partition(array, start, end) # pivot 설정

    quickSort(array, start, q-1)
    quickSort(array, q+1, end)

def partition(array, start, end):
    q = start 
    for i in range(start, end):
        if array[i] <= array[end]: #엇갈리지 않을 때
            temp  = array[q]
            array[q] = array[i]
            array[i] = temp
            q += 1
    temp = array[end]
    array[end] = array[q]
    array[q] = temp
    return q

array = [11, 1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
quickSort(array, 0, len(array)-1)
print(array)