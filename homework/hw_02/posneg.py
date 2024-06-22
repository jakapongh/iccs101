# Assignment 2, Task 2
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 10 mins


a: int = int(input())
b: int = int(input())
negative: bool = input().lower() == 'true'

result = (not negative and ((a < 0 and b > 0) or (a > 0 and b < 0))) \
         or (negative and a < 0 and b < 0)

print(result)
