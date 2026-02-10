import pytest

from src.data_store import MockDataStore, Entry
from src.id_service import ResourceType

@pytest.fixture
def test_data_store():
    mock_store = MockDataStore()
    mock_store.put_entry()