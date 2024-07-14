def winner(records: [list[dict[str, int]]]) -> str:
    """
    Player with most wins in each match gets 1 point
    Two players will play a match against each other at most once
    Winner of tournament is player with most points
    """
    tournament_points = dict()

    for match in records:
        player_with_most_points = ""
        most_points = 0
        for player in match.keys():
            points = match[player]
            if points > most_points:
                player_with_most_points = player
                most_points = points

        if player_with_most_points in tournament_points.keys():
            tournament_points[player_with_most_points] += 1
        else:
            tournament_points[player_with_most_points] = 1

    points_all_same = True
    current_point = None
    if len(tournament_points) <= 1:
        points_all_same = False
    else:
        for key in tournament_points:
            points = tournament_points[key]
            if current_point is None:
                current_point = points
            elif current_point != points:
                points_all_same = False

    if points_all_same:
        print("returning empty")
        return ""

    # Get player with most points in the tournament
    player_with_most_points = None
    most_points = 0

    for player in tournament_points.keys():
        points = tournament_points[player]
        if points > most_points:
            most_points = points
            player_with_most_points = player

    print("returning", player_with_most_points)
    return player_with_most_points

def test_winner() -> None:
    # Chess
    assert winner([{'A': 2, 'B': 1}]) == 'A'
    assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}]) == ''
    assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}, {'B': 0, 'C': 3}]) == 'C'
    assert winner([{'A': 3, 'B': 0}, {'A': 1, 'C': 2}, {'B': 0, 'D': 3}, {'A': 2, 'D': 1}]) == 'A'
    assert winner([{'A': 3, 'B': 0}, {'B': 2, 'C': 1}, {'C': 2, 'D': 1}, {'A': 0, 'D': 3}]) == ''


test_winner()
