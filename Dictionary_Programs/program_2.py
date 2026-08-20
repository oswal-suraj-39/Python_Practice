# Write a Python script to sort (ascending and descending) a dictionary by key and value.

dict1 = {'b': 3, 'a': 1, 'd': 4, 'c': 2}

print("ascending order by key: ",sorted(dict1.items()))

print("descending order by key: ",sorted(dict1.items(), reverse="True"))

print("ascending order by value: ",sorted(dict1.items(), key=lambda item: item[1]))

print("descending order by value: ",sorted(dict1.items(), reverse="True", key=lambda item: item[1]))