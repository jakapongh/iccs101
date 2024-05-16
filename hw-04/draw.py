# Assignment 4, Task 3
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 50 minutes

def triangle_generator(k: int, base: bool = True, inverse: bool = False):
    # We need to find the base size in order to find how
    # many pound signs we need on each side of the
    # asterisks
    base_size = 2 * k - 1

    if not inverse:
        # Normal, smallest at top
        it_range = range(k + 1)
    else:
        # Inverse, biggest at top
        it_range = range(k, 0, -1)

    for x in it_range:
        # Skip last iteration when we don't want the
        # base of the triangle (only used for diamond)
        if not base and x == k:
            continue

        asterisks = 2 * x - 1
        if asterisks > 0:
            total_pounds_needed = base_size - asterisks
            pounds_on_each_side = total_pounds_needed // 2
            print("#" * pounds_on_each_side, end="")
            print("*" * asterisks, end="")
            print("#" * pounds_on_each_side, end="")

        if x != k and x != 0:
            # Only print newline when it's not the last
            # sequence
            print("")


def triangle(k: int) -> None:
    triangle_generator(k)


def diamond(k: int) -> None:
    """
    A diamond consists of a triangle without the
    base and the inverse/reflection of that triangle,
    also without the base.

                          /\
                         /  \
                        /    \
                        -------
                        \    /
                         \  /
                          \/

    """

    # Generate triangle with no base
    triangle_generator(k + 1, base=False)

    # Generate inverse of triangle with no base
    triangle_generator(k + 1, base=False, inverse=True)

    # Why do I have to do k + 1 to generate the correct size of
    # the diamond, I don't know, but it works??
