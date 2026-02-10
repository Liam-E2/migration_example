import pytest

from src.data_store import MockDataStore, Entry

@pytest.fixture
def test_data_store():
    mock_store = MockDataStore()
    mock_store.put_entry()