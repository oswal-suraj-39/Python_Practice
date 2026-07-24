# Write a python script to define a class student having members roll no, name, age, gender.
# Create a subclass called Test with member marks of 3 subjects. 
# Create three objects of the Test class and display all the details of the student with total marks. 

class Student:
    def __init__(self, r, n, a, g):
        self.rollno = r
        self.name = n
        self.age = a
        self.gender = g