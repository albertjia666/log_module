import logging
import os.path
import time
import sys
from colorama import Fore, Style


class MyLogger(object):

    def __init__(self, logger_c, logger_f, log_name):

        self.logger_c = logging.getLogger(name=logger_c) # 定义对应的程序模块名name，默认是root
        self.logger_c.setLevel(level=logging.DEBUG) # 指定最低的日志级别 critical > error > warning > info > debug

        self.logger_f = logging.getLogger(name=logger_f)
        self.logger_f.setLevel(level=logging.DEBUG)

        log_time = time.strftime("%Y-%m-%d:%H-%M-%S", time.localtime(time.time()))
        log_name = os.getcwd() + "/logs/" + log_name + ".log"

        formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(message)s")

        if not self.logger_c.handlers:

            self.ch = logging.StreamHandler(stream=sys.stdout) # 日志输出到屏幕控制台
            self.ch.setLevel(level=logging.DEBUG) # 设置日志等级
            self.ch.setFormatter(fmt=formatter)
            self.logger_c.addHandler(self.ch)

        if not self.logger_f.handlers:

            self.fh = logging.FileHandler(filename=log_name, encoding='utf-8') 
            self.fh.setLevel(level=logging.DEBUG)
            self.fh.setFormatter(fmt=formatter)
            self.logger_f.addHandler(self.fh)

    def debug(self, message):
        self.logger_c.debug(Fore.BLUE + "DEBUG - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))

    def info(self, message):
        self.logger_c.info(Fore.GREEN + "INFO - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))

    def warning(self, message):
        self.logger_c.warning(Fore.YELLOW + "WARNING - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))

    def error(self, message):
        self.logger_c.error(Fore.LIGHTRED_EX + "ERROR - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))

    def critical(self, message):
        self.logger_c.critical(Fore.RED + "CRITICAL - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))


if __name__ == '__main__':

    log = MyLogger(logger_c="Console", logger_f="FileLog", log_name="test")
    log.debug("this is a test")
    log.info("this is a test")
    log.warning("this is a test")
    log.error("this is a test")
    log.critical("this is a test")
