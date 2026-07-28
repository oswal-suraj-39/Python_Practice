# Write a python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output: o-4, e-3, u-2, h-2, r-2, t-2

string = input("enter a string: ")
dict1 = {}

for i in list(string):
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
        
for k, v in dict1.items():
    print(k, " - ", v, end=", ")