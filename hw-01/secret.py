# Assignment 1, Task 6
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 10 minutes

### Your code start here ######

# Step 1: Read the secret key from the console
M: float = (25 * 1502)**(257+123) + (98 * 34) ** (981-813)
k: int = int(input("Enter secret key: "))

# Step 2: Compute the secret code
M_STR: str = str(M)
a: str = M_STR[k - 1]
b: str = M_STR[len(M_STR) - k]
secret_code: str = str(a) + str(b)

# Step 3: Print out the result
print("The secret code is", int(str(b + a)))