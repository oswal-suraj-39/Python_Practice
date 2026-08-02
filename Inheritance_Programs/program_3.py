# Define a class named Shape and its subclass(Square/ Circle).
# The subclass has an init function which takes an argument (Length/radius).
# Both classes should have methods to calculate area and volume of a given shape.

class shape:
    length = 0
    radius = 0

class square(shape):
    def __init__(self, l, r):
        self.length = l
        self.radius = r

class circle(shape):
    def __init__(self, l, r):
        self.length = l
        self.radius = r

l = int(input("enter a length: "))
r = int(input("enter a radius: "))

squ = square(l, r)
cir = circle(l,r)