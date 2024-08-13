
from datetime import date
from vote import Vote

class Answer:
    def __init__(self, user, question, content):
        self.id = id(self)
        self.content = content
        self.author = user
        self.question = question
        self.comments = []
        self.votes = []
        self.created_at = date.today()
        self.accepted = False

    def add_comment(self, comment):
        self.comments.append(comment)

    def vote(self, user, value):
        if value not in [1, -1]:
            raise ValueError("Vote must be either 1 or -1.")
        self.votes = [v for v in self.votes if v.user != user]
        self.votes.append(Vote(user, value))
        self.author.update_reputation(value * 5)

    def get_vote_count(self):
        return sum(v.value for v in self.votes)

    def get_comments(self):
        return self.comments.copy()

    def accept(self):
        if self.accepted:
            raise ValueError("The answer is already accepted.")
        self.accepted = True
        self.author.update_reputation(15)
