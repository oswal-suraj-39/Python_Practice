# Write a python script to implement bubble sort using list

li = [9, 5, 7, 3, 8, 2]

print("unsorted list: ", li)

for j in range(len(li)):
    
    for i in range(0, len(li) - 1):
        if li[i] > li[i+1]:
            temp = li[i]
            li[i] = li[i+1]
            li[i+1] = temp
               
print("sorted list: ", li)