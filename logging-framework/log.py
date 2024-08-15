from datetime import datetime

class Log:
    def __init__(self, log_level, message):
        self.timestamp = datetime.now()
        self.log_level = log_level
        self.message = message