import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="thema4.log", level=logging.NOTSET)


def list_sum(list):
    if len(list) == 0:
        logger.warning("List is empty.")
        return

    logger.info(list)

    sum = 0
    for item in list:
        sum += item
        logger.debug(f"Add: {item} => {sum}")

    logger.info(sum)


if __name__ == "__main__":
    list = [7, 8, 24, 469, 274, 82, 698, 84]
    list_sum(list=list)
