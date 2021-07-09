# -*- coding: utf-8 -*-
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger(name="test")

ch = logging.StreamHandler()
fmt = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(filename)s %(funcName)s:%(lineno)d %(message)s')
ch.setFormatter(fmt)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)
logger.info("PROGRESS", extra={"event_type": "EventType.PROGRESS",
                               "status": "运行中",
                               "total": 100, "current": 5})
