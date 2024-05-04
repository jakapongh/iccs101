# Assignment 2, Task 7
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 21 minutes

# only: boolean ops., numerical comp, abs()
# check if triangle is right-angled

def avg(a: float, b: float) -> float:
    return (a + b) / 2


def dist_midpoint(a: float, b: float) -> float:
    return abs(a - b) / 2


def get_longer(a: float, b: float) -> float:
    # same concept as previous task minmax.py
    return avg(a, b) + dist_midpoint(a, b)


def get_smaller(a: float, b: float) -> float:
    # same concept as previous task minmax.py
    return avg(a, b) - dist_midpoint(a, b)


x: float = float(input())
y: float = float(input())
z: float = float(input())

# Get longest of all possible combinations of x, y, z
longest_side: float = get_longer(get_longer(get_longer(x, y), get_longer(x, z)), get_longer(y, z))

# Get smallest of all possible combinations of x, y, z
side_1: float = get_smaller(get_smaller(get_smaller(x, y), get_smaller(x, z)), get_smaller(y, z))

SUM_OF_ALL_SIDES: float = x + y + z
side_2: float = SUM_OF_ALL_SIDES - longest_side - side_1

hyp = longest_side ** 2
a_squared_b_squared_sum = side_1 ** 2 + side_2 ** 2

THRESHOLD = 1e-7
is_right_angled = abs(hyp - a_squared_b_squared_sum) < THRESHOLD
print(is_right_angled)
