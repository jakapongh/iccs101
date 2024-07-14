# Assignment 07, Task 04
# Name: Jakapong Hemla
# Collaborators: -
# Time Spent: 1 hour

BID_INCREMENT = 1.5


def validate_bid_instance(inst):
    if not isinstance(inst, Bid):
        raise TypeError


class Bid:
    def __init__(self, bid_id, bidder_id, auction):
        self.bid_id = bid_id
        self.bidder_id = bidder_id
        self.auction = auction

    def __str__(self):
        return f'Bid ID: {self.bid_id}, Bidder ID: {self.bidder_id}, Auction: {self.auction}'

    def __repr__(self):
        return f'Bid(bid_id={self.bid_id}, bidder_id={self.bidder_id}, auction={self.auction})'

    def __lt__(self, other):
        """
        less than, compares only bid_id
        """
        validate_bid_instance(other)
        return int(self.bid_id) < int(other.bid_id)

    def __lte__(self, other):
        """
        less than or equal to, compares only bid_id
        """
        validate_bid_instance(other)
        return int(self.bid_id) <= int(other.bid_id)

    def __gt__(self, other):
        """
        greater than, compares only bid_id
        """
        validate_bid_instance(other)
        return int(self.bid_id) > int(other.bid_id)

    def __gte__(self, other):
        """
        greater or equal than, compares only bid_id
        """
        validate_bid_instance(other)
        return int(self.bid_id) >= int(other.bid_id)

    def __eq__(self, other):
        """
        equality
        """
        validate_bid_instance(other)
        return self.bid_id == other.bid_id


class Auction:
    def __init__(self, auction_id):
        self.auction_id = auction_id
        self.price = 0
        self.winner = None

    def __str__(self):
        return f'Auction id: {self.auction_id}, current price: {self.price}, winner: {self.winner}'

    def __repr__(self):
        return f'Auction(auction_id={self.auction_id}, current_price={self.price}, winner={self.winner})'

    def placeBid(self, bidder_id):
        self.price += BID_INCREMENT
        # Winner will always be the last bid placed
        self.winner = bidder_id


def CSV2List(csvFilename: str) -> list[Bid]:
    """
    Custom CSV parser that returns sorted instances of Bid
    """
    # Custom CSV Parser
    bid_instances = []
    with open(csvFilename, 'r') as csvfile:
        for idx, line in enumerate(csvfile):
            if idx == 0:
                # Skip header
                continue
            # Strip \n
            line = line.strip()
            parts = line.split(',')
            new_bid = Bid(parts[0], parts[1], parts[2])
            bid_instances.append(new_bid)
    return sorted(bid_instances)


def mostPopularAuction(bidList: list[Bid]) -> set[str]:
    """
    Input: list of Bid instances
    Returns: set of identifiers (string) of the most popular auctions
    (which is the auction with the most distinct number of bidders), there
    can be more than one or more of these bids that match this criteria.
    """
    # Count all auctions
    auctions_count = dict()
    biggest_count = 0
    for bid in bidList:
        # Increment count
        if bid.auction not in auctions_count.keys():
            auctions_count[bid.auction] = 1
        else:
            auctions_count[bid.auction] += 1

        # Update the biggest count
        if auctions_count[bid.auction] > biggest_count:
            biggest_count = auctions_count[bid.auction]

    # Get all the auctions with this same "biggest_count"
    biggest_keys = set()
    for key in auctions_count.keys():
        auction_count = auctions_count[key]
        if auction_count == biggest_count:
            biggest_keys.add(key)

    return biggest_keys


def auctionWinners(bidList: list[Bid]) -> dict[str, Auction]:
    """
    Input: list of Bid instances
    Returns: dict
    """
    auctions = dict()
    for bid in bidList:
        # Prevent creating multiple auctions that may
        # already have been created
        if bid.auction not in auctions.keys():
            new_auction = Auction(bid.auction)
            auctions[bid.auction] = new_auction
        auctions[bid.auction].placeBid(bid.bidder_id)

    return auctions


if __name__ == '__main__':
    bid_list = CSV2List('sample_bids.csv')
    most_popular = mostPopularAuction(bid_list)
    auction_winners = auctionWinners(bid_list)
    print(most_popular)
    print(auction_winners)