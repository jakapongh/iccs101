# Assignment 05, Task 04
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 20 mins

# Helpers
def parse_time(line: str) -> int:
    line = line.replace("time:", "")
    split_line = line.split(";")
    split_time = split_line[1].split(",")

    minutes = int(split_time[0])
    seconds = int(split_time[1])
    return (minutes * 60) + seconds


def parse_dist(line: str) -> float:
    line = line.replace("distance:", "")
    split_line = line.split(";")
    return float(split_line[2])


def jogging_average(activities: list[str]) -> float:
    jogging_activities = []

    total_km = 0
    total_seconds = 0

    for line in activities:
        split_line = line.split(';')

        if split_line[0] != 'jogging':
            continue

        total_km += parse_dist(line)
        total_seconds += parse_time(line)

    avg_speed_metres_per_sec = round((total_km * 1000) / total_seconds, 7)
    return avg_speed_metres_per_sec


def test_parse_time():
    assert parse_time('jogging;time:40,11;distance:6') == 2411
    assert parse_dist('jogging;time:40,11;distance:7.1') == 7.1


def test_jogging_average():
    log_book = [
        "cycling;time:1,49;distance:2",
        "jogging;time:40,11;distance:6",
        "swimming;time:1,49;distance:1.2",
        "jogging;time:36,25;distance:5.3",
        "hiking;time:106,01;distance:8.29"
    ]
    assert jogging_average(log_book) == 2.4586597


test_parse_time()
test_jogging_average()
