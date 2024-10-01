class User:
    def __init__(self, id, email, username):
        self.id = id
        self.username = username
        self.auction_listings = []
        self.email = email

    def add_auction_listing(self, auction_listing):
        self.auction_listings.append(auction_listing)