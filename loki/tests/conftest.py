import pytest

from .. import create_app


@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    # create the app with common test config
    app = create_app()
    app.config['TESTING'] = True

    ctx = app.app_context()
    ctx.push()

    client = app.test_client()

    yield client
