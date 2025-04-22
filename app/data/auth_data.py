import json
import os

USER_DB_PATH = "users.json"

def load_users():
    if not os.path.exists(USER_DB_PATH):
        return []
    with open(USER_DB_PATH, "r") as f:
        return json.load(f).get("users", [])

def save_users(users):
    with open(USER_DB_PATH, "w") as f:
        json.dump({"users": users}, f, indent=4)
