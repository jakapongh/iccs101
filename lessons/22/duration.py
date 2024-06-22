class Duration:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss

    def __str__(self):
        return f'{self.hh} hour {self.mm} min {self.ss} sec'

    def __repr__(self):
        return f'Duration(hh={self.hh}, mm={self.mm}, ss={self.ss})'

    # Support for Duration() + Duration()
    def __add__(self, other):
        result = Duration(self.hh, self.mm, self.ss)
        result.hh += other.hh
        result.mm += other.mm
        result.ss += other.ss
        return result

    # Support for Duration() += Duration()
    def __iadd__(self, other):
        if isinstance(other, Duration):
            self.hh += other.hh
            self.mm += other.mm
            self.ss += other.ss
        else:
            raise TypeError("Other must be of type Duration")
        return self

    def to_secs(self):
        total_secs = 0
        total_secs += self.hh * 60 * 60
        total_secs += self.mm * 60
        total_secs += self.ss
        return total_secs

    # Support for < operator
    def __lt__(self, other):
        return self.to_secs() < other.to_secs()

    # Support for > operator
    def __gt__(self, other):
        return self.to_secs() > other.to_secs()

    # Support for <= operator
    def __le__(self, other):
        return self.to_secs() <= other.to_secs()

    # Support for >= operator
    def __ge__(self, other):
        return self.to_secs() >= other.to_secs()

    def __eq__(self, other):
        return self.to_secs() == other.to_secs()

    def is_shorter(self, other):
        return self < other


def main():
    # __add__
    a = Duration(0, 0, 10)
    b = Duration(0, 0, 50)
    print("Duration a:", a)
    print("Duration b:", b)
    print("Sum of two durations: ", a + b)

    print()

    # Greater than less than: __lt__, __gt__
    print("a is shorter than b:", a.is_shorter(b))
    print("b is shorter than a:", b.is_shorter(a))

    print()

    # Equality
    print("a == b:", a == b)

    print()

    # __iadd__
    a += b
    print("a += b:", a)


if __name__ == '__main__':
    main()
