# Write a Python program to accept two lists and merge the two lists into list of tuple

list1 = []
list2 = []
list3 = []

n = int(input("how many element: "))

for i in range(n):
    e = int(input("enter num: "))
    list1.append(e)

for i in range(n):
    e = input("enter char: ")
    list2.append(e)

for i in range(n):
    list3.append((list1[i], list2[i]))

print(list3)