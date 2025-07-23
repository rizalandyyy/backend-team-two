def test_index(client):
    """Test the index route."""
    response = client.get("/")
    assert response.status_code == 200
