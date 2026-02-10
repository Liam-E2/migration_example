from .id_service.id_service import IdService, ResourceType
from src.data_store import MockDataStore, Entry


def migrate_id_services(data: dict, resource_type: ResourceType, old_service: IdService, new_service: IdService, data_store: MockDataStore):
    """
    Migrate from one impementation of IdService to another.
    """
    new_id = new_service.generate_id(data, resource_type)
    old_id = old_service.generate_id(data, resource_type)

    if data_store.get_entry(old_id) is not None:
        # ordering - don't delete until successful write. Should be all in one transaction
        data_store.put_entry(new_id, Entry(data.get("id", ""), resource_type))
        data_store.pop_entry(old_id)
    else:
        data_store.put_entry(new_id, Entry(data.get("id", ""), resource_type))
