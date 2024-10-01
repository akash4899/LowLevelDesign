from threading import Lock
from auction_status import AuctionStatus
class AuctionListing:
    def __init__(self, id, item_name, description, starting_price, closing_price, auction_duration):
        self.id = id
        self.item_name = item_name
        self.description = description
        self.starting_price = starting_price
        self.auction_duration = auction_duration
        self.current_highest_bid = None
        self.bids = []
        self.current_bidder = None
        self.status = AuctionStatus.ONGOING
        self._lock = Lock()
        self.closing_price = closing_price

    def place_bid(self, bid):
        with self._lock:
            if self.status == AuctionStatus.ONGOING:
                if bid.amount > self.starting_price and (self.current_highest_bid == None or bid.amount > self.current_highest_bid.amount ) and bid.amount<self.closing_price:
                    self.bids.append(bid)
                    self.current_highest_bid = bid
                    self.current_bidder = bid.bidder
                    self.notify_observers()

    def close_auction(self):
        with self.lock:
            if self.status == AuctionStatus.ACTIVE:
                self.status = AuctionStatus.CLOSED
                self.notify_observers()


    def notify_observers(self):
        pass
                    
