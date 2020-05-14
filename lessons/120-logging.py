"""
Log level:

CRITICAL
ERROR
WANING
INFO
DEBUG

"""

import logging

# formatter = "[%(asctime)s] %(levelname)s: %(message)s"
# logging.basicConfig(filename="logging-test.log", level=logging.DEBUG)
# logging.basicConfig(level=logging.INFO, format=formatter)
logging.basicConfig(level=logging.INFO)




logging.critical("critical")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

logging.info("info {}".format("test"))
logging.info("info %s %s" % ("test1", "test2"))
logging.info("info %s %s", "test3", "test4")


# Filter
class NoPassFilter(logging.Filter):
    def filter(self, record):
        log_message = record.getMessage()
        return "password" not in log_message


# Logger and Handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("hundler-log-test.log")
logger.addHandler(handler)
logger.addFilter(NoPassFilter())
logger.debug("debug from logger")
logger.debug("This is the password = pw")

