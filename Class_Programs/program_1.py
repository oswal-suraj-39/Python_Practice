# Write a Python script using class, which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.

class Strings:
    def get_String(self):
        self.string = input("enter a string: ")
    
    def print_String(self):
        print(self.string.upper())