import logging

loging_format = '{lineno}--{name}--{asctime}--{message}'
logging.basicConfig(filename='log_file.log',level=logging.DEBUG,style='{',format=loging_format,filemode='w')

logging.debug("This is debug")
logging.warning("this is warning")
logging.error("This is error")
logging.info("This is info")
logging.critical("this is critical")