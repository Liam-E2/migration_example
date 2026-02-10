from typing import Protocol
from copy import deepcopy
from hashlib import md5, sha256
import base64
import json
import logging

from .resource_type import ResourceType


class IdService(Protocol):
    logger: logging.Logger = logging.getLogger()
    fields_to_exclude: dict[ResourceType, list[str]]
    field_blocklist: list[str]

    def __init__(self):
        logging.basicConfig(level=logging.INFO)


    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
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


class IdServiceMd5(IdService):
    fields_to_exclude = {
        ResourceType.PERSON: ["metadata.lastVerifiedDate"],
        ResourceType.THING: ["metadata.observedDate"],
        ResourceType.PLACE: ["metadata.lastVerifiedDate"]
    }
    field_blocklist: list[str] = ["timestamp", "id"]

    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        all_fields_to_exclude = self.field_blocklist
        all_fields_to_exclude.extend(self.fields_to_exclude.get(resource_type, []))

        filtered_data = json.dumps(self.exclude_fields(data, all_fields_to_exclude), sort_keys=True)
        return base64.b64encode(md5(filtered_data.encode()).digest()).decode()


class IdServiceSha256(IdService):
    fields_to_exclude = {
        ResourceType.PERSON: ["metadata.lastVerifiedDate"]
        }
    field_blocklist: list[str] = ["timestamp", "id"]

    def generate_id(self, data: dict, resource_type: ResourceType) -> str:
        all_fields_to_exclude = self.field_blocklist
        all_fields_to_exclude.extend(self.fields_to_exclude.get(resource_type, []))

        filtered_data = json.dumps(self.exclude_fields(data, all_fields_to_exclude), sort_keys=True)
        return base64.b64encode(sha256(filtered_data.encode()).digest()).decode()