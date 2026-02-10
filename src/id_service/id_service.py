from typing import Protocol
from copy import deepcopy
from hashlib import md5, sha256
import json
import logging

from .resource_type import ResourceType


class IdService(Protocol):
    logger = logging.getLogger()
    exclude_fields: dict[ResourceType, list[str]]
    field_blocklist: list[str]

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
        copied = deepcopy(data)
        for field in exclude_fields:
            if "." not in field:
                copied.pop(field, None)
                continue
            
            split_path = field.split(".")
            sub_dict = copied
            for key in split_path[:-1]:
                sub_dict = sub_dict[key]
            sub_dict.pop(split_path[-1], None)

        return copied


class IdServiceMd5:
    exclude_fields = {
        ResourceType.PERSON: ["metadata.lastVerifiedDate"],
        ResourceType.THING: ["metadata.observedDate"],
        ResourceType.PLACE: ["metadata.lastVerifiedDate"]
    }
    field_blocklist: list[str] = ["timestamp"]

    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        fields_to_exclude = self.field_blocklist
        fields_to_exclude.extend(self.exclude_fields.get(resource_type, []))

        filtered_data = json.dumps(self.exclude_fields(data, fields_to_exclude))
        return md5(filtered_data)


class IdServiceSha256:
    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        fields_to_exclude = self.field_blocklist
        fields_to_exclude.extend(self.exclude_fields.get(resource_type, []))
        
        filtered_data = json.dumps(self.exclude_fields(data, fields_to_exclude))
        return md5(filtered_data)