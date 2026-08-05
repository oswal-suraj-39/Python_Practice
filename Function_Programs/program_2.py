# Write an anonymous function to find area of square and rectangle.

square_area = lambda side : side * side
rectangle_area = lambda length , width : length * width

s = int(input("enter a side: "))
l = int(input("enter a length: "))
w = int(input("enter a width: "))

print("area of square: ",square_area(s))
print("area of rectangle: ",rectangle_area(l, w))