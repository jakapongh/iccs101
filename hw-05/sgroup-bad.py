# Assignment 05, Task 06
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: --

# ! THIS DOESN'T EVEN WORK

def get_biggest_dists(data: list[int]):
    # Find all gaps
    idx = 0
    biggest_dists_idx = tuple()
    biggest_dists = None
    while idx < len(data):
        if (idx + 1) < len(data):
            distance = abs(data[idx] - data[idx + 1])

            if biggest_dists is None or distance > biggest_dists:
                biggest_dists = distance
                biggest_dists_idx = (idx, idx + 1,)

        idx += 1

    return biggest_dists, biggest_dists_idx


def separate(data: list[int], k: int) -> list[list[int]]:
    groups = None
    for passes in range(k):
        print("pass", passes)
        if groups is None:
            groups = []
            biggest_distance_pair, biggest_distance_pair_idx = get_biggest_dists(data)

            # Split based on indices of between biggest_distance_pair_idx

            new_list = []
            for (idx, item) in enumerate(data):
                print("inner")
                new_list.append(item)
                if (idx in biggest_distance_pair_idx and idx != biggest_distance_pair_idx[1]) or idx == (len(data) - 1):
                    groups.append(new_list)
                    new_list = []
        else:
            new_list = []
            for (idx, item) in enumerate(data):
                print("inner")
                new_list.append(item)
                if (idx in biggest_distance_pair_idx and idx != biggest_distance_pair_idx[1]) or idx == (len(data) - 1):
                    groups.append(new_list)
                    new_list = []

    print(groups)

    # print(biggest_distance_pair_idx, biggest_distance)


    return groups


def test_separate():
    # height_data = [71.4, 72.73, 74.36, 75.38, 76.15, 76.96, 79.51, 86.82, 87.81, 87.87, 146.38, 150.89,
    #                151.16, 152.18, 152.36, 153.27, 155.7, 160.99, 161.36, 164.5]
    # assert separate(height_data, k=2)

    arbitrary_data = [10, 12, 45, 47, 91, 98, 99]
    assert separate(data=arbitrary_data, k=3) == [[10, 12], [45, 47], [91, 98, 99]]



test_separate()
