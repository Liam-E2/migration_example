from src.id_service import IdServiceMd5, IdServiceSha256, ResourceType
from src.migration import migrate_id_services


def test_migration(people, data_store, new_people):
    """
    Given the pre-populated data-store, replay 'person' data using migrate_id_services,
    demonstrating that ids have been migrated.
    """
    new_service = IdServiceSha256()
    old_service = IdServiceMd5()

    for person in people:
        migrate_id_services(person, ResourceType.PERSON, old_service, new_service, data_store)
        old_id = old_service.generate_id(person, ResourceType.PERSON)
        new_id = new_service.generate_id(person, ResourceType.PERSON)
        assert data_store.get_entry(old_id) is None
        assert data_store.get_entry(new_id) is not None
    
    assert len(data_store.entries) == 3

    for person in new_people:
        migrate_id_services(person, ResourceType.PERSON, old_service, new_service, data_store)
        old_id = old_service.generate_id(person, ResourceType.PERSON)
        new_id = new_service.generate_id(person, ResourceType.PERSON)
        assert data_store.get_entry(old_id) is None
        assert data_store.get_entry(new_id) is not None
    
    assert len(data_store.entries) == 5