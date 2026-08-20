# Write a Python script to Create a Class which Performs Basic Calculator Operations.

class calculate:
    def __init__ (self, num1, num2):        
        self.num1 = num1
        self.num2 = num2
        
    def add(self):
        print(self.num1 + self.num2)

    def sub(self):
        print(self.num1 - self.num2)

    def mul(self):
        print(self.num1 * self.num2)

    def div(self):
        print(self.num1 / self.num2)

num1 = int(input("enter number1 : "))
num2 = int(input("enter number2 : "))

cal = calculate(num1, num2)

cal.add()
cal.sub()
cal.mul()
cal.div()