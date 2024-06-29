# Assignment 06, Task 01
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 15 minutes

ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def sort_dict(dict):
    # Sort by value
    # Lambda function taken from https://realpython.com/sort-python-dictionary/
    sorted_tuples = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    # Turn tuples back into dict
    sorted_dict = {}
    for sorted_tuple in sorted_tuples:
        sorted_dict[sorted_tuple[0]] = sorted_tuple[1]

    return sorted_dict


def charHistogram(filename: str) -> None:
    chars_list = {}
    with open(filename) as f:
        # Turn all characters into lowercase, then sort it
        # alphabetically. Required so that it would produce
        # the same order as the assignment's results

        contents = sorted(f.read().lower())

        for char in contents:
            # Skip non alphabet characters
            if char not in ENGLISH_ALPHABET:
                continue

            if char not in chars_list.keys():
                chars_list[char] = 1
            else:
                chars_list[char] += 1

    # Sort dictionary by descending frequency
    sorted_chars_list = sort_dict(chars_list)
    for char in sorted_chars_list:
        count = sorted_chars_list[char]
        print(char, "+" * count)


if __name__ == '__main__':
    charHistogram('textfile.txt')
