# Write a Python program to convert a tuple of string values to a tuple of integer 
# values.   Original tuple values: (('333', '33'), ('1416', '55')) 
#           New tuple values:      ((333, 33), (1416, 55))

list1 = []
tuple1 = ("10", "20", "30", "40", "50")

print("Original tuple values: ", tuple1)

for i in tuple1:
    n = int(i)
    list1.append(n)

tuple1 = tuple(list1)

print("New tuple values:", tuple1)
