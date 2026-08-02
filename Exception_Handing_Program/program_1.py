# Define a class Date (Day, Month, Year) with functions to accept and display it. 
# Accept date from user. 
# Throw user defined exception “invalid Date Exception” 
# if the date is invalid.

import datetime as dt

class date:
    day = 1
    month = 1
    year = 2000

    def accept (self):
        self.year = int(input("enter a year: "))
        
        try:
            self.month = int(input("enter a month: "))
        except self.month > 12:
            print("invalid Date Exception: you enter more then 12 month")
        else:
            try:
                self.day = int(input("enter a day: "))
            except self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12 and self.day > 31:
                print("invalid Date Exception: you enter more then 31 day in january, march, may, july, august, october or december ")
            except self.month == 2 and self.day > 28:
                print("invalid Date Exception: you enter more then 28 day in february")
            except self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11 and self.day > 30:
                print("invalid Date Exception: you enter more then 30 day in april, june, september, november")
        print("all clear...!")

    def display (self):
        print(dt.datetime(self.year, self.month, self.day))
        
d = date()
d.accept()
d.display()