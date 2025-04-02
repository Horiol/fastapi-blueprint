from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_books_post_and_delete():
    # First create a book to delete
    response = client.post(
        "/books", json={"title": "Test Book", "author": "Test Author"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Book"
    assert response.json()["author"] == "Test Author"

    book_id = response.json()["id"]

    # Delete the book
    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == book_id

    # Verify book is deleted
    get_response = client.get("/books")
    assert get_response.status_code == 200
    assert not any(book["id"] == book_id for book in get_response.json())


def test_invalid_posts():
    response = client.post("/books", json={"invalid": "data"})
    assert response.status_code == 422

    response = client.post("/books", json={"title": "Test Book"})
    assert response.status_code == 422

    response = client.post("/books", json={"author": "Test Author"})
    assert response.status_code == 422

    response = client.post("/books", json={})
    assert response.status_code == 422
