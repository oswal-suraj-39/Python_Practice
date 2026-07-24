# Write a Python program to check if a given key already exists in a dictionary.
# If key exists replace with another key/value pair.

def isKey (di, key):
    if key in di:
        print("key is exist")
        del di[key]
        newKey = int(input("enter new key number: "))
        newValue = input("enter a value string: ")
        di[newKey] = newValue
        print(di)
    else:
        print("key is not exist")