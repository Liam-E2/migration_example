import pytest
from time import time
from datetime import date
from src.data_store import MockDataStore, Entry
from src.id_service import ResourceType, IdServiceMd5


@pytest.fixture
def people() -> list[dict]:
    # Similar, but different - here, id doesn't work because the same ID points to 5 'different people'
    # Looking to use an ID based on meaningful attributes instead
    return [
        {"id": 1, "first_name": "Liam", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-10"}},
        {"id": 1, "first_name": "Joe", "last_name": "Earley2", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-11"}},
        {"id": 1, "first_name": "Liam", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-12"}},
        {"id": 1, "first_name": "William", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-13"}},
        {"id": 1, "first_name": "Liam", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-14"}}
    ]

@pytest.fixture
def new_people():
    return [
        {"id": 1, "first_name": "Test", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-13"}},
        {"id": 1, "first_name": "Test2", "last_name": "Earley", "timestamp": str(time()), "metadata": {"lastVerifiedDate": "2026-02-14"}}
    ]

@pytest.fixture
def data_store(people) -> MockDataStore:
    mock_store = MockDataStore()
    id_service = IdServiceMd5()

    for person in people:
        mock_store.put_entry(
            id_service.generate_id(person, ResourceType.PERSON), 
            Entry(record_type=ResourceType.PERSON, record_id=person.get('id'))
            )

    return mock_store
