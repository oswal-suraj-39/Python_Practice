# Write a python script to find the repeated items of a tuple

tuple1 = (2, 4, 5, 6, 2, 3, 4, 4, 7)
dict1 = {}

for i in tuple1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
        
print("dict1   : ", dict1)        
print("elements: ", tuple(dict1.keys()))
print("count   : ", tuple(dict1.values()))