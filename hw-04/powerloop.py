# Assignment 4, Task 2
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 3 mins


def powerLoop(upto: int) -> None:
    for i in range(upto + 1):
        print(i, (7 ** i) % 97)
