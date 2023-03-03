import pytest


@pytest.fixture
def client(app):
    return app.test_client()


def test_proxy(mocker):
    mock_session = mocker.patch('app.my_proxy_client.session')
    test_payload = {'test': 'test'}
    result = client.post('/proxy', data=test_payload)
    assert result
