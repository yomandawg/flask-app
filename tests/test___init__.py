from shoppingapp import create_app

def test_factory():
    assert not create_app().testing
