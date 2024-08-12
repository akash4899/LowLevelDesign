class Note:
    def __init__(self, value):
        self.value = value
        self.quantity = 0

    def decrease(self, required):
        if required < self.quantity:
            return f"Not enough number of notes available of {self.value}"
        else:
            self.quantity -= required
            return f"Number of notes left of {self.value}Rs: {self.quantity}"

    def add(self, quantity):
        self.quantity += quantity