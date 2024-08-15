from output_destination import OutputDestination
from log import Log

class File(OutputDestination):
    def __init__(self, name):
        super().__init__(name)

    def add_log(self, log: Log):
        self.logs.append(log)
        print("log uploaded to a file.")