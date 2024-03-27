import logging


# logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO)

#

logger = logging.Logger(name="my_logger")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(message)s")
handler = logging.FileHandler("pylogs.log", mode="a")

handler.setFormatter(formatter)
logger.addHandler(handler)



x_nums = [4, 6, 22, 56, 98]
y_nums = [3, 4, 2, 0, 8]

try:
    logger.info("Start")
    for x_val, y_val in zip(x_nums, y_nums):
        x, y = x_val, y_val
        res = x / y
        # print(res)
        logger.info(f"Successful operation {res}")
except ZeroDivisionError as err:
    logger.error(f"An error occurred: {err}")
finally:
    logger.info("Close app")