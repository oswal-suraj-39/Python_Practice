# Write a Python script using class to reverse a string word by word

class String:
    def reverse_string(self):
        self.string = input("enter a string: ")
        print(self.string[::-1])
        
s = String()
s.reverse_string()