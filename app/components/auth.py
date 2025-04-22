from app.data import auth_data
import hashlib

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email: str, password: str):
    users = auth_data.load_users()
    hashed = hash_password(password)
    return any(user["email"] == email and user["password"] == hashed for user in users)

def register(email: str, password: str):
    users = auth_data.load_users()
    if any(user["email"] == email for user in users):
        return False
    users.append({
        "email": email,
        "password": hash_password(password)
    })
    auth_data.save_users(users)
    return True
