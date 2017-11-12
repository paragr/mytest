__author__ = 'parag rajabhoj'

import os
import sys
import pickle
import functools
import time
import logging


def getLogHandler(vmId):
    """
        Creates a log handler for each vm based on vm id
    """
    print vmId
    log_dir_path = "summit.log"
    logger = logging.getLogger(str(vmId))
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        log_file = "summit.log"
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s : %(filename)s:%(lineno)s:%(funcName)s() -\t%(levelname)s - %(message)s')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
    return logger
