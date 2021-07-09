# -*- coding:utf-8 -*-
import logging
import os.path
import time
import sys
from colorama import Fore, Style


class MyLogger(object):

    def __init__(self, logger_c, logger_f, log_name):

        self.logger_c = logging.getLogger(name=logger_c)  # 定义对应的程序模块名name，默认是root
        self.logger_c.setLevel(level=logging.DEBUG)  # 指定最低的日志级别 critical > error > warning > info > debug

        self.logger_f = logging.getLogger(name=logger_f)
        self.logger_f.setLevel(level=logging.DEBUG)

        log_time = time.strftime("%Y-%m-%d:%H-%M-%S", time.localtime(time.time()))
        log_name = os.getcwd() + "/logs/" + log_name + ".log"

        # 定义handler的输出格式
        # formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(name)s - %(message)s")
        formatter = logging.Formatter("%(asctime)s - %(name)s [line:%(lineno)d] - %(message)s")

        # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志，解决重复打印的问题
        if not self.logger_c.handlers:
            self.ch = logging.StreamHandler()  # 日志输出到屏幕控制台
            self.ch.setLevel(level=logging.DEBUG)  # 设置日志等级
            self.ch.setFormatter(fmt=formatter)
            self.logger_c.addHandler(self.ch)  # 给logger添加handler

        if not self.logger_f.handlers:
            self.fh = logging.FileHandler(filename=log_name, encoding='utf-8')  # 日志写入文件
            self.fh.setLevel(level=logging.DEBUG)
            self.fh.setFormatter(fmt=formatter)
            self.logger_f.addHandler(self.fh)

    def debug(self, message):
        self.logger_c.debug(Fore.BLUE + "[DEBUG] - " + str(message) + Style.RESET_ALL)
        self.logger_f.debug(str(message))

    def info(self, message):
        self.logger_c.info(Fore.GREEN + "[INFO] - " + str(message) + Style.RESET_ALL)
        self.logger_f.info(str(message))

    def warning(self, message):
        self.logger_c.warning(Fore.YELLOW + "[WARNING] - " + str(message) + Style.RESET_ALL)
        self.logger_f.warning(str(message))

    def error(self, message):
        self.logger_c.error(Fore.CYAN + "[ERROR] - " + str(message) + Style.RESET_ALL)
        self.logger_f.error(str(message))

    def critical(self, message):
        self.logger_c.critical(Fore.RED + "[CRITICAL] - " + str(message) + Style.RESET_ALL)
        self.logger_f.critical(str(message))


if __name__ == '__main__':

    log = MyLogger(logger_c="[console] [x.py]", logger_f="[file] [x.py]", log_name="test")
    log.debug("this is a test")
    log.info("this is a test")
    log.warning("this is a test")
    log.error("this is a test")
    log.critical("this is a test")
