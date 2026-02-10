from typing import Protocol
from copy import deepcopy
from hashlib import md5, sha256
import logging

from .resource_type import ResourceType


class IdService[Protocol]:
    logger = logging.getLogger()
    exclude_fields: dict[ResourceType, list[str]]

    def __init__(self):
        logging.basicConfig(level=logging.INFO)


    def generate_id(self, data: dict, **kwargs) -> str:
        pass


    @staticmethod
    def exclude_fields(data: dict, exclude_fields: list[str]) -> dict:
        """
        Given a generic dict 'data' and exclude_fields, a list of JSON paths like
            ["field1", "field2.subfield", ...]
        
        returns a deepcopied version of data with the specified paths excluded.
        """
        pass


class IdServiceMd5:
    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        pass


class IdServiceSha256:
    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        pass
