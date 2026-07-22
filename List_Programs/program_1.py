# Write a Python program to accept n numbers in list and remove duplicates from a list.
N = int(input("enter how many number: "))
numbers = []
print("---enter the number---")
for i in range(N):
    num = int(input())
    if num not in numbers:
        numbers.append(num)
print("list without duplicate: ", numbers)