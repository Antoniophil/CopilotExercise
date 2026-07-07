from fastapi.testclient import TestClient

from src.app import app


def test_signup_and_remove_participant():
    client = TestClient(app)

    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "student@example.com"},
    )
    assert response.status_code == 200

    activity_response = client.get("/activities")
    assert activity_response.status_code == 200
    chess_club = activity_response.json()["Chess Club"]
    assert "student@example.com" in chess_club["participants"]

    delete_response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "student@example.com"},
    )
    assert delete_response.status_code == 200

    activity_response = client.get("/activities")
    chess_club = activity_response.json()["Chess Club"]
    assert "student@example.com" not in chess_club["participants"]
