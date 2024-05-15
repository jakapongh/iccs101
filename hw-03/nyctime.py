# Assignment 3, Task 6
# Name: Jakapong Hemla
# Collaborators: None
# Time Spent: 5 mins


# Convert Bangkok time to NY time
def nycHour(hour: int) -> str:
    hour_24 = hour

    # Special case where [00]:00 is technically [24]:00
    if hour == 0:
        hour_24 = 24

    # If hour_24 is less than 12, if we subtract 11 right away
    # it will result in a negative number, (as it's technically
    # converting the hours to the day before)
    # By adding 24, this wouldn't happen, and it would still give us
    # the correct hour number when we subtract it by 11.
    if hour_24 < 12:
        hour_24 += 24

    # NY is 11 hours behind Bangkok
    hour_24 -= 11

    hour_12 = None
    suffix = None

    if hour_24 == 24:
        # 24:00 is 12am
        hour_12 = 12
        suffix = "am"
    elif hour_24 < 12:
        # 24 hr is same as 12 hr as hour_24 < 12
        hour_12 = hour_24
        suffix = "am"
    else:
        # Convert 24 hours into 12 hours as hour_24 > 12
        hour_12 = hour_24 - 12
        suffix = "pm"

    # Special case where 0 is actually 12pm
    if hour_12 == 0:
        hour_12 = 12

    return str(hour_12) + suffix


def test_nycHour():
    # Assignment test cases
    assert nycHour(0) == "1pm"
    assert nycHour(11) == "12am"
    assert nycHour(23) == "12pm"
    assert nycHour(17) == "6am"
    assert nycHour(5) == "6pm"

    # All possible test cases
    assert nycHour(0) == "1pm"
    assert nycHour(1) == "2pm"
    assert nycHour(2) == "3pm"
    assert nycHour(3) == "4pm"
    assert nycHour(4) == "5pm"
    assert nycHour(5) == "6pm"
    assert nycHour(6) == "7pm"
    assert nycHour(7) == "8pm"
    assert nycHour(8) == "9pm"
    assert nycHour(9) == "10pm"
    assert nycHour(11) == "12am"
    assert nycHour(12) == "1am"
    assert nycHour(13) == "2am"
    assert nycHour(14) == "3am"
    assert nycHour(15) == "4am"
    assert nycHour(16) == "5am"
    assert nycHour(17) == "6am"
    assert nycHour(18) == "7am"
    assert nycHour(19) == "8am"
    assert nycHour(20) == "9am"
    assert nycHour(21) == "10am"
    assert nycHour(22) == "11am"
    assert nycHour(23) == "12pm"


test_nycHour()
