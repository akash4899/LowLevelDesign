from output_destination import OutputDestination

class LoggerConfig:
    def __init__(self, log_level, output_destination: OutputDestination):
        self.log_level = log_level
        self.output_destination = output_destination

    def get_log_level(self):
        return self.log_level

    def set_log_level(self, log_level):
        self.log_level = log_level

    def get_output_destination(self):
        return self.output_destination

    def set_output_destination(self, output_destination):
        self.output_destination = output_destination