import logging

LOG_HAHAH = "%(asctime)s======%(levelname)s+++++++%(message)s"
logging.basicConfig(filename="wahahaha.log",level=logging.WARNING,format = LOG_HAHAH) #进行配置





logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")

logging.log(logging.DEBUG,"This is a debug log.")
logging.log(logging.INFO,"This is a info log")

