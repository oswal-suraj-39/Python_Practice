# Write a Python program to compute element-wise sum of given tuples.   
# Original lists: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1) 
# Element-wise sum of the said tuples: (6, 9, 8, 6)

t1 = (1, 2, 3, 4)
t2 = (3, 5, 2, 1)
t3 = (2, 2, 3, 1)
l1 = []

for i in range(0, 4):
    r = t1[i] + t2[i] + t3[i]
    l1.append(r)
    
t4 = tuple(l1)
print(t4)