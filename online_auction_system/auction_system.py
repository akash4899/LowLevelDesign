from threading import Lock


class AuctionSystem:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls.users = {}
                cls.listings = {}

        return cls._instance

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    def add_user(self, user):
        self.users[user.id] = user

    def add_listing(self, listing):
        self.listings[listing.id] = listing

    def search_auction_listing(self, keyword):
        return [listing for listing in self.listings.values() if keyword.lower() in listing.item_name.lower()]

    def place_bid(self, listing_id, bid):
        listing = self.listings.get(listing_id)
        if listing:
            listing.place_bid(bid)
