# Assignment 2, Task 5
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: about 2 hrs

p: int = int(input())
q: int = int(input())
r: int = int(input())
s: int = int(input())

one = min(p, q, r, s)
four = max(p, q, r, s)

"""
Explanation for myself
Getting the second largest value (three)

We have:
28, 13, 4, 10
p, q, r, s

How do we get the second largest number 13?
We test all possible combinations of p, q, r, s,
with one variable removed.

By removing one variable, the one that sticks
out/inconsistent with the rest is the combination
without the largest possible number.

Without the largest possible number, one
combination will return the second largest possible
number, and that's why it will stick out.

Therefore we test all possible combinations with only
three variables in each combination, and get the min()
of all of these combinations

max(p, q, r) -> max(28, 13, 4) = 28
max(q, r, s) -> max(13, 4, 10) = 13
max(r, s, p) -> max(4, 10, 28) = 28
max(s, p, q) -> max(10, 28, 13) = 28

min(28, 13, 28, 28) = 13
"""

three = min(max(p, q, r), max(q, r, s), max(r, s, p), max(s, p, q))

SUM = p + q + r + s
two = SUM - one - three - four

median = (two + three) / 2
print(median)

