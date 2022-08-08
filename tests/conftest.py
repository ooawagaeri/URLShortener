import pytest
from core import app
from datetime import datetime
from core.models import ShortUrls


@pytest.fixture(scope='module')
def new_shortUrl():
    """
    Creates new ShortUrl object for unit testing.
    """
    date_now_str = '08/08/22 08:08:08'
    date_obj = datetime.strptime(date_now_str, '%d/%m/%y %H:%M:%S')
    
    url = ShortUrls(
        original_url="https://abc.com/", short_id="12345abc", created_at=date_obj)
    return url


@pytest.fixture(scope='module')
def test_client():
    """
    Initializes test flask client for testing.
    """
    app.config.update(
        TESTING=True,
    )
    
    with app.test_client() as testing_client:
        # Establish application context
        with app.app_context():
            yield testing_client