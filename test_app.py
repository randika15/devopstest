from app import app

def test_hello():
    response = app.test_client().get("/")
    assert response.data == b"Hello, World!"    
    assert response.status_code == 200
    assert ="Hello, World!" in response.data
    