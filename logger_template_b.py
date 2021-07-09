# -*- coding:utf-8 -*-
import logging
import os
import sys


class Log(object):

    """
        %(levelno)s     打印日志级别的数值
        %(levelname)s   打印日志级别名称
        %(pathname)s    打印当前执行程序的路径，其实就是sys.argv[0]
        %(filename)s    打印当前执行程序名
        %(funcName)s    打印日志的当前函数
        %(lineno)d      打印日志的当前行号
        %(asctime)s     打印日志的记录时间
        %(thread)d      打印线程ID
        %(threadName)s  打印线程的名称
        %(process)d     打印进程的ID
        %(message)s     打印日志的信息

        LOG LEVEL       CRITICAL > ERROR > WARNING > INFO > DEBUG
    """

    def __init__(self, file_name=None, log_name=None):

        self.logger = logging.getLogger(file_name)  # 添加日志器
        self.logger.setLevel(level=logging.INFO)  # 设置日志级别
        self.console_format = logging.Formatter(fmt='[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(levelname)s] %(message)s')  # 设置日志格式
        self.file_format = logging.Formatter(fmt='[%(asctime)s] [%(filename)s] [line:%(lineno)d] [%(levelname)s] %(message)s')  # 设置日志格式
        self.log_dir = os.path.join(sys.path[0], 'logs', log_name)  # 日志文件名

        if not self.logger.handlers:

            # add a console handler
            ch = logging.StreamHandler()  # 添加控制台处理器
            ch.setLevel(level=logging.INFO)  # 设置处理器的日志级别
            ch.setFormatter(self.console_format)  # 处理器添加格式
            self.logger.addHandler(ch)  # 日志器添加处理器

            # add a file handler
            fh = logging.FileHandler(filename=self.log_dir, encoding='utf-8')  # 添加文件处理器
            fh.setLevel(level=logging.INFO)  # 设置处理器的日志级别
            fh.setFormatter(self.file_format)   # 处理器添加格式
            self.logger.addHandler(fh)  # 日志器添加处理器

        # self.logger.removeHandler(fh)
        # self.logger.handlers = self.logger.handlers[:1]  # 将handlers列表切片截取第一和第二个元素再付给handlers列表

    def init_logger(self):
        return self.logger


if __name__ == '__main__':

    logger = Log(file_name=None, log_name='test.log').init_logger()  # 实例化日志类，调用get_logger方法

    logger.info('======[INFO TEST]======')
    logger.debug('======[DEBUG TEST]======')
    logger.warning('======[WARNING TEST]======')
    logger.error('======[ERROR TEST]======')
    logger.critical('======[CRITICAL TEST]======')
