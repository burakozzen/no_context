import logging
import sys
from typing import Any


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# __metaclass__=Singleton
class ApiLogger:
    def __init__(self, name: str = "ApiLogger", log_file_name: str = "api"):
        # get logger
        self.logger: logging.Logger = logging.getLogger(name=name)

        # create formatter
        self.__formatter: logging.Formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")
        self.__log_file_name: str = f"{log_file_name}.log"

        # add handlers to logger
        self.__add_handlers_to_logger()

        # set log-level
        # self.logger.setLevel(log_level)

    def __init_stream_handler(self) -> logging.StreamHandler:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(self.__formatter)
        return stream_handler

    def __init_file_handler(self) -> logging.FileHandler:
        file_handler = logging.FileHandler(filename=self.__log_file_name)
        file_handler.setFormatter(self.__formatter)
        return file_handler

    def __add_handlers_to_logger(self):
        stream_handler: logging.StreamHandler = self.__init_stream_handler()
        file_handler: logging.FileHandler = self.__init_file_handler()
        self.logger.handlers = [stream_handler, file_handler]

    def info(self, msg: Any):
        self.logger.setLevel(logging.INFO)
        self.logger.info(msg=msg)

    def warning(self, msg: Any):
        self.logger.setLevel(logging.WARNING)
        self.logger.info(msg=msg)
