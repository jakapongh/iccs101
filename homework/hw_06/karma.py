# Assignment 06, Task 03
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 40 mins

def is_transfer(action):
    return "->" in action


def parse_name(action):
    if "->" in action:
        # src, dest
        return action.split("->")[0], action.split("->")[1]
    if "+" in action:
        return action.split("++")[0], "+"
    if "-" in action:
        return action.split("--")[0], "-"


def add_points(parsed_list: dict, name: str, operation: str):
    if name not in parsed_list.keys():
        if operation == "+":
            parsed_list[name] = 1
        elif operation == "-":
            parsed_list[name] = -1
    else:
        if operation == "+":
            parsed_list[name] += 1
        elif operation == "-":
            parsed_list[name] -= 1
    return parsed_list


def transfer(parsed_list, src_name: str, dest_name: str):
    # if one of them doesn't exist, do nothing
    if src_name not in parsed_list.keys() or dest_name not in parsed_list.keys():
        return False

    # transfer from person to person
    parsed_list[dest_name] += parsed_list[src_name]

    # Remove src from dict
    parsed_list.pop(src_name, None)

    return parsed_list


def keepTabs(actions: list[str]) -> dict[str, int]:
    parsed_list = {}
    for action in actions:
        if not is_transfer(action):
            name, operation = parse_name(action)
            add_points(parsed_list, name, operation)
        else:
            src_name, dest_name = parse_name(action)
            transfer(parsed_list, src_name, dest_name)

    return parsed_list


def test_keepTabs():
    actions = ["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff",
               "Jeff--", "June++", "Home->House"]
    assert keepTabs(actions) == {'Jeff': -2, 'June': 1, 'Jim': 2}


test_keepTabs()
