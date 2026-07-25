#Write python script using package to calculate area and volume of cube and sphere

import cude as c
import sphere as s

num = int(input("enter a number: "))

print("area of cube: ", c.area(num))
print("volume of cube: ", c.volume(num))
print("area of sphere: ", s.area(num))
print("volume of sphere: ", s.volume(num))