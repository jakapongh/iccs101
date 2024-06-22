# Assignment 2, Task 1
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 20 mins


def split_segments(string: str, nth: int) -> list[str]:
    segments = []
    collector = ""
    nth_len = len(string) / nth

    for i in range(len(string)):
        collector += string[i]
        if (i + 1) % nth_len == 0:
            segments.append(collector)
            collector = ""

    return segments


def concat_array_to_str(arr: list):
    concated = ""
    for item in arr:
        concated += item
    return concated

s = input()
t = input()

s = s.lower()
t = t.upper()

s_replacements: list[str] = ['s', 'l', 'a']
t_replacements: list[str] = ['P', 'O', 'I', 'N']

for original in s_replacements:
    s = s.replace(original, 'm')

for original in t_replacements:
    t = t.replace(original, 'T')

s_first_char: str = s[0]
t_first_char: str = t[0]

# Trim first letter of the var
# and add first_char of the opposite var
s = t_first_char + s[1:]
t = s_first_char + t[1:]

# Split strings into 1/3 segments
s_segments: list[str] = split_segments(s, 3)
t_segments: list[str] = split_segments(t, 3)

s_last_segment = s_segments[-1]
t_middle_segment = t_segments[len(t_segments) // 2]

# Replace last of s with middle of t
s_segments[-1] = t_middle_segment

# Reconstruct str from segments
s = concat_array_to_str(s_segments)
t = concat_array_to_str(t_segments)

z: str = s + t
print(z)
