# Assignment 07, Task 02
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 2 days

Hand = set[tuple[str, str]]


def has_rank(hand_haystack: Hand, rank_needle) -> bool:
    # check if hand contains card of rank rank_needle
    for card in hand_haystack:
        rank = card[1]
        if rank == rank_needle:
            return True
    return False


def get_card_rank(card):
    # convert card rank to numerical value for sort function below
    ranks = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3,
             '2': 2}
    if card[1] in ranks:
        return ranks[card[1]]
    return 0  # return 0 if rank not found (shouldn't happen with valid input)


def sort_hand_by_rank(hand: Hand) -> list:
    # sort hand by card descending
    return sorted(hand, key=get_card_rank, reverse=True)


def is_straight_flush(hand: Hand) -> bool:
    # hand that contains five cards in sequence, all of the same suit.
    # ace can be either the highest or the lowest in the sequence.
    if len(hand) != 5:
        return False

    sorted_hand = sort_hand_by_rank(hand)
    suits = set()
    for card in sorted_hand:
        suit = card[0]
        suits.add(suit)

    # check if all cards have the same suit
    if len(suits) != 1:
        return False

    ranks = []
    for card in sorted_hand:
        ranks.append(get_card_rank(card))

    # special case: A, 5, 4, 3, 2
    if ranks == [14, 5, 4, 3, 2]:
        return True

    # check ranks are in sequence
    for i in range(4):
        # comp. each rank with the next rank in the sequence
        if ranks[i] - ranks[i + 1] != 1:
            # diff between two consecutive ranks is not 1,
            # it's not a straight flush
            return False

    # all ranks are in sequence
    return True


def is_four_of_a_kind(hand: Hand) -> bool:
    # hand that contains all four cards of one rank and any other card
    if len(hand) != 5:
        return False

    rank_counts = {}
    for card in hand:
        rank = card[1]
        # count occurrences of each rank
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    # check if any rank appears exactly 4 times
    for count in rank_counts.values():
        if count == 4:
            return True
    return False


def is_full_house(hand: Hand) -> bool:
    # contains three matching cards of one rank and two matching cards of another rank
    if len(hand) != 5:
        return False

    rank_counts = {}
    for card in hand:
        rank = card[1]
        # count occurrences of each rank
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    has_three = False
    has_two = False
    for count in rank_counts.values():
        if count == 3:
            has_three = True
        elif count == 2:
            has_two = True
    # full house requires both a three-of-a-kind and a pair
    return has_three and has_two


def is_two_pair(hand: Hand) -> bool:
    # contains two cards of the same rank, plus two cards of another rank that match each other
    # but not the first pair, plus any card not of either pair.
    if len(hand) != 5:
        return False

    rank_counts = {}
    for card in hand:
        rank = card[1]
        # count occurrences of each rank
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1

    # count number of pairs
    pairs = 0
    for count in rank_counts.values():
        if count == 2:
            pairs += 1
    # two pair requires exactly two pairs
    return pairs == 2


def test():
    assert is_straight_flush({
        ('Spade', 'A'),
        ('Spade', '5'),
        ('Spade', '4'),
        ('Spade', '3'),
        ('Spade', '2')
    }) is True

    assert is_four_of_a_kind({
        ('Club', '3'),
        ('Spade', '3'),
        ('Diamond', '3'),
        ('Heart', '3'),
        ('Heart', 'J')
    }) is True

    assert is_full_house({
        ('Club', '4'),
        ('Spade', '4'),
        ('Diamond', '4'),
        ('Heart', '7'),
        ('Spade', '7')
    }) is True

    assert is_two_pair({
        ('Heart', '9'),
        ('Club', '9'),
        ('Spade', '4'),
        ('Club', '4'),
        ('Club', '10')
    }) is True


test()
