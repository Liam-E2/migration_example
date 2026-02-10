from dataclasses import dataclass

@dataclass
class Entry:
    record_id: str
    record_type: str


class MockDataStore:
    def __init__(self):
        self.entries = {}


    def put_entry(self, id: str, entry: Entry) -> None:
        self.entries[id] = entry


    def get_entry(self, id: str, entry: Entry) -> Entry | None:
        return self.entries.get(id)
