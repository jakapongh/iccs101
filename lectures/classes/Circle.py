from __future__ import annotations
from math import pi as pi

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def distance_from(self, z: Point) -> float:
        a = self.x - z.x
        b = self.y - z.y
        return (a ** 2 + b ** 2) ** 0.5


class Circle:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        # pi r^2
        return pi * (self.radius ** 2)

    def inside(self, p: Point):
        """
        Calculate the distance from the point to the center of the circle.
        If is less than the radius of the circle the point is inside the circle.
        """
        center_point = Point(self.x, self.y)
        distance_from_origin = p.distance_from(center_point)
        if distance_from_origin <= self.radius:
            return True
        return False


if __name__ == '__main__':
    c = Circle(0, 0, 10)
    print(c.area())
