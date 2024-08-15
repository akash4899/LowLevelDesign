from logging_framework import LoggingFramework
from file import File
from database import Database
from console import Console
from logger_config import LoggerConfig
from log_level import LogLevel


class Demo:
    @staticmethod
    def run():
        print('here')
        logger = LoggingFramework.get_instance()

        logger.info("This is an information message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")

        # Changing log level and appender
        config = LoggerConfig(LogLevel.DEBUG, File("app.log"))
        logger.set_config(config)

        logger.debug("This is a debug message")
        logger.info("This is an information message")

if __name__ == "__main__":
    Demo.run()


