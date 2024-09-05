from profile import Profile
from post import Post
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.profile = None
        self.friends = []
        self.newsfeed = None
        self.posts = []


    def create_post(self, text=None, picture=None, video=None):
        post = Post(text, picture, video)
        self.posts.append(Post)


    def send_friend_request(self, user):
        pass

    def accept_friend_request(self, request):
        pass

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def get_profile_picture(self):
        return self.profile_picture

    def get_bio(self):
        return self.bio

    def get_friends(self):
        return self.friends

    def get_posts(self):
        return self.posts