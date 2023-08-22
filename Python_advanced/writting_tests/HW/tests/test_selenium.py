import pytest
from ..Ya_auth_selenium import yandex_login


@pytest.mark.parametrize(
    'email, password',
    [('', ''),
     ('', '')]
)
def test_yandex_auth(email, password):
    result = yandex_login(email, password)
    assert result == 'Яндекс ID'