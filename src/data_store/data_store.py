from dataclasses import dataclass
from src.id_service.resource_type import ResourceType


@dataclass
class Entry:
    record_id: str
    record_type: ResourceType


class MockDataStore:
    def __init__(self):
        self.entries = {}


    def put_entry(self, id: str, entry: Entry) -> None:
        self.entries[id] = entry


    def get_entry(self, id: str) -> Entry | None:
        return self.entries.get(id)
    

    def pop_entry(self, id: str) -> Entry | None:
        return self.entries.pop(id, None)
