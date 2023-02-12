import logging, coloredlogs


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console =  logging.StreamHandler()
console.setLevel(logging.DEBUG)

formatter = coloredlogs.ColoredFormatter(fmt="[%(asctime)s] [%(levelname)s]: %(message)s")

console.setFormatter(formatter)

logger.addHandler(console)