from datetime import datetime

class User:
   def __init__(self, id, created_at):
       self.id =  id(self)
       self.created_at = datetime.now()