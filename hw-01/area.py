# Assignment 1, Task 5
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 3 mins

### Your code start here ######

# Step 1: Read p and q from the console
p: float = float(input("Enter p: "))
q: float = float(input("Enter q: "))

# Step 2: Compute the area
pi = 3.14
radius = q / 2

area_2 = p * q
area_1 = (pi * (radius ** 2)) / 2
area_3 = area_1
total = area_1 + area_2 + area_3

# Step 3: Print out the result
print("The total area is", round(total, 3))