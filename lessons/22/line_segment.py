class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    @property
    def dx(self):
        return self.end.x - self.start.x

    @property
    def dy(self):
        return self.end.y - self.start.y

    def slope(self):
        # Rise over run
        return self.dy / self.dx

    def length(self):
        # Compute length of segment
        # a^2 + b^2 = c^2
        a_squared = self.dy ** 2
        b_squared = self.dx ** 2
        c_squared = a_squared + b_squared
        return c_squared ** 0.5


def main():
    segment = LineSegment(Point(1, 1), Point(3, 2))
    print("Slope:", segment.slope())
    print("Length:", segment.length())


if __name__ == '__main__':
    main()
