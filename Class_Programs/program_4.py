# Write a Python class named Student with two attributes student_name, marks. 
# Modify the attribute values of the said class and 
# print the original and modified values of the said attributes. 

class student:
    student_name = "suraj"
    marks = 90
    
    def modify(self):
        
        print("-----original values-----")
        print("student name  : ", self.student_name)
        print("student marks : ", self.marks)
        
        self.student_name = input("enter new student name  : ")
        self.marks = int(input("enter new student marks : "))
        
        print("-----modified values-----")
        print("student name  : ", self.student_name)
        print("student marks : ", self.marks)

s = student()
s.modify()