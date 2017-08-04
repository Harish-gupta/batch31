import logging
logging.basicConfig(filename="log1.txt", level=logging.DEBUG, format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("info message")
cost=300
logging.debug("cost=%s"%cost)
logging.warn("warning")
logging.error("error")
logging.exception("exception")