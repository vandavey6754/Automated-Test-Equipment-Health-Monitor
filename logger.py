import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok = True)

    logging.basicConfig(
        #basicConfig() is a function that belongs to logging module
        filename = "logs/monitor.log",
        level = logging.INFO,
        #.INFO is a constant defined in the logging module
        format = "%(asctime)s - %(levelname)s - %(message)s"
        #%(asctime)s is part of the logging format string system,
        #logging module uses placeholders like :%(something)s
        #what format is = to tells python:
        #insert timestamp, insert log level, insert message
    )

    return logging