# Assignment 06, Task 02
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: an hour


ENGLISH_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
NUMERICAL_DIGITS = "1234567890"
SPECIAL_CHARS = "$#@%!"


def has_repeating_chars(string):
    # no character or digit can appear three
    # times in a row
    chars_list = {}
    for char in string:
        normalised_char = char.lower()

        # Skip non alphabet characters
        if normalised_char not in ENGLISH_ALPHABET \
           and char not in NUMERICAL_DIGITS:
            continue

        if normalised_char not in chars_list.keys():
            chars_list[normalised_char] = 1
        else:
            chars_list[normalised_char] += 1

        if chars_list[normalised_char] > 2:
            return True

    return False


def passwordOK(password):
    """
    Conditions
    1. At least 1 lower-case letter (a-z);
    2. At least 1 numerical digit (0-9);
    3. At least 1 upper-case letter (A-Z);
    4. At least 1 special character from $#@%!
    5. Minimum length of password: 6
    6. Maximum length of password: 12
    7. No character or digit can appear three times in a row.
    """

    lower_case_letters = 0
    numerical_digits = 0
    upper_case_letters = 0
    special_characters = 0
    length = len(password)

    for char in password:
        if char in ENGLISH_ALPHABET.lower():
            lower_case_letters += 1
        if char in ENGLISH_ALPHABET.upper():
            upper_case_letters += 1
        if str(char) in NUMERICAL_DIGITS:
            numerical_digits += 1
        if char in SPECIAL_CHARS:
            special_characters += 1

    # Count conditions
    if (lower_case_letters < 1) or (numerical_digits < 1) \
       or (upper_case_letters < 1) or (special_characters < 1):
        return False

    # Length conditions
    if 6 > length > 12:
        return False

    # No character or digit can appear three times in a row
    if has_repeating_chars(password):
        return False

    return True


def test_passwordOK():
    # assert passwordOK('ABd1234@1') is True
    # assert passwordOK('f#9') is False
    assert passwordOK('Abbbc1!f') is False


test_passwordOK()
