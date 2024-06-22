# data: list[dict[str, int]] = [
#     {
#         "student_id": 6380182,
#         "quiz_score": 26,
#     },
#     {
#         "student_id": 6380922,
#         "quiz_score": 25,
#     },
#     {
#         "student_id": 6380727,
#         "quiz_score": 96,
#     },
# ]

data: dict[int, int] = {
    6380182:26,
    6380922:25,
    6380727:96,
}


def find_avg(d: dict[int, int]) -> float:
    sum = 0
    for key in d:
        sum += d[key]
    return (sum / len(d))


print(find_avg(data))
