# Write a Python program to unzip a list of tuples into individual lists.

zipped_list = [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = []
list2 = []

for i in zipped_list:
    list1.append(i[0])
    list2.append(i[1])

print("List 1:", list1)
print("List 2:", list2)