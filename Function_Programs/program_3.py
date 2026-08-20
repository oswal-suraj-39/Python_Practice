# Write a python program to accept string and 
# remove the characters which have odd index values of given string using user defined function.

def removeOddIndexValues(string):
    
    result = ""
    
    for i in range(len(string)):
        
        if i % 2 == 0:
            result += string[i]
            
    print(result)

string = input("enter a string: ")

removeOddIndexValues(string)