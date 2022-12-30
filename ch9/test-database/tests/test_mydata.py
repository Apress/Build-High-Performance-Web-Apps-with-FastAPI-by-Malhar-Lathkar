from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from ..main import app, get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite3"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def test_get_db():
    try:
        db = TestingSession()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = test_get_db

client = TestClient(app)


def test_add_book():
    response = client.post(
        "/books/",
        json={"id":1,"title": "Jungle Book", "price": 500},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Computer"
    assert "id" in data
    book_id = data["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Jungle Book"
    assert data["id"] == book_id
