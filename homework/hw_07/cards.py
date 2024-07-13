# Assignment 07, Task 02
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: -

Hand = set[tuple[str, str]]


def has_rank(hand_haystack: Hand, rank_needle) -> bool:
    for card in hand_haystack:
        suit, rank = card
        if rank == rank_needle:
            return True
    return False


def get_card_rank(card):
    return card[1]


def sort_hand_by_rank(hand: Hand) -> list:
    return sorted(hand, key=get_card_rank, reverse=True)


def has_ace(hand: list) -> bool:
    for card in hand:
        suit, rank = card
        if rank == 'Ace':
            return True
    return False


def is_straight_flush(hand: Hand) -> bool:
    """
    a straight flush is a hand that contains
    five cards in sequence, all the same suit
    CAUTION: The ace can either be the highest
    or the lowest in the sequence
    """

    if len(hand) < 5:
        return False

    sorted_hand = sort_hand_by_rank(hand)
    first_card = sorted_hand[0]
    print(sorted_hand)

    for card in sorted_hand:
        suit, rank = card

        # If suit differs from first suit
        if suit != first_card[0]:
            return False

        return True

    hand_has_ace = has_ace(sorted_hand)

    # Check if rank ascending or descending
    # First card is lower than second card
    ascending = first_card[1] < sorted_hand[1][1]


def is_four_of_a_kind(hand: Hand) -> bool:
    """
    a hand that contains all four cards of one rank
    and any other card
    """
    pass


def is_full_house(hand: Hand) -> bool:
    """
    a hand that contains three matching cards of one
    rank and two matching cards of another rank
    """
    pass


def is_two_pair(hand: Hand) -> bool:
    """
    contains two cards of the same rank, plus two cards
    of another rank that match each other but not the first pair
    """
    pass



'''
A hand has exactly 5 cards.
Hands compared using a ranking system
Player who has highest-ranking hand wins
'''


def test():
    assert is_straight_flush({
        ('Spade', '5'),
        ('Spade', '4'),
        ('Spade', '3'),
        ('Spade', '2'),
        ('Spade', 'Ace')
    }) is True


test()
