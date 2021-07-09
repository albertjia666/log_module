# -*- coding: utf-8 -*-
import logging
import os
import sys
from pythonjsonlogger import jsonlogger

class Log(object):

    def __init__(self, file_name=None, log_name=None):

        self.logger = logging.getLogger(name=file_name)
        self.logger.setLevel(level=logging.INFO)
        self.console_format = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s')
        self.file_format = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(filename)s %(lineno)d %(levelname)s %(message)s')
        self.log_dir = os.path.join(sys.path[0], 'logs', log_name)

        if not self.logger.handlers:
            # add a console handler
            ch = logging.StreamHandler()
            ch.setLevel(level=logging.INFO)
            ch.setFormatter(self.console_format)
            self.logger.addHandler(ch)

            # add a file handler
            fh = logging.FileHandler(filename=self.log_dir, encoding='utf-8')
            fh.setLevel(level=logging.INFO)
            fh.setFormatter(self.file_format)
            self.logger.addHandler(fh)

    def init_logger(self):
        return self.logger


if __name__ == '__main__':

    logger = Log(file_name=None, log_name='test.log').init_logger()

    logger.info('======[INFO TEST]======')
    logger.debug('======[DEBUG TEST]======')
    logger.warning('======[WARNING TEST]======')
    logger.error('======[ERROR TEST]======')
    logger.critical('======[CRITICAL TEST]======')

    # add extra key-value logs
    logger.info("PROGRESS", extra={"key": "value"})

