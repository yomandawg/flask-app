from shoppingapp import create_app
import json
import pytest


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    return app.test_client()


def test_factory():
    assert not create_app().testing


def test_api_handler(client):
    res = client.get("/api/test")
    res = json.loads(json.loads(res.data))
    assert res["name"] == "cs"
    assert res["age"] == 34

# def test_trend(client):
#     res = client.get("/api/trend/corona")
#     print("res.data", res.data)
#     res = json.loads(json.loads(res.date))
#     assert res["startDate"] == "2019-12-30"
