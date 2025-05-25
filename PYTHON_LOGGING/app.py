import logging

logging.basicConfig(
     level=logging.DEBUG,            # Log everything from DEBUG and above
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',

    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger("ArithemeticApp")
def add(a,b):
    result =a+b
    logger.debug(f"Adding {a ,b} ={result}")
    return result
def subtract(a,b):
    result =a-b
    logger.debug(f"Subtracting {a , b} ={result}")
    return result
def multiply(a,b):
    result =a*b
    logger.error(f"Multiplying {a ,b} ={result}")
    logger.info("WHat the hell did happen here")
    return result
def divide(a,b):
    try:
        result =a/b
        logger.debug(f"dividing {a , b} ={result}")
        return result 
    except ZeroDivisionError:
        logger.error("Trying to divide by zero")
        return None
    
add(2,3)
subtract(3,2)
multiply(2,3)
divide(2,2)    