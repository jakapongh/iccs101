# Assignment 2, Task 6
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 7 mins

# boolean and numerical comparisons only

hour: int = int(input())
minute: int = int(input())
meowing: bool = input().lower() == 'true'

in_morning = hour <= 6 and minute < 30
at_night = hour >= 21 and minute > 0
trouble = (in_morning and meowing) or (at_night and meowing)

print(trouble)