# Python Program to Create a Class in which One Method Accepts a String from the 
# User and Another method Prints it. 
# Define a class named Country which has a method called print Nationality. 
# Define subclass named state from Country which has a method called printState. 
# Write a method to print state, country and nationality.

class country: 
    def __init__(self):
        country = ""
        nationality = ""
    
    def acceptNationality(self):
        self.country = input("enter country: ")
        self.nationality = input("enter nationality: ")

    def printNationality(self):
        print("Country: ", self.country)
        print("Nationality: ",self.nationality)
        
        
class state(country):
    def __init__(self):
        self.state = ""

    def acceptState(self):
        self.state = input("enter state: ")

    def printState(self):
        print("State: ", self.state)

s = state()

s.acceptNationality()
s.acceptState()

s.printNationality()
s.printState()