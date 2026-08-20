# Define a class named Rectangle which can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area and Perimeter.

class rectangle:
    
    def __init__(self, l, w):
        self.length = l
        self.width = w
        self.area = 0
        self.perimeter = 0