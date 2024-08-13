
from datetime import date

class Comment:
    def __init__(self, user, content):
        self.id = id(self)
        self.content = content
        self.author = user
        self.created_at = date.today()
