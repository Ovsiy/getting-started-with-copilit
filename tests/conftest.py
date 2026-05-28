from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client():
    """Create a fresh TestClient for each test."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def restore_activities_state():
    """Keep tests isolated by restoring global in-memory state after each test."""
    snapshot = deepcopy(activities)

    yield

    activities.clear()
    activities.update(snapshot)
