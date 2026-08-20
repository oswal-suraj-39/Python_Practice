# Write a python program to create a class Circle and Compute the Area 
# and the circumferences of the circle.(use parameterized constructor) 

class circle:
    
    area = 0
    circumferences = 0
    
    def __init__(self, r):
        self.radius = r
        self.area = 0
        self.circumferences = 0

    def compute(self):
        self.area = 3.14 * self.radius**2
        self.circumferences = 2 * 3.14 * self.radius

r = int(input("enter a radius: "))    
c = circle(r)

c.compute()

print("area of circle: ", c.area)
print("circumferences of circle: ",c.circumferences)