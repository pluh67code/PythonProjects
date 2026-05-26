from user import User
import json
file = "user_data.json"

def load_users() -> dict[str, dict]:
    try:
        with open(file, "r") as f:
            users = json.load(f)
    except:
        users = {}

    return users

def save_user(username: str, password: str):
    new_user = User(username, password)
    users = load_users()
    users[username] = new_user.to_dict()

    with open(file, "w") as f:
        json.dump(users, f)

def find_user(username: str, password: str) -> User | None:
    try: 
        with open(file, "r") as f:
            users = json.load(f)
    except:
        return None

    for user_key, user_dct in users.items():
        if username == user_key and password == user_dct["password"]:
            return User.from_dict(user_dct)
    return None

def username_taken(username: str) -> bool:
    return username in load_users().keys()

def valid_entries(username: str, password: str) -> bool:
    return username and password and any(char.isdigit() for char in password)