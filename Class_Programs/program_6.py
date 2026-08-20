# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area and Perimeter.

class rectangle:
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.area = 0
        self.perimeter = 0
        
    def compute(self):
        self.area = self.length * self.width
        self.perimeter = 2 * (self.length + self.width)
        
length = int(input("enter a length: "))
width = int(input("enter a width: "))

r = rectangle(length, width)
r.compute()

print("area of rectangle: ",r.area)
print("perimeter of rectangle: ",r.perimeter)