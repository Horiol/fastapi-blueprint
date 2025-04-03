from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_graphql_books_query():
    query = """
        query {
            books {
                id
                title 
                author
            }
        }
    """

    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200

    data = response.json()
    assert "data" in data
    assert "books" in data["data"]
    assert isinstance(data["data"]["books"], list)

    # If any books exist, verify the structure
    for book in data["data"]["books"]:
        assert "id" in book
        assert "title" in book
        assert "author" in book
        assert isinstance(book["id"], int)
        assert isinstance(book["title"], str)
        assert isinstance(book["author"], str)


def test_graphql_invalid_query():
    query = """
        query {
            invalid {
                field
            }
        }
    """

    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200  # GraphQL returns 200 even for errors

    data = response.json()
    assert "errors" in data
