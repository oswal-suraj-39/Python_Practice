# Define a class Date (Day, Month, Year) with functions to accept and display it. 
# Accept date from user. 
# Throw user defined exception “invalid Date Exception” 
# if the date is invalid.

import datetime as dt

class date:
    day = 1
    month = 1
    year = 2000

    def display (self):
        print(dt.datetime(self.year, self.month, self.day))