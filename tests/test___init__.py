from shoppingapp import create_app

def test_factory():
    assert create_app().testing
