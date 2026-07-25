# Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case. 
# Further modify the program to reverse a string word by word and print it in lower case.

class Strings:
    def get_String(self):
        self.string = input("enter a string: ")
    
    def print_String(self):
        print(self.string.upper())

    def reverse_String (self):
        reverse_str = self.string[::-1]
        print(reverse_str.lower())
        
objStr = Strings()
objStr.get_String()
objStr.print_String()
objStr.reverse_String()