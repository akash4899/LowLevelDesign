from log import Log


class OutputDestination:
    def __init__(self, name):
        self.logs = []
        self.name = name

    def add_log(self, log: Log):
        self.logs.append(log)

    def show_logs(self):
        for log in self.logs:
            print(f"{log.log_level} {log.timestamp}  {log.message}")
