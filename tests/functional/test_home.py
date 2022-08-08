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
    Tests uploading of empty fields
    Verifies if correct error message is loaded
    """
    response = test_client.post('/',
        data=dict(url="", custom_id=""),
        follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Oh on! The URL is required." in response.data