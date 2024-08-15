from threading import Lock
from file import File
from console import Console
from database import Database
from log import Log
from log_level import LogLevel
from logger_config import LoggerConfig

class LoggingFramework:
    _instance = None
    _lock = Lock()

    def __init__(self):
        if LoggingFramework._instance is None:
            LoggingFramework._instance = self
            self.config = LoggerConfig(LogLevel.INFO, Console('Linux Console'))
        else:
            return "This is a singleton class and an object is already created"

    @classmethod
    def get_instance(cls):
        if LoggingFramework._instance is None:
            LoggingFramework()
        return LoggingFramework._instance

    def set_config(self, config):
        self.config = config




    def log(self, log_level, message):
        if log_level == self.config.get_log_level():
            log_message = Log(log_level, message)
            self.config.get_output_destination().add_log(log_message)

    def debug(self, message):
        self.log(LogLevel.DEBUG, message)

    def info(self, message):
        self.log(LogLevel.INFO, message)

    def warning(self, message):
        self.log(LogLevel.WARN, message)

    def error(self, message):
        self.log(LogLevel.ERROR, message)

    def fatal(self, message):
        self.log(LogLevel.FATAL, message)





