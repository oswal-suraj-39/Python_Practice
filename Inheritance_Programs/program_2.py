# Write a python script to define a class student having members roll no, name, age, gender.
# Create a subclass called Test with member marks of 3 subjects. 
# Create three objects of the Test class and display all the details of the student with total marks. 

class Student:
    def __init__(self, r, n, a, g):
        self.rollno = r
        self.name = n
        self.age = a
        self.gender = g
        
class Test(Student):
    def __init__(self, r, n, a, g, e, m, s):
        super().__init__(r, n, a, g)
        self.eng = e
        self.math = m
        self.sci = s

    def display(self):
        self.total = self.eng + self.math + self.sci
        print("\n-----Student Details-----")
        print("Roll No      :", self.rollno)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Gender       :", self.gender)
        print("English      :", self.eng)
        print("Math         :", self.math)
        print("Science      :", self.sci)
        print("Total Marks  :", self.total)
        
# Create objects
test1 = Test(1, "Ashish", 20, "Male", 80, 87, 75)
test2 = Test(2, "Ram", 21, "Male", 83, 79, 80)
test3 = Test(3, "Suraj", 21, "Male", 74, 85, 80)

# Display results
test1.display()
test2.display()
test3.display()