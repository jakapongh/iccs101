# Assignment 05, Task 06
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: like 2 days


def separate(data, k):
    # Special case
    if k == 1: return data

    groups = []
    segments = [(0, len(data) - 1)]

    while len(segments) < k:
        biggest_gap = 0
        max_index = -1
        segment_to_split = None

        for (start, end) in segments:
            # Find the biggest gap within this segment
            for i in range(start, end):
                current_gap = data[i + 1] - data[i]
                if current_gap > biggest_gap:
                    biggest_gap = current_gap
                    max_index = i
                    segment_to_split = (start, end)

        # Split the segment with the largest gap
        start, end = segment_to_split
        segments.remove(segment_to_split)
        segments.append((start, max_index))
        segments.append((max_index + 1, end))

    segments.sort()

    # From segments, create each group
    for start, end in segments:
        groups.append(data[start:end + 1])

    return groups


def test_separate():
    assert separate([10, 12, 45, 47, 91, 98, 99], 3) == [[10, 12], [45, 47], [91, 98, 99]]


test_separate()
