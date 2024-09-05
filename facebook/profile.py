
class Profile:
    def __init__(self, picture=None, bio=None, interests=None):
        self.picture = picture
        self.bio = bio
        self.interests = interests

    def update_picture(self, picture):
        self.picture = picture

    def update_bio(self, bio):
        self.bio = bio

    def update_interests(self, interests):
        self.interests = interests