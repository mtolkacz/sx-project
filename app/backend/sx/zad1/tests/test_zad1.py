from django import urls


def test_zad1_api_get_method(client):
    url = urls.reverse('zad1:api')
    resp = client.get(url)

    assert resp.status_code == 405


def test_zad1_200_ok_and_sha(client):
    post_data = """{
        "data_list": [
            {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
        ]
    }"""
    response = client.post(
        urls.reverse('zad1:api'),
        post_data,
        content_type='application/json',
    )

    assert response.status_code == 200

    data = response.json()

    assert 'result' in data
    assert 'sha256' in data['result'][0]
    assert 'd371d82da0bcb79c71d8a9d56a5272732f01ed3496887620c6f10ef9fa823e3a' == data['result'][0]['sha256']


def test_zad1_incorrect_structure(client):
    post_data = """{
        "data_list": [
            {"incorrect": "Jan", "structure": "Kowalski", "birth_date": "1977-11-10"}
        ]
    }"""
    response = client.post(
        urls.reverse('zad1:api'),
        post_data,
        content_type='application/json',
    )

    assert response.status_code == 400


def test_zad1_incorrect_input(client):
    post_data = """{
        "incorrect_input": [
            {"first_name": "Jan", "second_name": "Kowalski", "birth_date": "1977-11-10"}
        ]
    }"""
    response = client.post(
        urls.reverse('zad1:api'),
        post_data,
        content_type='application/json',
    )

    assert response.status_code == 400
