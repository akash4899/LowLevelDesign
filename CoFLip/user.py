from  enum import Enum

class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    NONBINARY = 'Non-binary'

class User:
    def __init__(self, name, gender, preferred_vaccine_type):
        self.name = name
        self.gender = gender
        self.preferred_vaccine_type = preferred_vaccine_type
