from app import app

def test_app_exists():
    # A simple test to ensure the Flask app object can be imported and initialized
    assert app is not None
