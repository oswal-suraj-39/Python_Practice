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
        
di = {1: "suraj", 
      2: "ram", 
      3: "krishna", 
      4: "ashish", 
      5: "taiyo"}

key = int(input("enter a key number: "))
isKey(di, key)