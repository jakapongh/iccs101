# Assignment 2, Task 3
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 20 mins


st: str = input()
k: int = int(input())

mod: int = k % len(st)

end_only: str = st[len(st) - mod:]
without_end: str = st[:len(st) - mod]

print(end_only + without_end)
