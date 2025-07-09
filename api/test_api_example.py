import httpx


def test_example_api_status():
    response = httpx.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    json_data = response.json()
    assert "userId" in json_data
