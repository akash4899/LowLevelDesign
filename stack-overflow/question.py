from vote import Vote
from datetime import date
from tag import Tag


class Question:
    def __init__(self, user, title, content, tag_names):
        self.id = id(self)
        self.title = title
        self.content = content
        self.author = user
        self.tags = [Tag(tag_name) for tag_name in tag_names]
        self.votes = []
        self.comments = []
        self.answers = []
        self.created_at = date.today()

    def add_answer(self, answer):
        if answer not in self.answers:
            self.answers.append(answer)

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
