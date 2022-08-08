from datetime import datetime


def test_new_shortUrl_with_fixture(new_shortUrl):
    """
    Tests creation of new ShortUrl.
    Verifies if input attributes are defined correctly
    """
    date_now_str = '08/08/22 08:08:08'
    date_obj = datetime.strptime(date_now_str, '%d/%m/%y %H:%M:%S')

    assert new_shortUrl.original_url == "https://abc.com/"
    assert new_shortUrl.short_id == "12345abc"
    
    date_now_str_false = '09/09/22 09:09:09'
    date_obj_false = datetime.strptime(date_now_str_false, '%d/%m/%y %H:%M:%S')
    
    assert new_shortUrl.created_at != date_obj_false
    assert new_shortUrl.created_at == date_obj