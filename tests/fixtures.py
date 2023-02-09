import pytest


@pytest.fixture
def create_login_user(client):
    """Фикстура создания логина пользователя"""
    user_data = {
        'username': 'test',
        'first_name': 'test',
        'last_name': 'test',
        'email': 'test@test.ru',
        'password': '1q2w3eR$',
        'password_repeat': '1q2w3eR$'
    }
    create_user_response = client.post('/core/signup', data=user_data, content_type='application/json')
    login_user_response = client.post(
        '/core/login',
        {
            'username': user_data['username'],
            'password': user_data['password']
        },
        content_type='application/json'
    )

    return create_user_response, login_user_response
