# Write a python script to create a class Rectangle with data member’s length, width 
# and methods area, perimeter which can compute the area and perimeter of rectangle. 

class rectangle:
    length = 4
    width = 4

    def area(self):
        result1 = self.length * self.width
        return result1
    
    def perimeter(self):
        result2 = 2 * (self.length + self.width)
        return result2
    
rect = rectangle()