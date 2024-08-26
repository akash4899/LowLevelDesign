class Message:
    def __init__(self, message):
        self.id = id(self)
        self.content = message

    def get_message(self):
        return self.content