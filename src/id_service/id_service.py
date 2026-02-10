from typing import Protocol
from hashlib import md5
import logging


class IdService[Protocol]:
    logger = logging.getLogger()

    def __init__(self):
        logging.basicConfig(level=logging.INFO)


    def generate_id(self) -> str:
        pass


class IdServiceV0:
    def generate_id(self) -> str:
        pass


class IdServiceV1:
    def generate_id(self) -> str:
        pass
