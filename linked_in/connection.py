from datetime import date
class Connection:
    def __init__(self, user):
        self.user = user
        self.connection_date =  date.today()
