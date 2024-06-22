# Assignment 2, Task 4
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 25 mins


# GOAL: print whatever value is the smallest
"""
Explanation for myself
---
a = 1
b = 2
Average of two numbers is the midpoint between a and b
in this case, it is A = 1.5

We are currently in the middle A.
    - We can "go to the left" (subtract) to go back to the
    starting position (min number)
    - We can "go to the right" (addition) to go to the maximum
    position (max number).

Question is how far do we go back?
    - We can find the distance D, between the two numbers, and
    divide it by two to find the midpoint, M_d of the distance.

That is how far we have to move to either go to back the
start or go forwards to the max.

Therefore, A + M_d brings us to the maximum position
and A - M_d brings us to the minimum position.
"""

a: int = int(input())
b: int = int(input())

first = None
second = None

D = abs(a - b)
mid = D / 2

avg = ((a + b) / 2)
bigger_num = int(avg + mid)
smaller_num = int(avg - mid)

print(smaller_num, bigger_num)
