#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging
import platform
import sys

from pweight import photo

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("logs/pweight.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)

logger.info("Start print log")


def main():
    if platform.system() != "Linux":
        return 1
    p = photo.Photos()
    p.manager()

if __name__ == '__main__':
    sys.exit(main())
