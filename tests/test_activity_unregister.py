from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_signup_updates_activity_participants_without_refresh():
    activity_name = "Basketball Team"
    email = "student@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")

    assert response.status_code == 200
    assert email in client.get("/activities").json()[activity_name]["participants"]

    client.delete(f"/activities/{activity_name}/unregister?email={email}")


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")

    assert response.status_code == 200
    assert email not in client.get("/activities").json()[activity_name]["participants"]

    client.post(f"/activities/{activity_name}/signup?email={email}")
