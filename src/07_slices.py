"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
num = a[1:2]
print(num[0])

# Output the second-to-last element: 9
num = a[4:5]
print(num[0])

# Output the last three elements in the array: [7, 9, 6]
num = a[3:6]
print(num)

# Output the two middle elements in the array: [1, 7]
num = a[2:4]
print(num)

# Output every element except the first one: [4, 1, 7, 9, 6]
num = a[1:6]
print(num)

# Output every element except the last one: [2, 4, 1, 7, 9]
num = a[:5]
print(num)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
s[1:5]
print(s[7:12])