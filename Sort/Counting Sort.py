#Counting Sort

count=[0]*5
array=[1,3,2,4,3,2,5,3,1,2,3,4,4,3,5,1,2,3,5,2,3,1,4,3,5,1,2,1,1,1]

for i in range (0,30):
    count[array[i]-1]+=1

for i in range (len(count)):
    for j in range (count[i]):
        print(i+1, end = ' ')