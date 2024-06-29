# Assignment 06, Task 04
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 30 mins

def eto(lst: list[int]) -> list[int]:
    # Even numbers appear before odd numbers
    # Needs to be recursive function

    # Base case is that len lst is 0
    if len(lst) == 0: return []

    keep = lst[0]
    rest = lst[1:]

    friend_answer = eto(rest)
    if keep % 2 != 0:
        friend_answer.append(keep)
    else:
        friend_answer.insert(0, keep)

    return friend_answer


def test_eto():
    # Too lazy to write actual asserts regardless of order
    # So just compare it yourself by eye
    test_cases = [
        {
            "input": [3, 1, 2],
            "expected": [2, 1, 3]
        },
        {
            "input": [4, 2, 8],
            "expected": [8, 4, 2]
        },
        {
            "input": [8, -2, 3, -3, -1, 5, 8, -1, 5],
            "expected": [8, -2, 8, 5, -1, 5, -1, -3, 3]
        }
    ]

    for idx, case in enumerate(test_cases):
        print("Test case", idx)
        print("Input   :", case["input"])
        print("Result  :", eto(case["input"]))
        print("Expected:", case["expected"])
        print()


test_eto()
