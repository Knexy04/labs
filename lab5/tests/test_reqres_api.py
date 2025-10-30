import os
import re
import requests

BASE_URL = os.getenv("API_BASE_URL", os.getenv("REQRES_BASE_URL", "https://jsonplaceholder.typicode.com"))


def test_get_post_by_id_returns_200_and_expected_shape():
    post_id = 1
    resp = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert resp.status_code == 200
    body = resp.json()

    assert body.get("id") == post_id
    assert isinstance(body.get("userId"), int)
    assert isinstance(body.get("title"), str)
    assert isinstance(body.get("body"), str)


def test_create_post_returns_201_and_echoes_fields():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = requests.post(f"{BASE_URL}/posts", json=payload)
    # jsonplaceholder returns 201 Created
    assert resp.status_code == 201
    body = resp.json()

    # API echoes back sent fields and assigns id (101)
    assert body.get("title") == payload["title"]
    assert body.get("body") == payload["body"]
    assert body.get("userId") == payload["userId"]
    assert "id" in body and isinstance(body["id"], int)


def test_update_post_put_returns_200_and_updates_fields():
    post_id = 1
    payload = {"id": post_id, "title": "updated", "body": "lorem", "userId": 1}
    resp = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    assert resp.status_code == 200
    body = resp.json()

    assert body.get("id") == post_id
    assert body.get("title") == payload["title"]
    assert body.get("body") == payload["body"]
    assert body.get("userId") == payload["userId"]


def test_get_nonexistent_post_returns_empty_object_with_200():
    # jsonplaceholder returns 200 with {} for many nonexistent resources
    resp = requests.get(f"{BASE_URL}/posts/999999")
    assert resp.status_code == 200
    json_body = resp.json()
    assert isinstance(json_body, dict)
    assert json_body == {} or json_body.get("id") != 999999
