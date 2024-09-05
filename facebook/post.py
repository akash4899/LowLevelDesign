from privacy import Privacy
class Post:
    def __init__(self, text=None, picture=None, video=None, privacy=Privacy.PUBLIC):
        self.text = text
        self.picture = picture
        self.video = video
        self.likes = 0
        self.comments = []
        self.privacy = privacy

    def add_like(self):
        self.likes += 1

    def reduce_like(self):
        self.likes -= 1

    def add_picture(self, picture):
        self.picture = picture

    def add_comment(self, comment):
        self.comments.push(comment)

    def add_text(self, text):
        self.text = self.text + text

    def get_likes(self):
        return self.likes

    def get_comments(self):
        return [comment for comment in self.comments]
