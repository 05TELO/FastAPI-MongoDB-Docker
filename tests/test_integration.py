import pytest


@pytest.mark.parametrize(
    "data",
    [
        {
            "phone": "+7 111 111 11 11",
            "email": "xxx@gmail.com",
            "first_name": "Bob",
        },
        {
            "phone": "+7 222 222 22 22",
            "email": "yyy@gmail.com",
            "first_name": "Alice",
        },
    ],
)
async def test_get_form(client, data):
    url = "http://127.0.0.1:8000/get_form"

    response = await client.post(url, json=data)

    assert response.status_code == 200
    assert response.json() == {"name": "Registration Form"}
