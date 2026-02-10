from src.id_service import IdService, IdServiceMd5, ResourceType


def test_exclude_fields():
    exclude_fields = ["payload.payload1", "nested"]
    data = {
        "id": "hmmm", 
        "payload": {
            "payload1": ["data1", "data2"], 
            "payload2": ["data3", "data4"]
            },
        "nested": {"nested": {"field"}, "don't": "keep"}
        }
    expected = {
        "id": "hmmm",
        "payload": {"payload2": ["data3", "data4"]}
    }

    assert expected == IdService.exclude_fields(data, exclude_fields)


def test_initial_population(data_store, people):
    service = IdServiceMd5()
    for person in people:
        assert data_store.get_entry(service.generate_id(person, ResourceType.PERSON)) is not None
