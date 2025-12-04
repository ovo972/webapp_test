import pytest
from api.sample_api import app  # adaptez le chemin si nécessaire

@pytest.fixture
def test_client():
    return app.test_client()