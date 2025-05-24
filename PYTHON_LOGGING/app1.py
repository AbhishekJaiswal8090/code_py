import logging 
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("app4.log")
file_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
# Adding formatter to both console and file handler 
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Adding handlers to the logger 
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def add_two_num(a, b):
    logger.info("You are trying to add two numbers")
    print(a+b)
    return a + b

add_two_num(2, 4)