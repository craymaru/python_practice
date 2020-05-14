"""
Log level:

CRITICAL
ERROR
WANING
INFO
DEBUG

"""

import logging

logging.basicConfig(filename="logging-test.log", level=logging.DEBUG)

logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.info("info {}".format("test"))
logging.info("info %s %s" % ("test1", "test2"))
logging.info("info %s %s", "test3", "test4")