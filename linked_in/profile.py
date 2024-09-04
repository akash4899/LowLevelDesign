
class Profile:
    def __init__(self):
        self.picture = ""
        self.headline = ""
        self.summary = ""
        self.experience = []
        self.education = []
        self.skills = []

    def set_picture(self, picture):
        self.picture = picture

    def set_headline(self, headline):
        self.headline = headline

    def set_summary(self, summary):
        self.summary = summary


    def add_experience(self, experience):
        self.experience.append(experience)

    def add_education(self, education):
        self.education.append(education)

    def add_skill(self, skill):
        self.skills.append(skill)

