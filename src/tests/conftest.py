import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture
def test_app(scope="module"):
    client = TestClient(app)
    yield client  # testing happens here
