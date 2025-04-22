import json
import os
from typing import Optional

USERS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "users.json")


def load_users() -> dict:
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users: dict) -> None:
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


def register_user(email: str, password: str) -> bool:
    users = load_users()
    if email in users:
        return False
    users[email] = {"password": password}
    save_users(users)
    return True


def login_user(email: str, password: str) -> bool:
    users = load_users()
    return email in users and users[email]["password"] == password
