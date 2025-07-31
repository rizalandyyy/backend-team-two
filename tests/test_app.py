def test_index(client):
    """Test the index route (expect 404 since it's not defined)."""
    response = client.get("/")
    assert response.status_code == 404
