from src.id_service import IdService


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
