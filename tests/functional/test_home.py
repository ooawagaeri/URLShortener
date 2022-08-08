def test_home_page_with_fixture(test_client):
    """
    Tests home page response.
    Verifies if correct elements are loaded
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome to URL Shortener" in response.data


def test_home_page_with_fixture_empty_post(test_client):
    """
    Tests uploading of empty fields response.
    Verifies if correct error message is loaded.
    """
    response = test_client.post('/',
        data=dict(url="", custom_id=""),
        follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Oh on! The URL is required." in response.data


def test_home_page_with_fixture_duplicate_custom_id_post(test_client):
    """
    Tests uploading of custom id response when already exist.
    Verifies if correct error message is loaded.
    """
    response = test_client.post('/',
        data=dict(url="https://abc.com/", custom_id="a"),
        follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Oh no! Please enter different custom id." in response.data


def test_redirect_with_fixture(test_client):
    """
    Tests page redirection response to GDS blog.
    Verifies if correct redirect elements are loaded.
    """
    response = test_client.get('/a')
    assert response.status_code == 302
    assert b"https://blog.gds-gov.tech/terragrunt-in-retro-i-would-have-done-these%20few-things-e5aaac451942" in response.data
